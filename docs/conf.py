import alabaster
from sphinxcontrib import jsondomain


project = 'sphinx-jsondomain'
copyright = '2016, Dave Shawley'
release = '.'.join(str(v) for v in jsondomain.version_info[:2])
version = jsondomain.__version__
needs_sphinx = '1.0'
extensions = [
    'sphinx.ext.intersphinx',
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
}
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
