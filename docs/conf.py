extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
source_suffix = ".rst"
master_doc = "index"
project = "BazaarBot"
year = "2024"
author = "Nathan Manville"
copyright = f"{year}, {author}"
version = release = "0.0.0"

pygments_style = "trac"
templates_path = ["."]
extlinks = {
    "issue": ("https://github.com/nsmanville/python-bazaarbot/issues/%s", "#%s"),
    "pr": ("https://github.com/nsmanville/python-bazaarbot/pull/%s", "PR #%s"),
}

html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_options = {
    "githuburl": "https://github.com/nsmanville/python-bazaarbot/",
}

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_short_title = f"{project}-{version}"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
