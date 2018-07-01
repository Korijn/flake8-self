from setuptools import setup

from version import __version__


setup(
    name='flake8-self',
    py_modules=['flake8_self'],
    version=__version__,
    description=open("README.md").readlines()[4],
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    keywords='private access self linting flake8',
    author='Korijn van Golen',
    author_email='korijn@gmail.com',
    url='http://github.com/korijn/flake8-self',
    license='Freely Distributable',
    zip_safe=False,
    entry_points={
        'flake8.extension': [
            'SLF001 = flake8_self:SelfLinter',
        ],
    },
    install_requires=["flake8"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Freely Distributable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
