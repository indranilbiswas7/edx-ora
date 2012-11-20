from django.conf.urls import patterns, url
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


# General
# Note that instructor grading is a temporary stub view
#------------------------------------------------------------
urlpatterns = patterns('controller.views',
    url(r'^login/$', 'log_in'),
    url(r'^logout/$', 'log_out'),
    url(r'^status/$', 'status'),
    url(r'^instructor_grading/$', 'instructor_grading'),
)

# Xqueue submission interface (xqueue pull script uses this)
#------------------------------------------------------------
urlpatterns += patterns('controller.xqueue_interface',
    url(r'^submit/$', 'submit'),
)

# Grader pull interface
#------------------------------------------------------------
urlpatterns += patterns('controller.grader_interface',
    url(r'^get_submission_ml/$', 'get_submission_ml'),
    url(r'^get_submission_instructor/$', 'get_submission_instructor'),
    url(r'^put_result/$', 'put_result'),
)