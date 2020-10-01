from django.urls import path
from .views import *

urlpatterns = [
    path('', project_index, name='project_index'),
    path('project<int:pk>', project_detail, name='project_detail'),
    path("<tech>/", project_tech, name="project_tech"),
]
