# website/views.py
from django.shortcuts import render


def homepage(request):
    return render(request, "website/homepage.html")


def about_us(request):
    return render(request, "website/about-us.html")


def admissions(request):
    return render(request, "website/admissions.html")


def contact_us(request):
    return render(request, "website/contact-us.html")


def curriculum(request):
    return render(request, "website/curriculum.html")


def news_and_events(request):
    return render(request, "website/news-and-events.html")


def parent_information(request):
    return render(request, "website/parent-information.html")


def policies(request):
    return render(request, "website/policies.html")


def school_life(request):
    return render(request, "website/school-life.html")
