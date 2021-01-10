from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image,Location,Category

# Create your views here.

def homepage(request):
    image = Image.objects.all()
    locations = Location.get_locations()
    category = Category.objects.all()
    context = {'image':image, 'locations': locations, 'category':category}

    return render(request, 'homepage.html', context )

def location(request, location):
    images = Image.filter_by_location(location)
    locations = Location.get_locations()
    category = Category.objects.all()
    context = {'images':images, 'locations': locations, 'category':category}

    return render(request, 'location.html', context)

def search_image(request):
    locations = Location.get_locations()
    category1 = Category.objects.all()

    if 'searchimage' in request.GET and request.GET["searchimage"]:
        category = request.GET.get("searchimage")
        images = Image.search_by_category(category)
 
        return render(request, 'search.html', {"images":images, 'locations': locations, 'category1':category1})

    else:
        return render(request, 'search.html', {'locations': locations,'category1':category1})
