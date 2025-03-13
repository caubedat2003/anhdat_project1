from django.contrib.auth.hashers import make_password, check_password
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Customer, Address
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import CustomerSerializer , AddressSerializer
from rest_framework.generics import RetrieveAPIView

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            first_name = data.get("first_name")
            last_name = data.get("last_name")
            username = data.get("username")
            password = data.get("password")  
            email = data.get("email")
            phone_number = data.get("phone_number")

            if not all([first_name, last_name, username, password, email, phone_number]):
                return JsonResponse({"error": "All fields are required."}, status=400)

            # Check if username or email already exists
            if Customer.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already taken."}, status=400)
            if Customer.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already registered."}, status=400)

            hashed_password = make_password(password)

            user = Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=hashed_password,  
                email=email,
                phone_number=phone_number
            )

            return JsonResponse({"message": "User registered successfully!", "user_id": user.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

    return JsonResponse({"error": "Only POST method allowed."}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            # Find user by username
            user = Customer.objects.filter(username=username).first()
            if not user:
                return JsonResponse({"error": "Invalid username or password."}, status=400)

            # Verify the password
            if not check_password(password, user.password):
                return JsonResponse({"error": "Invalid username or password."}, status=400)

            request.session['user_id'] = user.id
            request.session['username'] = user.username

            return JsonResponse({"message": "Login successful!", "user_id": user.id, "username": user.username}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

    return JsonResponse({"error": "Only POST method allowed."}, status=405)

def get_all_customers(request):
    customers = Customer.objects.all().values("first_name", "last_name", "username", "email", "phone_number")
    return JsonResponse(list(customers), safe=False)

def logout_user(request):
    request.session.flush()  # Clears all session data
    return JsonResponse({"message": "Logged out successfully."})

class CustomerListCreateView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a customer by ID
class CustomerDetailView(APIView):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return Response({"message": "Customer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class CustomerSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('name', None) 
        if query:
            customers = Customer.objects.filter(first_name__icontains=query) | Customer.objects.filter(last_name__icontains=query)
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
        return Response({"error": "No search query provided"}, status=status.HTTP_400_BAD_REQUEST)

class CustomerAddressView(RetrieveAPIView):
    serializer_class = AddressSerializer

    def get_object(self):
        customer_id = self.kwargs['customer_id']
        return get_object_or_404(Address, customer_id=customer_id)

def register_page(request):
    return render(request, "register.html")

def login_page(request):
    return render(request, "login.html")

def customer_list_page(request):
    return render(request, "customer_list.html")
