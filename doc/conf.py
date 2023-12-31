# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Example'
copyright = 'workshop participant'
author = 'workshop participant'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']
# extensions = [
#     "sphinx.ext.autodoc",
#     "sphinx.ext.mathjax",
#     "sphinx.ext.viewcode",
#     "sphinx.ext.autosummary",
#     "sphinx.ext.doctest",
#     "sphinx.ext.inheritance_diagram",
#     "sphinx_rtd_theme",
#     "sphinx.ext.autosectionlabel", 
#     "sphinx.ext.napoleon", 
#     "nbsphinx",
# ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
