from setuptools import setup

import sdist_upip

setup(
    name="umock",
    version="0.0.1",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xsteadfastx/umock",
    author="Marvin Preuss",
    author_email="marvin@xsteadfastx.org",
    license="MIT",
    cmdclass={"sdist": sdist_upip.sdist},
    package_dir={"": "src"},
    packages=["umock"],
)
