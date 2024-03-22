# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = 'Your Project Name'
author = 'Your Name'

# The full version, including alpha/beta/rc tags
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
}

latex_documents = [
    (master_doc, 'YourProject.tex', 'Your Project Documentation',
     'Your Name', 'manual'),
]

# -- Extension configuration -------------------------------------------------