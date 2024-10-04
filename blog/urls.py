from django.contrib import admin
from django.urls import path
from blog import views 

app_name = "blog"
urlpatterns=[
    path("", views.index, name = "index"),
    # path("about/", views.about, name = "about"),
    path("factors/", views.factors, name = "factors"),
    path("method/", views.method, name = "method"),
    path("how/", views.how, name = "how"),
    path("references/", views.references, name = "references"),
    path("env/", views.env, name = "env"),
    
    # path("factors/ages", views.ages, name = "ages"),
    path("factors/group", views.group, name = "group"),
    path("factors/metropolitan", views.metropolitan, name = "metropolitan"),
    path("factors/single", views.single, name = "single"),
    path("factors/spouse", views.spouse, name = "spouse"),

    path("factors/job", views.job, name = "job"),
    path("factors/place", views.place, name = "place"),

    # path('chart/', views.year_show_chart, name='show_chart'),
    # 차트 삽입 about
    path('about/', views.year_chart_about, name='about'),
    # 차트 삽입 factors/ages
    path('factors/ages/', views.factors_age_chart, name='ages'),
] 

