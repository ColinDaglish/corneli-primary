# website_content/urls.py
from django.urls import path
from website_content import views

urlpatterns = [
    path("about/", views.about_us, name="about-us"),
    path("admissions/", views.admissions, name="admissions"),
    path("contact-us/", views.contact_us, name="contact-us"),
    path("curriculum/", views.curriculum, name="curriculum"),
    path("", views.redirect_homepage, name="redirect-home"),
    path("home/", views.homepage, name="home"),
    path("news-and-events/", views.news_and_events, name="news-and-events"),
    path(
        "parent-information/",
        views.parent_information,
        name="parent-information",
    ),
    path("policies/", views.policies, name="policies"),
    path("school-life/", views.school_life, name="school-life"),
]
