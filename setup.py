# setup.py

from setuptools import setup, find_packages

setup(
    name='encryption',
    version='1.0.0',
    description='A Python package to encrypt and decrypt config.json files to preserve  sensitive information.',
    author='Shabir Ahmad',
    author_email='shabir@caimy.co.kr',
    packages=find_packages(),
    install_requires=[
        'cryptography'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
