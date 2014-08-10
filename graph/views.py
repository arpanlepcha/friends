from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Profile
from utils import serialize, filter_user


def home(request):
    return render_to_response('home.html')


def friends(request, idx):
    friends_list = Profile.objects.get(pk=idx).friends.all().select_related()
    return HttpResponse(serialize(friends_list), mimetype='application/json')


def friends_of_friends(request, idx):
    friends_list = [friend.pk for friend in Profile.objects.get(pk=idx).friends.all().select_related()]
    excluded_list = friends_list[:] + [int(idx)]
    friends_of_friends_list = Profile.objects.filter(friends__in=friends_list).exclude(id__in=excluded_list).distinct()
    return HttpResponse(serialize(friends_of_friends_list), mimetype='application/json')


def recommendation(request, idx):
    friends_list = [friend.pk for friend in Profile.objects.get(pk=idx).friends.all().select_related()]
    excluded_list = friends_list[:] + [int(idx)]
    friends_of_friends_list = Profile.objects.filter(friends__in=friends_list).exclude(id__in=excluded_list)\
        .select_related().distinct()

    return HttpResponse(filter_user(friends_of_friends_list, friends_list), mimetype='application/json')
