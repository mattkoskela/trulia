try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="trulia",
    version="0.0.3",
    author="Matt Koskela",
    author_email="mattkoskela@gmail.com",
    packages=["trulia"],
    url="https://github.com/mattkoskela/trulia",
    license="LICENSE",
    description="Python library for accessing trulia.com's REST API",
    long_description=open("README.md").read(),
    install_requires=[
        "requests==2.3.0",
        "xmltodict==0.9.0"
    ]
)
