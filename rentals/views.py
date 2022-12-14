from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Owner, Rental, Student
from .forms import OwnerForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q
# Create your views here.
@login_required(login_url="/accounts/login")
def home(request):
    return render(request, 'home.html')


@login_required(login_url="/accounts/login")
def hostel_owners(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        owners = Owner.objects.filter(Q(email__icontains=email))
    else:
        owners = Owner.objects.all()
    #if request.method == 'POST':
    #    email = request.POST.get('email')
    #    print(email)
    return render(request, 'rentals/owners.html', {"owners": owners})


def hostel_details(request, pk):
    hostel = Rental.objects.get(pk=pk)
    students = Student.objects.filter(rental=hostel)
    context = {
        'hostel': hostel,
        'students': students,
    }
    return render(request, "rentals/hostel_details.html", context)

class CreateOwner(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = "rentals/owner.html"

class UpdateOwner(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = "rentals/owner.html"

class OwnerDetails(DetailView):
    model = Owner
    template_name = "rentals/owner-details.html"
    

@login_required(login_url="/accounts/login")
def hostels(request):
    if request.method == "POST":
        search = request.POST.get('search')
        hostels = Rental.objects.filter(Q(name__icontains=search))
    else:
        hostels = Rental.objects.all()
    context = {
        "hostels": hostels
    }
    return render(request, 'rentals/hostels.html', context)


@login_required(login_url="/accounts/login")
def students(request):
    return render(request, 'rentals/students.html')
