# onetoast

Python package boilerplate using a modern `pyproject.toml` setup.

## Quickstart

### 1) Install in editable mode

```bash
python -m pip install -e .[dev]
```

### 2) Run tests

```bash
pytest
```

### 3) Use the package

```python
from onetoast import hello

print(hello("pip"))
```

## Build distributables

```bash
python -m build
```

This creates artifacts in `dist/`:
- source distribution (`.tar.gz`)
- wheel (`.whl`)

## Publish to PyPI

```bash
python -m twine upload dist/*
```

Before publishing, update metadata in `pyproject.toml`:
- `project.name`
- `project.version`
- author and URLs
