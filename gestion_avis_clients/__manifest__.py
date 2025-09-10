{
    'name': 'Gestion des avis clients',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Module de gestion des avis clients pour les produits',
    'description': """
        Ce module permet aux clients de laisser des avis sur les produits qu\'ils ont achetés.
        Les avis peuvent être modérés par les administrateurs avant publication.
    """,
    'author': 'Votre Nom ou Entreprise',
    'website': 'http://www.votre-site.com',
    'depends': ['base', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_review_views.xml',
        'views/menu_views.xml',
        
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}