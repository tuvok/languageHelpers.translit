from setuptools import setup, find_packages

setup(
    name = 'languageHelpers.translit',
    version = '0.0.6',
    author = 'Krzysztof Borowczyk',
    author_email = 'krzysztof@bordev.pl',
    description = 'Transliteration wrapper using uconv(1)',
    license = 'GPL v3',
    packages = find_packages('languageHelpers'),
    package_dir = {'':'languageHelpers'}
    )
