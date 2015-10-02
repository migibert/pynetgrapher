"""
Python net library
"""
from setuptools import find_packages, setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)
dependencies = [str(ir.req) for ir in install_reqs]

setup(
    name='pynetgrapher',
    version='0.1.0',
    url='https://github.com/migibert/pynetgrapher',
    license='MIT',
    author='Mikael Gibert',
    author_email='mikael.gibert@gmail.com',
    description='Python network graph generator',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'pynetgrapher = pynetgrapher.pynetgrapher:main',
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
