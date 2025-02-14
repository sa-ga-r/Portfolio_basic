from django.http import JsonResponse
from .models import Project

def home(request):
    data = {
        'name':'Sagar Bhalerao',
        'tagline' : 'Softwere Developer',
        'contact_links' : {
            'email':'sagar.bhalerao@yahoo.co.in',
            'github':'sa-ga-r/github.com'
        }
    }
    return JsonResponse(data)

def about(request):
    data = {
        'bio' : 'I am a passionate developer with knowledge of Python, Django, javascript and react.',
        'skills' : ["Python", "Django", "Javascript", "React"],
    }
    return JsonResponse(data)

def projects(request):
    projects = Project.objects.all().values("title", "description", "links")
    return JsonResponse(list(projects), safe=False)

def contacts(request):
    data = {
        'email' : 'sagar.bhalerao@yahoo.co.in',
        'socials' : {
            'twitter' : 'twitter.com/sagarbhalerao',
            'linkedin' : 'linkedin.com/sagarbhalerao',
        }
    }
    return JsonResponse(data)