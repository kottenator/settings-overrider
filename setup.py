from setuptools import setup


setup(
    name='settings-overrider',
    version='1.0.0',
    description='Override Python dict contents with YAML file and/or environment variables',
    long_description=(
        'Originally created for Django settings but may be useful in other cases. '
        'Read more on `project\'s GitHub page '
        '<https://github.com/kottenator/settings-overrider>`_.'
    ),
    url='https://github.com/kottenator/settings-overrider',
    author='Rostyslav Bryzgunov',
    author_email='kottenator@gmail.com',
    license='MIT',
    py_modules=['settings_overrider'],
    install_requires=['PyYAML'],
    extras_require={
        'test': [
            'pytest',
            'pytest-cov'
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ]
)
