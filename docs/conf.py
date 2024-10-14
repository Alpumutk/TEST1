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
import os
import sys
sys.path.insert(0, os.path.abspath('../maths'))


# -- Project information -----------------------------------------------------

project = 'VASP K-Point Visualizer Tool'
copyright = '2024, Alp Kurbay, Brian Robinson, Andre Schleife'
author = 'Alp Kurbay, Brian Robinson, Andre Schleife'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',         # Automatically document Python modules
    'sphinx.ext.viewcode',        # Add links to the source code
    'sphinx.ext.napoleon',        # Support for Google and NumPy style docstrings
    'sphinx.ext.intersphinx',     # Link to other Sphinx documentation
    'sphinx.ext.todo',            # Support for TODOs
    'sphinx.ext.imgconverter',     # Convert images during the build process
    'sphinx.ext.extlinks',        # Create links to external sites
    'sphinx.ext.mathjax',         # For rendering LaTeX math
    'sphinx.ext.githubpages',     # Enable GitHub Pages support
    'sphinx.ext.ifconfig',        # Conditional inclusion of content based on configuration
    'sphinx.ext.coverage',        # Generate coverage reports for your documentation
    'sphinx.ext.imgconverter',     # Convert images to other formats if needed
    'sphinx.ext.autosummary',     # Automatically generate summary tables for modules
    'sphinx.ext.todo',            # Include TODOs in the documentation
    'sphinx.ext.extlinks',        # Easily create links to external resources
    'sphinx.ext.graphviz',        # Add Graphviz support for creating diagrams
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
