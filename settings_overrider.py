import os

from yaml import safe_load as load_yaml


def override(settings, yaml=None, env=None):
    """
    :param dict settings: settings dict to be updated; usually it's ``globals()``
    :param yaml: path to YAML file
    :type yaml: str or FileIO
    :param str env: prefix for environment variables
    """
    if yaml is not None:
        if hasattr(yaml, 'read'):
            settings.update(load_yaml(yaml.read()))
        else:
            if os.path.exists(yaml):
                with open(yaml) as f:
                    settings.update(load_yaml(f.read()))

    if env is not None:
        for k, v in os.environ.items():
            if k.startswith(env):
                settings[k[len(env):]] = load_yaml(v)
