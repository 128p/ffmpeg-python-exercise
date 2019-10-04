from setuptools import setup

setup(
    name='tomp3',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'tomp3=tomp3:main'
        ]
    }
)
