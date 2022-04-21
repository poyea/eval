import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="expression-parse-eval",
    version="0.13.0",
    description="Mathematical expression calculator in Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/poyea/eval",
    author="John Law",
    author_email="johnlaw.po@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["eval"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "eval=eval.__main__:main",
        ]
    },
)
