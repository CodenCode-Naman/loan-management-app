from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CustomerSerializer
from .models import Customer
from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import math
from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .tasks import get_credit_score

# POST api - api/apply-loan
# POST api - api/make-payment
# GET api - api/get-statement


# register user api - POST api - api/register-user
class CustomerView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        return Response({"message": "Hello, Customer!"})

    def post(self, request):
        try:
            data = JSONParser().parse(request)

            serializer = CustomerSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                customer = Customer.objects.create(
                    name=data["name"],
                    email_id=data["email_id"],
                    aadhar_id=data["aadhar_id"],
                    annual_income=data["annual_income"],
                )
                get_credit_score.delay(customer.id)

                response_data = {
                    "id": customer.id,
                    "message": "User Registered Successfully!",
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                error_message = serializer.errors
                return Response(
                    {"error": error_message}, status=status.HTTP_400_BAD_REQUEST
                )
        except JSONDecodeError:
            return JsonResponse(
                {
                    "result": "error", 
                    "message": "Json Error"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
