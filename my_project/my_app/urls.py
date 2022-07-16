from django.urls import path,re_path
from . import views

app_name = "my_app"

urlpatterns =[
    path('',views.StudentListView.as_view(),name='list'),
    path('create/',views.StudentCreateView.as_view(),name='create'),
    re_path(r'^(?P<pk>\d+)/$',views.StudentDetailView.as_view(),name='student_detail'),
    re_path(r'^update/(?P<pk>\d+)/$',views.StudentUpdateView.as_view(),name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$',views.StudentDeleteView.as_view(),name='delete'),
]