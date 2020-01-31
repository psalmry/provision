
from django.contrib import admin
from django.urls import path
from pages.views import *
from provison_users.views import login_view, signup_view, logout_view
from courses.views import course_list_view, course_detail_view, test_course_detail_view, mycourse_view
from webinars.views import webinar, webinar_list_view, webinar_detail_view
from django.conf import settings 
from django.conf.urls.static import static 
from provison_users.views import activation_sent_view, activate, profile_view


urlpatterns = [
	#Main pages
    path('admin/', admin.site.urls),
    path('', home, name ='home' ),

    #User Auth
    path('accounts/login/', login_view, name="login_view"),
    path('accounts/signup/', signup_view, name="signup_view"),
    path('accounts/logout/', logout_view, name="logout_view"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),


    #User Profile
    path('profile/', profile_view, name="profile_view"),

    #Webinars
    path('webinar/', webinar ),#fromPages
    path('webinars/',webinar_list_view),
    path('<int:id>/webinar/',webinar_detail_view),

    path('<int:id>/category', course_list_view),
    path('<int:id>/course', course_detail_view, name='course_detail'),
    path('test', test_course_detail_view, name='test_course_detail'),
    path('your-courses/', mycourse_view, name='mycourse_view'),
    

    #Services Pages
    path('blended-learning', service_blended_learning ),
    path('consultancy-services', consultancy_services ),
    path('e-learning-solutions', e_learning_solutions ),
    path('empowerment-leadership-program-elp', empowerment_leadership_program_elp ),
    path('engineering-management-consulting', engineering_management_consulting ),
    path('executive-coaching', executive_coaching ),
    path('in-house-courses', in_house_courses ),
    path('individual-training-program-itp', individual_training_program_itp ),
    path('intelligent-leader-program-ilp5', intelligent_leader_program_ilp5 ),
    path('iso-robot', iso_robot ),
    path('outsourcing-solutions', outsourcing_solutions ),
    path('talent-tool', talent_tool ),
    path('testing-examination-center', testing_examination_center ),

    #About Us
	path('aboutus', aboutus ),
	path('accreditations', accreditations ),
	path('clients', clients ),
	path('contactus', conatctus ),
	path('instructors', instructors ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)