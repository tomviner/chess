from setuptools import setup

setup(
    name='chess',
    entry_points={
        'console_scripts':
            ['chess.run:main'],
    },
)