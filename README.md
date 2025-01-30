[![Tests](https://github.com/um-jglad/ckanext-um_biostat_theme/workflows/Tests/badge.svg?branch=main)](https://github.com/um-jglad/ckanext-um_biostat_theme/actions)

# ckanext-um_biostat_theme

This theme was created for the UM-Biostat Faculty CKAN instance. It mostly updates the featured image and changes colors to UM branded ones.

## Requirements

**TODO:** For example, you might want to mention here which versions of CKAN this
extension works with.

If your extension works across different versions you can add the following table:

Compatibility with core CKAN versions:

| CKAN version     | Compatible? |
| ---------------- | ----------- |
| 2.10 and earlier | not tested  |
| 2.11.1           | yes         |

## Installation

To install ckanext-um_biostat_theme:

1. Activate your CKAN virtual environment, for example:

   ```bash
        . /usr/lib/ckan/default/bin/activate
   ```

2. Clone the source and install it on the virtualenv

   ```bash
      git clone https://github.com/um-jglad/ckanext-um_biostat_theme.git
      cd ckanext-um_biostat_theme
      pip install -e .
      pip install -r requirements.txt
   ```

3. Add `um_biostat_theme` to the `ckan.plugins` setting in your CKAN

4. Restart CKAN.

## Config settings

None at present

## Developer installation

To install ckanext-um_biostat_theme for development, activate your CKAN virtualenv and
do:

```bash
    git clone https://github.com/um-jglad/ckanext-um_biostat_theme.git
    cd ckanext-um_biostat_theme
    pip install -e .
    pip install -r dev-requirements.txt
```

## Tests

To run the tests, do:

```bash
    pytest --ckan-ini=test.ini
```

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
