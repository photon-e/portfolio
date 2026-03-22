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
    'instagram_url': 'https://www.instagram.com/jah_3li/',
    'instagram_handle': '@jah_3li',
    'youtube_url': 'https://www.youtube.com/@jah3li',
    'youtube_label': '@jah3li',
    'twitch_url': 'https://www.twitch.tv/jah3li',
    'twitch_handle': 'twitch.tv/jah3li',
    'location': 'Available for remote and hybrid engineering roles',
    'availability': 'Open to backend, platform, IoT, and systems-focused opportunities',
}

SOCIAL_LINKS = [
    {'label': 'Email', 'url': 'mailto:hello@example.com', 'value': 'hello@example.com'},
    {'label': 'Twitter', 'url': 'https://twitter.com/jah_3li', 'value': '@jah_3li'},
    {'label': 'GitHub', 'url': 'https://github.com/jah3li', 'value': 'github.com/jah3li'},
    {'label': 'LinkedIn', 'url': 'https://www.linkedin.com/in/jah3li/', 'value': 'linkedin.com/in/jah3li'},
    {'label': 'Instagram', 'url': 'https://www.instagram.com/jah_3li/', 'value': '@jah_3li'},
    {'label': 'YouTube', 'url': 'https://www.youtube.com/@jah3li', 'value': '@jah3li'},
    {'label': 'Twitch', 'url': 'https://www.twitch.tv/jah3li', 'value': 'twitch.tv/jah3li'},
]


def profile_context(request):
    return {
        'profile': PROFILE,
        'social_links': SOCIAL_LINKS,
        'role_focus': [
            'Backend Engineer',
            'Django Developer',
            'Platform / Infrastructure Engineer',
            'IoT / Mechatronics Builder',
        ],
    }
