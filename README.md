# python-project

Python project template using Poetry as package manager.

> A Python project folder is also a Python package, and the folder name is the package name. Currently this is `proj`. Rename the folder and package `name` in `pyproject.toml` if desired.

## Installation

Clone this template to your local folder, e.g. `my-proj`:

```bash
git clone https://github.com/kengz/python-project.git my-proj
cd my-proj
```

[Install Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for Python dependency management; then install this project and its dependencies:

```bash
# install poetry if not already
curl -sSL https://install.python-poetry.org | python -

# switch to the same Python version as the project
poetry env use 3.11
# install this project and its dependencies
poetry install
```

> Always activate env with `poetry shell` first, or prepend `poetry run` to any commands.

## Usage

### Development notebook

Use VSCode interactive Python with any script, e.g. [nb/dev.py](./nb/dev.py) by selecting the kernel in `./.venv` created by Poetry.

To install new dependencies, use `poetry add <package>`

### Main script

```bash
python proj/main.py
```

### Unit Test

Run unit test to ensure module is set up correctly.

```bash
pytest
```
