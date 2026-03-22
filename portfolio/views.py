from django.shortcuts import render

from .models import Project

DEFAULT_PROJECTS = [
    {
        'title': 'Bike-Hailing App',
        'description': 'A Django-powered mobility platform designed for Nigeria with operations, dispatch, and deployment in mind.',
        'tech_stack': 'Django, SQLite, Tailwind CSS',
        'status': 'MVP',
    },
    {
        'title': 'Arduino Field Monitoring Node',
        'description': 'An embedded prototype for collecting sensor data from physical environments and surfacing usable telemetry.',
        'tech_stack': 'Arduino, Sensors, Embedded C',
        'status': 'In Progress',
    },
    {
        'title': 'Infrastructure Observability Toolkit',
        'description': 'A placeholder systems project focused on service visibility, network awareness, and operational simplicity.',
        'tech_stack': 'Python, Networking, Security',
        'status': 'Planning',
    },
]


def _project_cards():
    projects = list(Project.objects.all())
    if projects:
        return projects
    return DEFAULT_PROJECTS


def home(request):
    projects = _project_cards()
    featured_project = projects[0]
    context = {
        'featured_project': featured_project,
        'featured_count': len(projects),
    }
    return render(request, 'portfolio/home.html', context)


def projects(request):
    return render(request, 'portfolio/projects.html', {'projects': _project_cards()})


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    return render(request, 'portfolio/contact.html')
