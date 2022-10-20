# {{ cookiecutter.repo_name.lower().replace('_', ' ').replace('-', ' ').title() }}

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![code style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![imports isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)
[![formatter docformatter](https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter)
[![docstyle numpy](https://img.shields.io/badge/%20style-numpy-459db9.svg)](https://numpydoc.readthedocs.io/en/latest/format.html)
[![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

## Repo Structure

```
.
├── data
│  ├── external
│  ├── interim
│  ├── processed
│  └── raw
{%- if cookiecutter.has_documentation == 'yes' -%}
├── docs
{% endif %}
├── models
{%- if cookiecutter.use_jupyter == 'yes' -%}
├── notebooks
{% endif %}
{%- if cookiecutter.has_documentation == 'yes' -%}
├── references
{% endif %}
{%- if cookiecutter.use_jupyter == 'yes' -%}
├── report
│  └── figures
{% endif %}
├── src
│  └── {{ cookiecutter.package_name }}
│     ├── data
│     └── models
├── tests
├── .env.template
├── .gitignore
├── .pre-commit-config.yaml
{%- if cookiecutter.use_pyenv == 'yes' -%}
├── .python-version
{% endif %}
{%- if cookiecutter.license != 'No license' -%}
├── LICENSE
{% endif %}
├── pyproject.toml
└── README.md
```


* [`data`](./data) contains the data. **This folder might actually not be versioned if the data lies in some cloud storages**.
  * [`raw`](./data/raw) contains the raw data. Never change those directly!
  * [`external`](./data/external) contains the external data.
  * [`interim`](./data/interim) will contain the intermediate results of the data manipulation.
  * [`processed`](./data/processed) will contain the final data used for the models.
{%- if cookiecutter.has_documentation == 'yes' -%}
* [`docs`](./docs) contains the documentation.
{% endif %}
* [`models`](./models) contains the models.
{%- if cookiecutter.use_jupyter == 'yes' -%}
* [`notebooks`](./notebooks) contains the exploratory notebooks. 
{% endif %}
{%- if cookiecutter.has_documentation == 'yes' -%}
* [`references`](./references) contains references (e.g. for ML modelling).
{% endif %}
{%- if cookiecutter.use_jupyter == 'yes' -%}
* [`report`](./report) contains rendered notebooks.
  * [`figures`](./figures) might contains figures used in the references.
{% endif %}
* [`src`](./src) contains the source code: 
  * [`{{cookiecutter.__package_name}}`](./src/{{ cookiecutter.package_name }}) is the dedicated python package.
    * [`data`](./src/{{ cookiecutter.package_name }}/data) contains the data manipulation and loading functions.
    * [`models`](./src/{{ cookiecutter.package_name }}/models) has model training steps.
* [`tests`](./tests) will contain the tests run with `pytest`.
* [`.env.template`](./.env.template) is a template dotenv file to store secret variables. **Do not put that under version control!**
* [`.gitignore`](./.gitignore) contains commonly ignored Python files, generated with [`gitignore.io`](https://www.toptal.com/developers/gitignore).
* [`.pre-commit-config.yaml`](./.pre-commit-config.yaml) contains the specifics for running some pre-commit/continuous integration hooks, on both scripts and notebooks.
{%- if cookiecutter.use_pyenv == 'yes' -%}
* [`.python-version`](./.python-version) is used by `pyenv`.
{% endif %}
{%- if cookiecutter.license != 'No license' -%}
* [`LICENSE`](./LICENSE) is the project's license.
{% endif %}
* [`pyproject.toml`](./pyproject.toml) is the new `requirements.txt`. It contains information about the project and groups dependencies in production, optional and development. This `pyproject.toml` is set up to be used with `pdm` specifically, but it can be swiftly updated to be used with other dependency managers, e.g. `Poetry`.

## Setup

The setup is explained in greater detail in the paragraph below. To get up and running, do the following:

1. Install `pdm` globally in one of the following ways:

```bash
# with pip
pip install -U pdm

# with pipx
pipx install pdm
```

2. Execute the following command inside the project folder:

```bash
pdm install
```

3. Configure `pdm` for Your IDE. Since `pdm` is still not as widely supported as `pipenv` or `poetry`, but
   the [official documentation](https://pdm.fming.dev/#use-with-ide) explains how to configure them:
    1. For PyCharm specifically, you need
       to [mark as Sources Root](https://www.jetbrains.com/help/pycharm/configuring-project-structure.html#mark-dir-project-view)
       the `__pypackages__/{{ cookiecutter.python_version }}/lib` folder.
    2. As the project interpreter, you will need to select the same Python version specified in the `pyproject.toml`.
        * To support multiple Python versions on your machine, [`pyenv`](https://github.com/pyenv/pyenv) is recommended.

:warning: If you need to run command-line executables installed with `pdm`, such as `pytest` or `jupyter notebook`, you need to run `pdm run <command> <args>`. Also see the [official docs](https://pdm.fming.dev/latest/usage/scripts/)

<details>
   <summary><h3>Why `pdm`: The Other Dependency Managers</h3></summary>

There are a lot of Python dependency management tools - each with its own set of trade-offs. `conda` is painfully slow
and does not offer many of the capabilities that dependency managers display today - starting from the user
interface. [`mamba`](https://github.com/mamba-org/mamba) is a worthy replacement that can be installed in your
base `conda` environment. However, this does not solve problems such as cross-platform compatibility with Unix and
Windows OS. To ensure maximum compatibility, `pip` and virtualenv-based managers were chosen. Crucially, `conda` does
not support differentiation between production and development dependencies: tools such as `pytest` and `tox` will end
up in the same environment specification file - while they should be separated.

`poetry` does not suffer from these weaknesses, as it is production/build oriented. Yet, it was not considered as it
overly-uses upper version constraints (see [here](https://iscinumpy.dev/post/bound-version-constraints/)
and [here](https://iscinumpy.dev/post/poetry-versions/)) and, crucially, **does not plan to follow future PEP
standards**. [`pipenv`](https://github.com/pypa/pipenv) does not, but requires running a shell subprocess to work. `pdm`
is the latest addition in Python dependency management and it is developed independently by a member of PyPA, i.e. the
Python Packaging Authority. It is by far the most complete, albeit it lacks mainstream support that all the other
managers. `pipenv` and `pdm` support PEP standards and adopt the `pyproject.toml` file specification to ensure
deterministic builds.

</details>
