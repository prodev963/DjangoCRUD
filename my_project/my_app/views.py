from django.views.generic import View, TemplateView, UpdateView,DeleteView,ListView,CreateView,DetailView
from . import models
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class StudentCreateView(CreateView):
    fields = 'name' , 'course','age','gender','phoneNumber'
    model = models.Student

class StudentListView(ListView):
    context_object_name = 'student_list'
    model = models.Student

class StudentDetailView(DetailView):
    context_object_name = 'student_detail'
    model = models.Student    
    template_name: str = 'my_app/student_detail.html'    

class StudentUpdateView(UpdateView):
    fields = ('name','age','course','phoneNumber')
    model = models.Student    

class StudentDeleteView(DeleteView):
    context_object_name = 'student'
    model = models.Student
    success_url = reverse_lazy("my_app:list")
