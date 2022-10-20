#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.license }}" == "No license":
        remove_file("LICENSE")

    if "{{ cookiecutter.use_pyenv }}" != "yes":
        remove_file(".python-version")

    if "{{ cookiecutter.has_documentation }}" != "yes":
        remove_dir("docs")
        remove_dir("references")

    if "{{ cookiecutter.use_jupyter }}" != "yes":
        remove_dir("notebooks")
        remove_dir("report")
