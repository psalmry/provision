from django.shortcuts import render
from courses.models import Course
#main pages

#my changes

def home(request):
    #courses = Course.objects.filter(date__year='2020')
    courses = Course.objects.all()
    context = {'courses': courses}
    
    print('I was here very well')
    return render(request, 'home.htm', context)

#Services
def service_blended_learning(request, *args, **kwargs):
	return render(request, 'Services/blended_learning.htm', {})

def consultancy_services(request, *args, **kwargs):
	return render(request, 'Services/consultancy-services.htm', {})

def e_learning_solutions(request, *args, **kwargs):
	return render(request, 'Services/e-learning-solutions.htm', {})

def empowerment_leadership_program_elp(request, *args, **kwargs):
	return render(request, 'Services/empowerment-leadership-program-elp.htm', {})

def engineering_management_consulting(request, *args, **kwargs):
	return render(request, 'Services/engineering-management-consulting.htm', {})

def executive_coaching(request, *args, **kwargs):
	return render(request, 'Services/executive-coaching.htm', {})

def in_house_courses(request, *args, **kwargs):
	return render(request, 'Services/in-house-courses.htm', {})

def individual_training_program_itp(request, *args, **kwargs):
	return render(request, 'Services/individual-training-program-itp.htm', {})

def intelligent_leader_program_ilp5(request, *args, **kwargs):
	return render(request, 'Services/intelligent-leader-program-ilp5.htm', {})

def iso_robot(request, *args, **kwargs):
	return render(request, 'Services/iso-robot.htm', {})

def outsourcing_solutions(request, *args, **kwargs):
	return render(request, 'Services/outsourcing-solutions.htm', {})

def talent_tool(request, *args, **kwargs):
	return render(request, 'Services/talent-tool.htm', {})

def testing_examination_center(request, *args, **kwargs):
	return render(request, 'Services/testing-examination-center.htm', {})

#Aboutus
def aboutus(request, *args, **kwargs):
	return render(request, 'about/aboutus.htm', {})

def accreditations(request, *args, **kwargs):
	return render(request, 'about/accreditations.htm', {})

def clients(request, *args, **kwargs):
	return render(request, 'about/clients.htm', {})

def conatctus(request, *args, **kwargs):
	return render(request, 'about/contactus.htm', {})

def instructors(request, *args, **kwargs):
	return render(request, 'about/instructors.htm', {})






	
	
