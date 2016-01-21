from setuptools import setup, find_packages

# su anki PyPI yazilimi markdown desteklemiyor
with open('README.rst') as f:
    long_description = f.read()

with open('requirements/requirements.txt') as f:
    install_requires = [line.strip() for line in f.readlines()]

setup(
    name='hello',
    version='hello',
    description='A hello word application',
    long_description=long_description,
    author='Eric Idle',
    author_email='idle@gmail.com',
    url='https://github.com/berkerpeksag/hello',
    # eger "pip install hello" denildiginde testlerin de kurulmasini
    # istiyorsanız exclude=['tests'] kismini kaldirabilirsiniz
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    # tum listeyi https://pypi.python.org/pypi?%3Aaction=list_classifiers
    # adresinde bulabilirsiniz
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    # zorunlu değil
    keywords='ast, codegen, PEP8',
)
