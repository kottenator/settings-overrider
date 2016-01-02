import pytest


@pytest.fixture
def settings_dict():
    """
    Initial settings dict
    """
    return {
        'DEBUG': True,
        'STATIC_ROOT': 'static',
        'STATIC_URL': '/static/'
    }
