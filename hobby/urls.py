from django.urls import path
from .import views


app_name = 'hobby'
# urlを記載
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('option/', views.OptionView.as_view(), name='option'),
    path('question/', views.QuestionView.as_view(), name='question'),
    path('results/', views.ResultsView.as_view(), name='results'),
]