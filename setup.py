from setuptools import setup, find_packages

setup(
    name='herba_scraper',
    version='0.0.1',
    author='zegal',
    author_email='zgeal@example.com',
    description='A simple toolkit for common tasks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_toolkit',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        "requests>=2.25.1",
        "beautifulsoup4>=4.9.3",
        "lxml>=4.6.2",
    ],
    test_requirements=[
        "pytest-httpbin==2.1.0",
        "pytest-cov",
        # "pytest-mock",
        # "pytest-xdist",
        # "PySocks>=1.5.6, !=1.5.7",
        "pytest>=3",
    ]
)
