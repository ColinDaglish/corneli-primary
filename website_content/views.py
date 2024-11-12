# website_content/views.py
from django.shortcuts import render, redirect


def redirect_homepage(request):
    return redirect("home/")


def homepage(request):
    return render(request, "website_content/homepage.html")


def about_us(request):
    return render(request, "website_content/about-us.html")


def admissions(request):
    return render(request, "website_content/admissions.html")


def contact_us(request):
    return render(request, "website_content/contact-us.html")


def curriculum(request):
    return render(request, "website_content/curriculum.html")


def news_and_events(request):
    return render(request, "website_content/news-and-events.html")


def parent_information(request):
    return render(request, "website_content/parent-information.html")


def policies(request):
    return render(request, "website_content/policies.html")


def school_life(request):
    return render(request, "website_content/school-life.html")
