from django.urls import path
from . import views

urlpatterns = [
    path('bins/', views.bin_list, name='bin_list'),
    path('schedules/', views.schedule_list, name='schedule_list'),
    path('reports/', views.report_view, name='report_list'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('',views.home,name="home"),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('request/', views.waste_request, name='waste_request'),
    path('profile/', views.user_profile, name='user_profile'),
    path('colect-histry/',views.collection_history,name="collection_history"),
    path('wast-trend/',views.waste_trends,name="waste_trends"),
    path('create-report/', views.create_report_view, name='create_report'),
    path('signup/', views.registerForm, name='signup'),
    path('coming-feature/', views.feature_coming, name='feature'),
    path('res/', views.res, name='res'),
]