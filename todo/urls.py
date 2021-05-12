from django.urls import path
from .views import task_list,task_detail


urlpatterns = [
    path('list/',task_list,name='task_list_and_add'),
    path('<int:id>/',task_detail,name='task_detail'),
]
