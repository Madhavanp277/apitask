from django.urls import path
from .views import StudentListCreateView, StudentDetailView, StudentProfileDetailView, StudentProfileListCreateView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('profiles/', StudentProfileListCreateView.as_view(), name='student-profile-list-create'),
    path('profiles/<int:pk>/', StudentProfileDetailView.as_view()),
]