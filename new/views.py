from django.shortcuts import render, redirect
from .forms import *

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):

    if request.method == 'POST':
        form = UserLogin(request, request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            userobj = authenticate(request, username=uname, password=upass)
            print(userobj)
            if userobj is not None:
                login(request, userobj)
                return redirect('dashboard/')
    else:
        form = UserLogin()
        return render(request, 'login.html', {'form': form})


def view_logout(request):
    logout(request)
    return redirect('/')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'dashboard.html')


@login_required(login_url='/')
def addClient(request):

    if request.method == "POST":
        if 'save_client' in request.POST:
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Client sucessfully Created")
                return redirect('/addcompany/')
            else:
                messages.warning(request, "form is not Valid")
                return redirect('/addinvoice/')
    else:
        form = ClientForm()
        try:
            data = Company.objects.all()
            return render(request, 'addClient.html', {'form': form, "data": data})
        except Exception as e:

            print("Error in Retriving data", e)
            return render(request, 'addClient.html', {'form': form})


@login_required(login_url='/')
def addService(request):

    if request.method == "POST":
        if 'save_service' in request.POST:
            form = ServiceForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Service Details sucessfully added")
                return redirect('/dashboard/')
            else:
                messages.warning(request, "form is not Valid")
                return redirect('/addservice/')
    else:
        form = ServiceForm()
        try:
            data = Company.objects.all()
            return render(request, 'addService.html', {'form': form, "data": data})
        except Exception as e:
            print("Error in Retriving data", e)
            return render(request, 'addService.html', {'form': form})


@login_required(login_url='/')
def addCompany(request):

    if request.method == "POST":

        if 'save_company' in request.POST:
            form = CompanyForm(request.POST)
            if form.is_valid():
                print('Helobb')
                form.save()
                messages.success(
                    request, "Company Details sucessfully Added")
                print('faoi')
                return redirect('/addservice/')
            else:
                messages.warning(request, "form is not Valid")
                return redirect('/addcompany/')
    else:
        form = CompanyForm()
        try:
            data = Company.objects.all()
            return render(request, 'addCompany.html', {'form': form, "data": data})
        except Exception as e:
            print("Error in Retriving data", e)
            return render(request, 'addCompany.html', {'form': form})


@login_required(login_url='/')
def updatecompany(request, id):

    if request.method == "POST":
        obj = Company.objects.get(id=id)
        print(obj)
        fm = CompanyForm(request.POST, instance=obj)
        if fm.is_valid():
            fm.save()
            messages.success(
                request, "Company Details sucessfully Updated")
            return redirect('/addservice/')
        else:
            messages.warning(request, "Form is not valid")
            return redirect('dashboard/')
    else:
        obj = Company.objects.get(id=id)
        print(obj)
        fm = CompanyForm(request.POST, instance=obj)
        # print(fm)
        return render(request, 'updatecompany.html', {"form": fm})


@login_required(login_url='/')
def DeleteCompany(request, id):
    try:
        if request.method == "GET":

            obj = Company.objects.get(id=id).delete()
            print(obj)
            messages.warning(
                request, "Company Details sucessfully Deleted")
            return redirect('/dashboard/')
    except Exception as e:
        print(e)
        messages.warning(
            request, "Something Wrong")
    finally:
        return redirect('/addservice/',)


@login_required(login_url="/")
def ReviewInvoice(request):
    try:
        client_obj = Client.objects.all()
        return render(request, 'reviewInvoice.html', {"data": client_obj})
    except Exception as e:
        print("Something is Wrong", e)
        return redirect('/dashboard/')


@login_required(login_url="/")
def view(request, pk):

    
    client_obj = Client.objects.get(pk=pk)

    

    try:
        company_obj = Company.objects.get(client_id=pk)

    except Company.DoesNotExist:
        # print("Client Not Found",e)
        company_obj={'key':"val"}

    try:
        service_obj = Services.objects.get(client_id=pk)

    except Services.DoesNotExist:
        # print("Client Not Found",e)
        service_obj = {'key':"val"}

    return render(request, 'show.html', context={"client": client_obj, "company": company_obj, "services": service_obj})
