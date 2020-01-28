from django.shortcuts import render, get_object_or_404
from webinars.models import Webinar

def webinar(request, *args, **kwargs):
	return render(request, 'webinars/webinar.htm', {})

def webinar_list_view(request):
	webinars = Webinar.objects.all()
	context = {'webinars': webinars}
	return render(request, "webinars/webinars.htm", context)

def webinar_detail_view(request,id):
	webinar = get_object_or_404(Webinar, id=id)
	context = {'webinar':webinar}
	return render(request, "webinars/webinar_detail.htm", context)

