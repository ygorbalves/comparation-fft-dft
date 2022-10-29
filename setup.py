from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="fft_dft",
    version="0.0.1",
    author="Ygor",
    author_email="ygorbalves222@gmail.com",
    description="Fast Fourier Transform (FFT) and Discrete Fourier Transform (DFT) comparation",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ygorbalves/comparation-fft-dft.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
)
