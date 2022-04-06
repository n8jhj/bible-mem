# pyproject-template

A template for my Python projects

# Testing

## pytest

The pytest documentation discusses two alternatives for test layouts. The test layout strategy chosen for this repository is ["Tests outside application code"](https://docs.pytest.org/en/6.2.x/goodpractices.html#tests-outside-application-code), with the presence of `__init__.py` files. I would like to do without the need for these files in the `test` directory, but having them allows VSCode Python Testing to work (i.e. I couldn't figure out how to get VSCode to use `python -m pytest` instead of just `pytest`).

## pytest-cov

As demonstrated in [this example](https://github.com/ryanluker/vscode-coverage-gutters/tree/94abefc02fe0df1505ca6d5a33e65bc2b949a507/example/python), use:

`poetry run pytest --cov . --cov-report xml:cov.xml`

See also: https://stackoverflow.com/a/60394674/7232335

## Coverage Gutters

The Coverage Gutters VSCode extension is the tool of choice for displaying coverage within the editor.

### Keyboard shortcuts
* `Ctrl+Shift+8` to turn on coverage watch
* `Ctrl+Shift+9` to turn it off

### VSCode settings
`"coverage-gutters.showLineCoverage": false,`
