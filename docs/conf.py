"""Sphinx configuration."""
# pylint: disable=invalid-name
from pathlib import Path

def get_version():
    """Return current version."""
    with Path('../version').open('r', encoding='utf-8') as v_fh:
        f_version = v_fh.read()
    return f_version

# pylint: disable=redefined-builtin
copyright = '2016, Dave Shawley'
extensions = ['sphinx.ext.intersphinx', 'sphinxjsondomain',]
html_sidebars = {
    '**': ['about.html', 'navigation.html'], }
html_static_path = ['_static']
html_theme = 'alabaster'
html_theme_options = {
    'description': 'Describe JSON documents',
    'github_user': 'dave-shawley',
    'github_repo': 'sphinx-jsondomain',
    'extra_nav_links': {
        'Index': 'genindex.html'},
}
intersphinx_mapping = {'python': ('https://docs.python.org/3', None), }
master_doc = 'index'
needs_sphinx = '1.0'
project = 'sphinx-jsondomain'
release = get_version()
version = get_version()
