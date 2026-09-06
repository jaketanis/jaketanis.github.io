# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Jake Tanis'
copyright = 'Copyright &#169 Jake Tanis '
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'githubpages',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_theme_options = {
    'page_layout': 'default',
    'accent_color': 'green',
    'color_mode': 'light',
    'foot_socials': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/jaketanis',
            'icon': 'simple-icons:github',
        },
           
        {
            'name': 'LinkedIn',
            'url': 'https://www.linkedin.com/in/jacobtanis/',
            'icon': 'simple-icons:linkedin',
        }
    ],
}

html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_title = 'Jake Tanis'
html_title_favicon = '_static/favicon.png'