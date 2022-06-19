from setuptools import setup, find_packages

setup(
    name='write-tight',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'wt = write_tight.scripts.main:wt',
        ],
    },
)
