# Poetry Chuy Plugin

![CodeQL](https://github.com/UltiRequiem/poetry-chuy-plugin/workflows/CodeQL/badge.svg)
![PyTest](https://github.com/UltiRequiem/poetry-chuy-plugin/workflows/PyTest/badge.svg)
![Pylint](https://github.com/UltiRequiem/poetry-chuy-plugin/workflows/Pylint/badge.svg)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/poetry-chuy-plugin)](https://pypi.org/project/poetry-chuy-plugin)
![Repo Size](https://img.shields.io/github/repo-size/ultirequiem/poetry-chuy-plugin?style=flat-square&label=Repo)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Lines of Code](https://img.shields.io/tokei/lines/github.com/UltiRequiem/poetry-chuy-plugin?color=blue&label=Total%20Lines)

This plugin integrates [Chuy](https://github.com/UltiRequiem/chuy) with
[Poetry](https://github.com/python-poetry/poetry).

_Note_: This only works in Poetry 1.2.0 or superior.

## Installation

From your terminal:

```bash
poetry plugin add poetry-chuy-plugin
```

## Configuration

In your `pyproject.toml`:

```toml
[tool.chuy]
format = "poetry run black ."
lint = "poetry run pylint chuy tests"
tests = "poetry run pytest"
package = "poetry build && poetry publish"
```

## Usage

```bash
poetry chuy tests
```

Or pass multiple arguments:

```bash
poetry chuy tests lint
```

See [Chuy](https://github.com/UltiRequiem/chuy) for all the options.

### License

This project is licensed under the [MIT License](https://github.com/UltiRequiem/poetry-chuy-plugin/blob/main/LICENSE).
