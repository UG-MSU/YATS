from django.shortcuts import render
from django.http import HttpResponse
from main.models import contest, user
def add_contest(request):
    cnts = contest.Contest.all()
    cont = contest(name=str(len(cnts) + 1), description=str(len(cnts) + 1), password=1, creator=user.User.all()[0])
    cont.save()
    return HttpResponse(f"added contest{len(cnts) + 1}")

