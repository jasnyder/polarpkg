import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="polaritymodel-jasnyder",
    version="0.0.1",
    author="Jordan Snyder",
    author_email="snydrew@gmail.com",
    description="A package for running the cell polarity model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jasnyder/polarpkg",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=[
        'torch',
        'torchaudio',
        'torchvision',
        'pickle',
        'numpy',
        'scipy',
        'plotly',
        'pandas'
    ],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)