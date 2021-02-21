# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Rajat Sethi"
copyright = "2021 - Rajat Sethi"
author = "Rajat Sethi"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "ablog",
    "sphinx_panels",
    "sphinxcontrib.bibtex",
    "myst_nb",
    # "sphinxext.opengraph",
]

autosummary_generate = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "*import_posts*", "**/pandoc_ipynb/inputs/*"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'pydata_sphinx_theme'
# html_logo = "_static/pandas.svg"

html_theme_options = {
    "github_url": "https://github.com/therajatsethi",
    "twitter_url": "https://twitter.com/therajatsethi",
    "search_bar_text": "Search this site...",
    "google_analytics_id": "G-EKRVF1S5Y8",
    "search_bar_position": "navbar",
     "show_prev_next": False
}

html_favicon = "_static/favicon.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_extra_path = ["feed.xml"]

html_sidebars = {
    "index": ["hello.html"],
    "articles/*" : ['globaltoc.html', 'recentposts.html'],
    "articles/data-science/**" : ['globaltoc.html', 'recentposts.html'],
    "articles/python/**" : ['globaltoc.html', 'recentposts.html'],
    "blog/**": ['postcard.html', 'recentposts.html', 'archives.html'],
    "blog": ['tagcloud.html', 'archives.html'],
}

blog_baseurl = "https://sethirajat.com"
blog_title = "Rajat Sethi"
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "blog/*/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2
disqus_shortname = "sethirajat"

# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_admonition_enable = True
myst_deflist_enable = True

# OpenGraph config
# ogp_site_url = "https://predictablynoisy.com"
# ogp_image = "https://predictablynoisy.com/_static/profile-bw.png"

# Temporarily stored as off until we fix it
jupyter_execute_notebooks = "off"

def setup(app):
    app.add_css_file("custom.css")


# Pygment style
pygments_style = 'friendly'


html_show_sphinx = False