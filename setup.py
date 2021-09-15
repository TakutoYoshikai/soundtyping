from setuptools import setup, find_packages

setup(
    name = 'soundtyping',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/soundtyping.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'This is a program to play sound when you are typing.',
    install_requires = ['setuptools', "playsound", "pyxhook"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "soundtyping = soundtyping.soundtyping:main",
        ]
    }
)
