""" Sets up Unlimited Google Translate API """
from setuptools import setup, find_packages

VERSION = '0.1.01'

setup(
    name='klarna_test_api',
    version=VERSION,
    description='Klarna test Api',
    long_description='Klarna Test providing web services to a given tasks/methods',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
    keywords='oak klarna test api',
    author='Omer Ahmed Khan',
    author_email='omerahmed122@gmail.com',
    url='',
    license='',
    packages=find_packages(),
    install_requires=['flask-restful'],
    include_package_data=True,
    zip_safe=False
)