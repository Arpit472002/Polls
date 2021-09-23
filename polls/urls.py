from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('polls/',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/vote/',views.vote,name='vote'),

]
