import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tqdmX", # Replace with your own username
    version="0.0.2",
    author="KimythAnly",
    author_email="kimythanly@gmail.com",
    description="A tqdm wrapper for multi-line logging.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kimythanly/tqdmX",
    packages=setuptools.find_packages(),
    install_requires=[
        'tqdm',
        'addict'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)