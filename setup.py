from setuptools import setup, find_packages

setup(
    name='sh-ec-scrapers',
    setup_requires=['setuptools_scm'],
    packages=find_packages(),

    install_requires=[
        'numpy==1.11.0',
        'pandas==0.18.0',
        'docopt==0.6.2',
        'pyaml==15.6.3',
        'requests',
        'simplejson'],


    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['ipdb==0.8.1',
                'ipython==4.1.2',
                'ipykernel']
    },

    scripts=[
    ],

    include_package_data=True

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
