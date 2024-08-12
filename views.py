from django.shortcuts import render, redirect
from .models import EmployeeDB
#from .models import VehiclesDB
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    data=EmployeeDB.objects.all()
    context={"data":data}
    return render(request, "index.html",context)


def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        id=request.POST.get('id')
        status=request.POST.get('status')
        type=request.POST.get('type')
        gender=request.POST.get('gender')
        # Number=request.POST.get('Number')
        # ModelNumber=request.POST.get('Model Number')
        # ChasisNumber=request.POST.get('Chasis Number')
        # Mileage=request.POST.get('Mileage')
        # RegistrationNumber=request.POST.get('Registration Number')
        # print(Number,ModelNumber,ChasisNumber,Mileage,RegistrationNumber)
        print(name,id,status,type,gender)
        query=EmployeeDB(name=name, id=id, status=status, type=type, gender=gender)
        #query=VehiclesDB(Number=Number, ModelNumber=ModelNumber, ChasisNumber=ChasisNumber, Mileage=Mileage, RegistrationNumber=RegistrationNumber)
        query.save()
        return redirect("/")
    return render(request, "index.html")

# def insertData(request):
#     if request.method=="POST":
#         number=request.POST.get('number')
#         modelNumber=request.POST.get('modelNumber')
#         chasisNumber=request.POST.get('chasisNumber')
#         Mileage=request.POST.get('Mileage')
#         registrationNumber=request.POST.get('registrationNumber')
#         print(number,modelNumber,chasisNumber,Mileage,registrationNumber)
#         query=EmployeeDB(number=number, modelNumber=modelNumber, chasisNumber=chasisNumber, Mileage=Mileage, registrationNumber=registrationNumber)
#         query.save()
#     return render(request, "index.html")

def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        new_id = request.POST.get('id')
        status = request.POST.get('status')
        type = request.POST.get('type')
        gender = request.POST.get('gender')

        # Fetch the current employee
        employee = EmployeeDB.objects.get(id=id)
        # Check if the new ID is already taken by another employee
        while new_id != id and EmployeeDB.objects.filter(id=new_id).exists():
            # If the new ID exists and is different from the current ID
            context = {
                'd': employee,
                'id_error': f'The ID "{new_id}" is already in use. Please choose another ID.'
            }
            return render(request, 'edit.html', context)

        # Update the employee details
        employee.name = name
        employee.id = new_id
        employee.status = status
        employee.type = type
        employee.gender = gender
        employee.save()

        return redirect("/")

    # If GET request, fetch the current employee details
    d = EmployeeDB.objects.get(id=id)
    context = {
        'd': d,
        'id_error': None
    }
    return render(request, 'edit.html', context)

# def updateVehcile(request, Number):
#     if request.method == "POST":
#         Number=request.POST.get('Number')
#         ModelNumber=request.POST.get('Model Number')
#         ChasisNumber=request.POST.get('Chasis Number')
#         Mileage=request.POST.get('Mileage')
#         RegistrationNumber=request.POST.get('Registration Number')

#         vehicle = VehiclesDB.objects.get(Number=Number)

#         vehicle.number = Number
#         vehicle.ChasisNumber = ChasisNumber
#         vehicle.moldelNumber = ModelNumber
#         vehicle.Mileage = Mileage
#         vehicle.RegistrationNumber = RegistrationNumber
#         vehicle.save()

#         return redirect("/")

#     # If GET request, fetch the current employee details
#     d = VehiclesDB.objects.get(Number=Number)
#     context = {
#         'd': d,
#         'number_error': None
#     }
#     return render(request, 'edit.html', context)

# def deleteData2(request, Number):
#     d=VehiclesDB.objects.get(Number=Number)
#     d.delete()
#     return redirect("/")



def deleteData(request, id):
    d=EmployeeDB.objects.get(id=id)
    d.delete()
    return redirect("/")



# def insertData(request):
#     if request.method=="POST":
#         Number=request.POST.get('Number')
#         ModelNumber=request.POST.get('Model Number')
#         ChasisNumber=request.POST.get('Chasis Number')
#         Mileage=request.POST.get('Mileage')
#         RegistrationNumber=request.POST.get('Registration Number')
#         print(Number,ModelNumber,ChasisNumber,Mileage,RegistrationNumber)

#     return render(request, "index.html")

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, "register.html", context)
  
def about(request):
    return render(request, "about.html")
