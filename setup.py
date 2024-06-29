from setuptools import setup, find_packages

setup(
    name="pdf-extract-pro",
    version="0.1.0",
    author="Suraj Shinde",
    description="Extract structured data from messy PDFs",
    url="https://github.com/surajshinde427/pdf-to-structure-converter",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.8",
    install_requires=[
        "pypdf>=3.0.0",
        "tabula-py>=2.0.0",
        "pandas>=1.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "pdfextract=pdfextract.cli:main",
        ],
    },
)
