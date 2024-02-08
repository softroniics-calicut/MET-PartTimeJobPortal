"""parttimejob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobportal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about',views.about),
    path('service',views.service),
    path('trainer',views.trainer),

    path('std_register', views.std_register),
    path('stdedit', views.stdedit),
    path('stdview',views.stdview),
    path('stdhome',views.stdhome,name='stdhome'),
    path('stdreview',views.stdreview,name='stdreview'),

    path('jobview',views.jobview,name='jobview'),
    path('jobsearch',views.jobsearch,name="jobsearch"),
    path('job_applications/<int:jid>',views.job_applications,name="job_applications"),
    path('job_applied/<int:jobid>',views.job_applied,name="job_applied"),

    path('agency_register', views.agency_register),
    path('agencyhome',views.agencyhome),
    path('agencyedit', views.agencyedit),
    path('agencyview', views.agencyview),

    path('aslogin', views.aslogin, name="aslogin"),
    path('aslogout',views.aslogout,name='aslogout'),

    path('addjob',views.addjob,name='addjob'),
    path('editjob/<int:jobid>',views.editjob,name="editjob"),
    path('delete/<int:jobid>',views.delete,name="delete"),
    path('jobaview',views.jobaview),
    path('history',views.history,name='history'),

    path('applicationrequest/<int:id>',views.applicationrequest,name="applicationrequest"),
    path('requestview',views.requestview,name="requestview"),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)