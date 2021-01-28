from django.shortcuts import render, redirect
from .models import TableReservation
from .forms import TableReservationForm
from django.core.mail import send_mail

# Create your views here.



def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def menu(request):
    return render(request, 'main/menu.html')

def table(request):
    error = ""
    if request.method == 'POST':
        form = TableReservationForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Столик забранирован',
                'Ваш столик № ' + str(form.cleaned_data.get("tableNumber")) + ' был успешно зарезервирован на ' + str(
                    form.cleaned_data.get('reservationTime')),
                'restoranprestij@gmail.com',
                [form.cleaned_data.get('email')],
                fail_silently=False,
            )
            return redirect('homePage')
        else:
            error = "Invalid form"
    form = TableReservationForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'main/table.html', context)
