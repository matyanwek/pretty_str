import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pretty_str",
    version="1",
    description="A python package to format strings for terminal output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matyanwek/pretty_str",
    author="Gal Zeira",
    author_email="gal_zeira@protonmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
)
