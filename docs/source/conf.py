# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '카지노사이트'
copyright = '카지노사이트 국내 최고의 자본과 보안을 자랑하는 카지노검증사이트 안내'
author = '카지노컴퍼니'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    '카지노사이트': ('https://projectfluent.io/', None),
    '바카라사이트': ('https://projectfluent.io/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
