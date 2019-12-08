from django.shortcuts import render,get_object_or_404,redirect

from django.http import HttpResponse,HttpResponseRedirect
from map.models import Squirrel
from .forms import SquirrelForm
# Create your views here.
def home (request):
    sightings=Squirrel.objects.all()
    context={'sightings':sightings,} 
    return render(request,"sightings/home.html",context)

def stats(request):
    Total_Num=Squirrel.objects.all().count()
    Run=Squirrel.objects.filter(running=True).count()
    Chase=Squirrel.objects.filter(chasing=True).count()
    Climb=Squirrel.objects.filter(climbing=True).count()
    Eat=Squirrel.objects.filter(eating=True).count()
    context={'Run':Run,'Chase':Chase,'Climb':Climb,'Eat':Eat,'Total_Num':Total_Num,}
    return render(request,'sightings/stats.html',context)

def add(request):
    if request.method=="POST":
        form=SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sightings:home')
    else:
        form=SquirrelForm()

    context={'form':form}
    return render(request,'sightings/add.html',context)


def update(request, unique_squirrel_id):
    up_sighting = get_object_or_404(Squirrel, unique_squirrel_id=unique_squirrel_id)
    if request.method == "POST":
        form = SquirrelForm(request.POST, instance=up_sighting)
        if form.is_valid():
            form.save()
            return redirect('sightings')
    form = SquirrelForm(instance=up_sighting)
    return render(request, "sightings/update.html", {"form": form, "unique_squirrel_id":unique_squirrel_id})
