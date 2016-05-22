# -*- coding:utf8 -*-
from __future__ import division, print_function, absolute_import
import os
import sys
import codecs
import re
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


here = os.path.abspath(os.path.dirname(__file__))
package_requires = [
    # 'errbot',
    'six',
]
test_requires = [
    'pytest',
    'pytest-pep8',
    'pytest-flakes',
    'pytest-cov',
    'freezegun',
]


def read_file(path):
    if os.path.exists(path):
        with codecs.open(path, encoding='utf-8') as fp:
            return fp.read()
    return ''


def find_version(path):
    try:
        version_file = read_file(path)
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
        if version_match:
            return version_match.group(1)
    except OSError:
        raise RuntimeError("Unable to find version string.")
    raise RuntimeError("Unable to find version string.")


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = [
            '--pep8',
            '--flakes',
            '--cov=errcron',
        ]

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='errcron',
    version=find_version('errcron/__init__.py'),
    url='https://github.com/attakei/errcron',
    description='Crontab implementation for Errbot',
    long_description=read_file(os.path.join(here, 'README.rst')),
    author='attakei',
    author_email='attakei@users.noreply.github.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Chat',
    ],
    keywords='errbot plugin crontab',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=package_requires,
    tests_require=test_requires,
    extras_require={'test': test_requires},
    cmdclass={
        'test': PyTest,
    },
    entry_points={
        'console_scripts': [
        ],
    }
)
