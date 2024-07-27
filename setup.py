from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="favihunter",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "favihunter=favihunter.favihunter:main",
        ],
    },
    author="gnome",
    author_email="gnome@groomla.ke",
    description="A pipx-installable cli tool to get the favicons of a list of domains.",
    long_description="A pipx-installable cli tool to get the favicons of a list of domains. It uses the favicon of the domain to identify the domain.",
    license="MIT",
    keywords="favicon domain",
    url="https://github.com/gnomegl/favihunter-pipx",
    python_requires=">=3.6",
)
