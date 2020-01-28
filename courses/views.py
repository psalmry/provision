from django.shortcuts import render, get_object_or_404
from .models import Course, Categorie, Course_Locality
# Create your views here.

def course_list_view(request, id):
	#A VERY DYNAMIC VIEW
	#all the categories printed
	categories = Categorie.objects.all()

	#the One category to print
	category = Categorie.objects.get(pk=id)

	#Filter all the course for the category
	courses = Course.objects.filter(category=category)
	

	context = {'courses': courses, 'categories':categories, 'category':category}

	return render(request, "courses/courses.htm", context)

def course_detail_view(request, id):
	#Call all thee Categories
	categories = Categorie.objects.all()
	obj = get_object_or_404(Course, id=id)
	context = {
        "object": obj,
        'categories': categories
	}
	return render(request, "courses/course_detail.htm", context)

def test_course_detail_view(request):
	#Call all thee Categories
	obj = get_object_or_404(Course, id=23)
	
	context = {
        "object": obj,
	}

	return render(request, "courses/test_course_detail.htm", context)


