from django.shortcuts import render, redirect
from user.forms import PolyabronForm
from user.models import Time, Polyabron
from datetime import timedelta
from django.http import JsonResponse
from django.utils import timezone

def list_polyabron(request):
    polyabrons = Polyabron.objects.filter(kun__gte=timezone.now().date())
    available_slots = Polyabron.get_available_slots()

    context = {
        'polyabrons': polyabrons,
        'available_slots': available_slots
    }

    return render(request, 'list.html', context=context)

def bosh_vaqtlar(request):
    available_slots = Polyabron.get_available_slots()

    context = {
        'available_slots': available_slots
    }

    return render(request, 'bosh_vaqtlar.html', context=context)

def create_polyabron(request):
    if request.method == 'POST':
        form = PolyabronForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_polyabron')
    else:
        form = PolyabronForm()

    times = Time.objects.all()
    return render(request, 'bron.html', {'form': form, 'times': times})

def check_availability(request):
    kun = request.GET.get('kun')
    vaqti = request.GET.get('vaqti')

    is_taken = Polyabron.objects.filter(kun=kun, vaqti_id=vaqti).exists()

    return JsonResponse({'is_taken': is_taken})

