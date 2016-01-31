from setuptools import setup

setup(
    name='chess',
    entry_points={
        'console_scripts':
            [
                'chess=chess.run:cmdline_game',
                'chess-demo=chess.run:random_game',
            ],
    },
)
