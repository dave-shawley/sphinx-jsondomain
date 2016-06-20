import alabaster


project = 'sphinx-jsondomain'
copyright = '2016, Dave Shawley'
release = '0.0'
version = '0.0.1'
needs_sphinx = '1.0'
extensions = [
    'sphinx.ext.intersphinx',
    'sphinxjsondomain',
]

master_doc = 'index'
html_theme = 'alabaster'
html_static_path = ['_static']
html_theme_path = [alabaster.get_path()]
html_sidebars = {
    '**': ['about.html',
           'navigation.html'],
}
html_theme_options = {
    'description': 'Describe JSON documents',
    'github_user': 'dave-shawley',
    'github_repo': 'sphinx-jsondomain',
    'extra_nav_links': {'Index': 'genindex.html'},
}
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
