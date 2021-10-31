from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from .models.NewCustomer import NewCustomer
from .forms import OurUserForm

# Create your views here.
def index(request):
    prod = None
    categories = Category.get_all_category()
    categoryId = request.GET.get('category')
    if categoryId:
        prod = Product.get_all_products_by_id (categoryId)
    else:
        prod = Product.get_all_products()
    data = {}
    data ['products'] = prod
    data ['categories'] = categories
    print('You are: ',request.session.get('customer'))
    return render(request,'index.html',data)

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    else:
        pd = request.POST
        first_name = pd.get('name')
        last_name = pd.get('lastname')
        email = pd.get('email')
        phone = pd.get('phone')
        password = pd.get('password')

        customer = Customer(first_name = first_name,
                            last_name = last_name,
                            phone = phone,
                            email = email,
                            password = password)

        customer.password = make_password(customer.password)
        customer.save()
        return redirect('homepage')

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_cutomer_by_email(email)
        print(customer)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id


                return redirect('homepage')
            else:
                error_msg = 'Emailid or Password incorrect'
        else:
            error_msg = 'Emailid or Password incorrect'
        print(email,password)
        # print(customer.email,customer.password)
        return render(request,'login.html',{'error':error_msg})

def signup_user(request):
    form = OurUserForm(request.POST)
    return render(request, 'NewSignUP.html',{"form":form})

def logout(request):
    request.session.clear()
    print("logout success")
    return redirect('login')