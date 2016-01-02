# settings-overrider

Override Python dict contents with YAML file and/or environment variables.

Originally created for Django settings but may be useful in other cases.

## Install

```sh
pip install settings-overrider
```

## Use

```py
# settings.py

from settings_overrider import override

...

# at the end of the file
override(globals(), ...)
```

Use YAML file path:

```py
override(globals(), yaml='/etc/project-settings.yaml')
```

Use YAML file:

```py
with open('/etc/project-settings.yaml') as f:
    override(globals(), yaml=f)
```

Use all environment variables with specified prefix:

```py
override(globals(), env='PRJ_')
```

Prefix will be omitted, i.e. `PRJ_DEBUG` variable will become `DEBUG` setting.

Variable content will be parsed as YAML.

You can combine YAML file and environment variables.

## Contribute and test

```sh
git clone https://github.com/kottenator/settings-overrider.git
cd settings-overrider
pip install -e '.[test]'
py.test
```
