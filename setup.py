from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Sorting and Recursion Package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/nelebogo/mypackage.git',
    author='Nelebogo Kgohlo',
    author_email='tebogokgohlo@gmail.com'
)
