from setuptools import setup, find_packages

setup(
    name="outlier-detector",
    version="0.1.0",
    description="A Python library for detecting outliers using IQR and Z-score methods.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Naeem Ahmed Booher",
    author_email="naeemahmedbdn2002@gmail.com",
    url="https://github.com/naeemahmed02/outlier-detector",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
