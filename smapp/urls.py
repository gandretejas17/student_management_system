
from django.urls import path
from smapp import views

urlpatterns = [
    
    path('add/', views.add_student_view),
    path('list/', views.student_list),
    path('detail/<int:id>/', views.student_detail),
    path('update/<int:id>/', views.update_student),
    path('delete/<int:id>/', views.delete_student),
    path('register/', views.user_register_view)

    
]