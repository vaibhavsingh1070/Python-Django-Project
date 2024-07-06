from django.shortcuts import get_object_or_404, redirect, render
from .models import Studentdb
from django.contrib import messages

# Create your views here.

def index(request):
    data=Studentdb.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def create(request):
    return render(request,"create.html")

def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age  = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        print(name ,age , email , phone , address)
        query=Studentdb(name=name,age=age,email=email,phone=phone,address=address)
        query.save()
        messages.info(request,"Data Inserted successfully")
        return redirect('index')  # Redirect after successful form submission
    return render(request,"create.html")

# def update(request, id):
#     #This is to update the data inside update form
#     if request.method == "POST":
#         name = request.POST.get('name')
#         age  = request.POST.get('age')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         #here instead of updating the it is creating a new data

#         edit=Studentdb.objects.get(id=id)
#         edit.name = name
#         edit.age = age
#         edit.email = email
#         edit.phone = phone
#         edit.address = address
#         edit.save()
#         messages.warning(request,"Data Upadated successfully")
#         return redirect("index")#here index function is called
    
#     #This is only to display the update form      
#     d=Studentdb.objects.get(id=id)
#     context={"d":d}
#     return render(request,"update.html",context)

def delete(request, id):
    d=Studentdb.objects.get(id=id) #gets particular id 
    d.delete()
    messages.error(request,"Data Deleted successfully")
    return redirect("index")

def updatepage(request):
    if request.method == "POST":
        user_id = request.POST.get('userId')

        try:
            student = Studentdb.objects.get(id=user_id)
            return redirect('update', id=student.id)
        except Studentdb.DoesNotExist:
            messages.error(request, "User ID not found")
            return redirect('updatepage')

    return render(request,"update_page.html")


def update(request, id):

   # Fetch the existing student data based on the ID
    student = get_object_or_404(Studentdb, id=id)

    if request.method == "POST":
        # Get the updated data from the form
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Update the student object with the new data
        student.name = name
        student.age = age
        student.email = email
        student.phone = phone
        student.address = address
        student.save()

        messages.success(request, "Data updated successfully")
        return redirect("index")  # Redirect to the index view

    # If the request method is GET, display the update form with pre-filled data
    context = {"student": student}
    return render(request, "update.html", context)

def deletepage(request):
    if request.method == "POST":
        user_id = request.POST.get('userId')

        try:
            student = Studentdb.objects.get(id=user_id)
            return redirect('deleteview', id=student.id)
        except Studentdb.DoesNotExist:
            messages.error(request, "User ID not found")
            return redirect('deletepage')

    return render(request,"delete_page.html")

def deleteview(request,id):
    # Fetch the existing student data based on the email
    student = get_object_or_404(Studentdb, id=id)

    context = {"student": student}
    return render(request, "delete.html", context)

def test(request):
    return render(request,"test.html")