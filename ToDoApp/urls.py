from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView,CustomLoginView,RegisterPage,TaskReorder
from django.contrib.auth.views import LogoutView


urlpatterns=[
   path('Login/',CustomLoginView.as_view(),name='Login'),
   path('logout/',LogoutView.as_view(next_page='Login'),name='logout'),
   path('register/',RegisterPage.as_view(),name ='register'),
   path('', TaskList.as_view(), name ='all_tasks'), 
   path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
   path('task-create/', TaskCreate.as_view(),name='task-create'), 
   path('update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
   
   path('delete/<int:pk>/',DeleteView.as_view(), name='delete_task'),
   path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]    