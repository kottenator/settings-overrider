import os

from settings_overrider import override


tests_dir = os.path.dirname(__file__)


def test_none(settings_dict):
    """
    Test ``override(d)`` - shouldn't change anything

    :param settings_dict: custom fixture - initial settings dict
    """
    override(settings_dict)

    assert settings_dict == {
        'DEBUG': True,
        'STATIC_ROOT': 'static',
        'STATIC_URL': '/static/'
    }


def test_yaml_path(settings_dict):
    """
    Test ``override(d, yaml='/path/to/settings.yaml')``

    :param settings_dict: custom fixture - initial settings dict
    """
    yaml_path = os.path.join(tests_dir, 'settings.yaml')
    override(settings_dict, yaml=yaml_path)

    assert settings_dict == {
        'DEBUG': False,
        'STATIC_ROOT': '/var/www/static/',
        'STATIC_URL': '/static/'
    }


def test_yaml_file(settings_dict):
    """
    Test ``override(d, yaml=yaml_file)``

    :param settings_dict: custom fixture - initial settings dict
    """
    yaml_path = os.path.join(tests_dir, 'settings.yaml')

    with open(yaml_path) as yaml_file:
        override(settings_dict, yaml=yaml_file)

    assert settings_dict == {
        'DEBUG': False,
        'STATIC_ROOT': '/var/www/static/',
        'STATIC_URL': '/static/'
    }


def test_env(monkeypatch, settings_dict):
    """
    Test ``override(d, env='PRJ_')``

    :param settings_dict: default fixture - patching modules and environments
    :param settings_dict: custom fixture - initial settings dict
    """
    monkeypatch.setenv('PRJ_DEBUG', 'False')
    monkeypatch.setenv(
        'PRJ_DATABASES',
        '{ default: { ENGINE: django.db.backends.sqlite3, NAME: prj.sqlite3 }}'
    )

    override(settings_dict, env='PRJ_')

    assert settings_dict == {
        'DEBUG': False,
        'STATIC_ROOT': 'static',
        'STATIC_URL': '/static/',
        'DATABASES': {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'prj.sqlite3'
            }
        }
    }


def test_yaml_path_with_env(monkeypatch, settings_dict):
    """
    Test ``override(d, yaml='/path/to/settings.yaml', env='PRJ_')``

    :param settings_dict: default fixture - patching modules and environments
    :param settings_dict: custom fixture - initial settings dict
    """
    monkeypatch.setenv('PRJ_DEBUG', 'True')
    monkeypatch.setenv('PRJ_STATIC_URL', 'http://example.com/static/')

    override(settings_dict, yaml=os.path.join(tests_dir, 'settings.yaml'), env='PRJ_')

    assert settings_dict == {
        'DEBUG': True,
        'STATIC_ROOT': '/var/www/static/',
        'STATIC_URL': 'http://example.com/static/'
    }
