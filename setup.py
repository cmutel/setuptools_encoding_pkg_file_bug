from setuptools import setup
import io

setup(
    name='setuptools_encoding_pkg_file_bug',
    version="1",
    # packages=["bw2calc"],
    author="Chris Mutel",
    author_email="cmutel@gmail.com",
    license=io.open('LICENSE.txt', encoding='utf-8').read(),
    url="",
    long_description="Test case repository",
)
