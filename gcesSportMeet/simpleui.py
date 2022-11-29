SIMPLEUI_LOGO = 'https://i.ibb.co/1fQJd42/logo.png'
SIMPLEUI_STATIC_OFFLINE = True
SIMPLEUI_HOME_ACTION = False
SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_QUICK = True
SIMPLEUI_DEFAULT_THEME = 'e-green-pro.css'
SIMPLEUI_HOME_ICON = 'fa fa-user'
SIMPLEUI_DEFAULT_ICON = False
SIMPLEUI_LOADING = False
SIMPLEUI_ANALYSIS = False
SIMPLEUI_LOADING = True
SIMPLEUI_CONFIG = {
    'dynamic':
    True,
    'system_keep':
    False,
    'menus': [
        {
            'app':
            'auth',
            'icon':
            'fa fa-user',
            'name':
            'People',
            'models': [
                {
                    'name': 'Users',
                    'icon': 'fa fa-user',
                    'url': 'auth/user/'
                },
            ],
        },
        {
            'app':
            'sports',
            'icon':
            'fa fa-money-bill-alt',
            'name':
            'Core',
            'models': [
                {
                    'name': 'Student',
                    'icon': 'fa fa-money-bill-alt',
                    'url': 'core/student/'
                },
                {
                    'name': 'Batch',
                    'icon': 'fa fa-chart-bar',
                    'url': 'sports/batch/'
                },
                {
                    'name': 'Position',
                    'icon': 'fa fa-dollar-sign',
                    'url': 'sports/position/'
                },
                {
                    'name': 'Sports',
                    'icon': 'fa fa-dollar-sign',
                    'url': 'sports/sports/'
                },
                {
                    'name': 'Teams',
                    'icon': 'fa fa-dollar-sign',
                    'url': 'sports/team/'
                },
                {
                    'name': 'Players',
                    'icon': 'fa fa-dollar-sign',
                    'url': 'players/player/'
                },
            ]
        },
        
        
    ]
}