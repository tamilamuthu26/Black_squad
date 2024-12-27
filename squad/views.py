from django.shortcuts import render
from .models import SquadMember
from squad import views


def home(request):
    members = SquadMember.objects.all()
    return render(request, 'home.html', {'members': members})

def member_detail(request, pk):
    member = SquadMember.objects.get(pk=pk)
    return render(request, 'member_detail.html', {'member': member})
