PROFILE = {
    'name': 'Ayomide Elijah Raji',
    'headline': 'Building software + hardware systems for real-world problems',
    'email': 'hello@example.com',
    'twitter_url': 'https://twitter.com/jah_3li',
    'twitter_handle': '@jah_3li',
    'github_url': 'https://github.com/jah3li',
    'github_label': 'github.com/jah3li',
    'linkedin_url': 'https://www.linkedin.com/in/jah3li/',
    'linkedin_label': 'linkedin.com/in/jah3li',
    'location': 'Available for remote and hybrid engineering roles',
    'availability': 'Open to backend, platform, IoT, and systems-focused opportunities',
}


def profile_context(request):
    return {
        'profile': PROFILE,
        'role_focus': [
            'Backend Engineer',
            'Django Developer',
            'Platform / Infrastructure Engineer',
            'IoT / Mechatronics Builder',
        ],
    }
