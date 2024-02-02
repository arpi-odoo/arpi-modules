
{
    'name': 'Game Dev',
    'depends': [
        'base',
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',

        # Views
        'views/game_views.xml',
        'views/genre_views.xml',
        'views/menus.xml',

        # Data
        'data/game_dev.genre.csv',
    ],
}
