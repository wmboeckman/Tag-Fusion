from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tag-fusion',
    version='0.0.1',
    description='An SEO Tag Generator.',
    long_description=readme,
    author='William Boeckman',
    author_email='wmboeckman@gmail.com',
    url='https://github.com/wmboeckman/Tag-Fusion',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    py_modules=['main'],
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        main=main:cli
    ''',
)