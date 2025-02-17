from django.contrib.auth.hashers import make_password, check_password
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Customer

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

            return JsonResponse({"message": "Login successful!", "user_id": user.id}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

    return JsonResponse({"error": "Only POST method allowed."}, status=405)

def get_all_customers(request):
    customers = Customer.objects.all().values("first_name", "last_name", "username", "email", "phone_number")
    return JsonResponse(list(customers), safe=False)

def register_page(request):
    return render(request, "register.html")

def login_page(request):
    return render(request, "login.html")

def customer_list_page(request):
    return render(request, "customer_list.html")
