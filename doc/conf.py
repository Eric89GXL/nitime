# -*- coding: utf-8 -*-
#
# nitime documentation build configuration file, created by
# sphinx-quickstart on Mon Jul 20 12:30:18 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import warnings

# Declare here the things that our documentation build will depend on here, so
# that if they are not present the build fails immediately rather than
# producing possibly obscure errors later on.

# Documentation dependency format: each dep is a pair of two entries, the first
# is a string that should be a valid (possibly dotted) package name, and the
# second a list (possibly empty) of names to import from that package.
doc_deps = [['networkx', []],
            ['mpl_toolkits.axes_grid',  ['make_axes_locatable'] ],
            ]

# Analyze the dependencies, and fail if  any is unmet, with a hopefully
# reasonable error
failed_deps = []
for package, parts in doc_deps:
    try:
        __import__(package, fromlist=parts)
    except ImportError:
        failed_deps.append([package, parts])

if failed_deps:
    print
    print "*** ERROR IN DOCUMENTATION BUILD ***"
    print "The documentation build is missing these dependencies:"
    for pak, parts in failed_deps:
        if parts:
            print "Package: %s, parts: %s" % (pak, parts)
        else:
            print "Package: %s" % pak

    raise RuntimeError('Unmet dependencies for documentation build')


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('sphinxext'))

#-----------------------------------------------------------------------------
# Error control in examples and plots
#-----------------------------------------------------------------------------
# We want by default our documentation to NOT build if any plot warnings are
# generated, so we turn PlotWarning into an error.  For now this requires using
# a patched version of the plot_directive, but we'll upstream this to matplotlib.
import plot_directive
# If you *really* want to disable these error checks to be able to finish a doc
# build, comment out the next line.  But please do NOT leave it uncommented in
# a committed file, so that the official build is always in the paranoid mode
# (where the warnings become errors).
warnings.simplefilter('error', plot_directive.PlotWarning)

# -- General configuration -----------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              #'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.pngmath',
              'numpydoc',
              'inheritance_diagram',
              'ipython_console_highlighting',
              'only_directives',
              'math_dollar', #Support for $x$ math

              # For now, we use our own patched plot directive, we'll revert
              # back to the official one once our changes are upstream.
              #'matplotlib.sphinxext.plot_directive',
              'plot_directive',
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'nitime'
copyright = u'2009, Neuroimaging in Python team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# We read the version info from the source file.
ver = {}
execfile('../nitime/version.py', ver)
# The short X.Y version.
version = '%s.%s' % (ver['_version_major'], ver['_version_minor'])
# The full version, including alpha/beta/rc tags.
release = ver['__version__']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d, %Y, %H:%M PDT'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Flag to show todo items in rendered output
todo_include_todos = True

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'sphinxdoc'

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'nitime.css'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# Content template for the index page.
html_index = 'index.html'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {'index': 'indexsidebar.html'}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {'index': 'index.html'}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'nitimedoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('documentation', 'nitime.tex', u'nitime Documentation',
   u'Neuroimaging in Python team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
