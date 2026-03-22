from django.shortcuts import render

from .models import Project

DEFAULT_PROJECTS = [
    {
        'title': 'Bike-Hailing App',
        'description': 'A Django-powered mobility platform designed for Nigeria with dispatch clarity, rider operations, and deployment realities as first-class concerns.',
        'tech_stack': 'Django, SQLite, Tailwind CSS',
        'status': 'MVP',
        'repo_url': 'https://github.com/jah3li',
    },
    {
        'title': 'Arduino Field Monitoring Node',
        'description': 'An embedded sensing prototype for collecting physical-environment telemetry and turning raw measurements into actionable field signals.',
        'tech_stack': 'Arduino, Sensors, Embedded C',
        'status': 'In Progress',
        'repo_url': 'https://github.com/jah3li',
    },
    {
        'title': 'Infrastructure Observability Toolkit',
        'description': 'A systems-oriented placeholder project focused on service visibility, network awareness, and operational simplicity for growing software platforms.',
        'tech_stack': 'Python, Networking, Security',
        'status': 'Planning',
        'repo_url': 'https://github.com/jah3li',
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
