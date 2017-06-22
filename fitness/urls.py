from django.conf.urls import url

from fitness.views import home, single_workout

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^workout/(?P<workout_id>[0-9]+)$', single_workout, name='single_workout')
]