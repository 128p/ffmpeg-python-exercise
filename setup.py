from setuptools import setup

setup(
    name='tomp3',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'tomp3=tomp3:main'
        ]
    }
)
