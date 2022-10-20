# Opinionated `cookiecutter` Template for Python Data Science Projects

This [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template is a twin of [`cookiecutter-python`](https://github.com/baggiponte/cookiecutter-python) inspired by [`cookiecutter-data-science`](https://github.com/drivendata/cookiecutter-data-science).

This template revolves around:

* [`nvim`](https://github.com/neovim/neovim) as a coding environment.
* [`pyright`](https://github.com/microsoft/pyright) as your LSP.
* [`pdm`](https://github.com/pdm-project/pdm) as your package manager.
  * A venv as your Python interpreter.

<details>
  <summary>Other goodies</summary>

* [`pytest`](https://github.com/pytest-dev/pytest)
* [`pre-commit`](https://github.com/pre-commit/pre-commit) with:
  * [`black`](https://github.com/psf/black)
  * [`isort`](https://github.com/PyCQA/isort)
  * [`pyupgrade`](https://github.com/nbQA-dev/nbQA)
  * [`flake8`](https://github.com/PyCQA/flake8)
  * [`docformatter`](https://github.com/PyCQA/docformatter)
  * [`nbqa`](https://github.com/nbQA-dev/nbQA)
</details>

## How to use this template

<details>
    <summary>How to install <code>cookiecutter</code></summary>

`cookiecutter` can be installed in the following ways:

```bash
# with pipx
pipx install cookiecutter

# with pip
pip install --user cookiecutter

# with your package manager, e.g. brew for macOS
brew install cookiecutter
```
</details>

<details>
    <summary>How to use <code>cookiecutter</code></summary>

You might also want to check [these slides](https://baggiponte.github.io/pymi-cookiecutter/)!

The `cookiecutter` CLI requires the user to input the values for some "context" variables. These values will be used to replace specific bits of text (not only filenames, but also portion of text within the filenames themselves) out of the template.

Context variables are specified in a `cookiecutter.json` file; then, each variable can be put either as a filename or as a bit of text as follows: `{{cookiecutter.<myvariable>}}`.

Two more things:

* Inside the `{{ }}`, standard string methods can be used, too. You can either use `.` as a separator, but also a `|`:

```
{{ cookiecutter.<myvariable>.lower().replace(' ', '_') }}
{{ cookiecutter.<myvariable>|lower()|replace(' ', '_') }}
```

* Private variables can also be specified, by prepending `_` or `__` to their names. See [here](https://cookiecutter.readthedocs.io/en/2.0.2/advanced/private_variables.html) for more.

</details>
<br>
After the installation, you can simply use this template with `cookiecutter`'s command line interface (CLI):

```bash
cookiecutter gh:baggiponte/cookiecutter-datascience
```

## What's in this template?

```
.
├── data
│  ├── external
│  ├── interim
│  ├── processed
│  └── raw
├── docs
├── models
├── notebooks
├── references
├── report
│  └── figures
├── src
│  └── {{ cookiecutter.package_name }}
│     ├── data
│     └── models
├── tests
│  └── __init__.py
├── .env.template
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── LICENSE
├── pyproject.toml
└── README.md
```
