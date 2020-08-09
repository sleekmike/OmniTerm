#!/usr/bin/env python3
import sys
import os
from setuptools import setup, find_packages


def find_data(relpath, folder):
    dir_content = []
    path = os.path.join(relpath, folder)
    tree = [(dirname, filenames) for dirname, _, filenames in os.walk(path)
            if filenames]

    for root, files in tree:
        path = os.path.relpath(root, relpath)
        dir_content.extend(map(lambda x: os.path.join(path, x), files))

    return dir_content


def package_data(relpath, folders):
    all_files = []
    for folder in folders:
        all_files.extend(find_data(relpath, folder))

    return all_files


### Post install script to install Micro and Cointop
# from setuptools.command.develop import develop
# from setuptools.command.install import install
# from subprocess import check_call, STDOUT
# import stat

# class PostDevelopCommand(develop):
#     """Post-installation for development mode."""
#     def run(self):
#         develop.run(self)
#         #os.chmod('./pokemonterminal/Scripts/install_linux_requirements.sh', stat.S_IXOTH)
#         check_call(
#             './pokemonterminal/Scripts/install_linux_requirements.sh',
#             shell=True,
#             stderr=STDOUT,
#             text=True
#         )

# class PostInstallCommand(install):
#     """Post-installation for installation mode."""
#     def run(self):
#         install.run(self)
#         #os.chmod('./pokemonterminal/Scripts/install_linux_requirements.sh', stat.S_IXOTH)
#         check_call(
#             './pokemonterminal/Scripts/install_linux_requirements.sh',
#             shell=True,
#             stderr=STDOUT,
#             text=True
#         )



setup(
    name="OmniTerm",
    version="0.0.1", 

    description="No More Messing Around",
    long_description="""

Everything outside of /omniterm_addons/ is from the base project:
    https://github.com/LazoCoder/Pokemon-Terminal

- <command> : <description>
    <link>

- micro: The Text Editor you wish Nano was
    https://micro-editor.github.io/

- asciinema rec : Cast your terminal instantly:
    https://asciinema.org/

- wtf: Too many functions
    https://wtfutil.com/modules/

- glances: Uber system monitor
    https://github.com/nicolargo/glances

- ttrv: Reddit Terminal App
    https://github.com/tildeclub/ttrv

- cointop: CryptoCurrency Monitor
    https://cointop.sh/

- bigtime: Nice Clock + Timer funcs
    https://github.com/teegre/bigtime

- pokemon: change the Terminal Background or Desktop Wallpaper: 
    https://github.com/LazoCoder/Pokemon-Terminal

- flash: flash cards Anki style:  
    https://github.com/tallguyjenks/fla.sh

- nvhtop: htop style nvidia-smi monitor enhancement
    https://github.com/shunk031/nvhtop

Supports Windows Terminal, iTerm2, Terminology, Tilix and ConEmu.""",
    url="https://github.com/kodiakcrypto/OmniTerm",

    author="Kodiak & SleekMike",
    author_email="cryptotradelogic@gmail.com",
    author_email="mikeohanu@icloud.com",

    license="GPLv3",

    packages=find_packages(exclude=['tests']),

    package_data={
        "pokemonterminal": package_data("pokemonterminal", ["Data", "Images", "Scripts", "omniterm_addons"]),
    },

    entry_points = {
        'console_scripts': [
            'pokemon = pokemonterminal.main:main',
            'ichooseyou = pokemonterminal.main:main',
            
            # Hackathon Addon Commands
            'wtf = pokemonterminal.omniterm_addons.wtf.main:main', 
            'cointop = pokemonterminal.omniterm_addons.cointop.main:main',
            'bigtime = pokemonterminal.omniterm_addons.bigtime.main:main', 
            'flash = pokemonterminal.omniterm_addons.flash.main:main', 
            # 'cht = pokemonterminal.omniterm_addons.cheatsheet.main:main', #this returns HTML and not helpful hints
            # 'fuck = pokemonterminal.omniterm_addons.thefuck.main:main', # it isnt giving suggestions...
            # 'ppp = pokemonterminal.omniterm_addons.thefuck.main:main', # alias for fuck
        ],
    },
    # for the post isntall classes above
    # cmdclass={
    #     'develop': PostDevelopCommand,
    #     'install': PostInstallCommand,
    # },
    #scripts=['install_linux_requirements.sh'] if sys.platform in ['linux', 'linux2'] else ['install_mac_requirements.sh'] if sys.platform == 'darwin' else [],
    # cointop and micro need to auto install here
    keywords="terminal app layer",

    classifiers=[
        "Development Status :: Beta",

        "Intended Audience :: End Users/Desktop",
        "Environment :: Console",
        "Topic :: Utilities",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],

    python_requires=">=3.7",

    # These work (asciinema untested)
    install_requires=
    [
        'psutil' if sys.platform != 'win32' else '',
        'ttrv' if sys.platform != 'win32' else '',
        'asciinema' if sys.platform != 'win32' else '',
        'thefuck' if sys.platform != 'win32' else '',
        'nvhtop' if sys.platform != 'win32' else '',
        'glances[action,browser,cloud,cpuinfo,docker,export,folders,gpu,graph,raid,snmp,web,wifi]' if sys.platform != 'win32' else '',
    ]
)