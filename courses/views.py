from django.shortcuts import render, get_object_or_404
from .models import Course, Category, CourseInfo, MyCourse
from django.contrib.auth.decorators import login_required
# Create your views here.

def course_list_view(request, id):
	#A VERY DYNAMIC VIEW
	#all the categories printed
	categories = Category.objects.all()

	#the One category to print
	category = Category.objects.get(pk=id)

	#Filter all the course for the category
	courses = Course.objects.filter(category=category)
	

	context = {'courses': courses, 'categories':categories, 'category':category}

	return render(request, "courses/courses.htm", context)

def course_detail_view(request, id):
	#Call all thee Categories
	categories = Category.objects.all()
	obj = get_object_or_404(Course, id=id)
	context = {
        "object": obj,
        'categories': categories
	}
	return render(request, "courses/course_detail.htm", context)


@login_required
def mycourse_view(request):
	courses = MyCourse.objects.filter(user_id=request.user.id)

	context = {"courses": courses}
	return render(request, 'courses/mycourses.htm', context)

def test_course_detail_view(request, id):
	#Call all thee Categories
	categories = Category.objects.all()
	obj = get_object_or_404(Course, id=id)
	context = {
        "course": obj,
        'categories': categories
	}

	return render(request, "courses/test_course_detail.htm", context)




