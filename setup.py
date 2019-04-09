from setuptools import setup

with open("README.md", "r") as f:
    long_desc = f.read()

setup(
    name="django-whiteless",
    version="0.1.0",
    packages=["whiteless"],
    url="https://github.com/denizdogan/django-whiteless",
    license="Apache-2.0",
    author="Deniz Dogan",
    author_email="denizdogan@noreply.users.github.com",
    description="Django template utilities for handling whitespaces",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    install_requires=["Django >= 1.11"],
    tests_require=[
        "hypothesis == 4.14.3",
        "pytest == 4.4.0",
        "pytest-cov == 2.6.1",
        "pytest-django == 3.4.8",
        "pytest-runner == 4.4",
    ],
    extras_require={
        "dev": [
            "black == 19.3b0",
            "flake8 == 3.7.7",
            "flake8-isort == 2.7.0",
            "isort == 4.3.16",
            "markdown-include == 0.5.1",
            "mkdocs == 1.0.4",
            "mkdocs-minify-plugin == 0.1.0",
            "pipdeptree == 0.13.2",
            "pre-commit == 1.15.1",
            "pygments == 2.3.1",
        ]
    },
)
