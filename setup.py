"""
lambdata-bjanota - A Collection of Data Science helper functions.
"""
import setuptools
REQUIRED = [
    "numpy",
    "pandas"
]
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
setuptools.setup(
    name="lambdata_jtsheppard",
    version="0.0.3",
    author="jtsheppard88",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/jtshepppard88/lambdata-jtsheppard",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_required=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)