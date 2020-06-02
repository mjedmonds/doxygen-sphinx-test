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
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('../src'))


# -- Project information -----------------------------------------------------

project = 'doxygen-test-cpp-python'
copyright = '2020, Mark Edmonds'
author = 'Mark Edmonds'


# -- General configuration ---------------------------------------------------


master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # there may be others here already, e.g. 'sphinx.ext.mathjax'
    'sphinx.ext.mathjax',
    'autoapi.extension',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'breathe',
    'exhale'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

breathe_projects = {
  "doxygen-test-cpp": "./doxyoutput/xml"
}

breathe_default_project = "doxygen-test-cpp"

breathe_implementation_filename_extensions = ['.c', '.cc', '.cpp']

breathe_default_members = ('members', 'private-members', 'undoc-members')

breathe_domain_by_extension = {
        "h" : "cpp",
        "hpp" : "cpp",
        "py": "py",
}

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder":     "./cpp_api",
    "rootFileName":          "cpp_api_root.rst",
    "rootFileTitle":         "C++ API Reference",
    "doxygenStripFromPath":  "..",
    # Suggested optional arguments
    "createTreeView":        True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin":    "INPUT = ../src/cpp/"
}

# Document Python Code
autoapi_type = 'python'
autoapi_dirs = ['../src/python/']
autoapi_file_pattern = "*.py"
autoapi_keep_files = True
autoapi_root = "py_api"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# [[[ begin theme marker ]]]
# The name of the Pygments (syntax highlighting) style to use.
# `sphinx` works very well with the RTD theme, but you can always change it
pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'

html_title = "Doxygen test: merging C++ and Python API references"
html_short_title = "Doxygen test"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


