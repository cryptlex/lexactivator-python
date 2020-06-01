import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptlex.lexactivator",
    version="3.10.0",
    author="Cryptlex, LLC",
    author_email="support@cryptlex.com",
    description="LexActivator API wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cryptlex/lexactivator-python",
    packages=setuptools.find_packages(),
    package_data={'cryptlex': ['lexactivator/libs/win32/**/*.dll', 'lexactivator/libs/linux/**/**/*.so', 'lexactivator/libs/macos/**/*.dylib']},
    keywords='cryptlex lexactivator licensing',
    classifiers=[
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        "Operating System :: OS Independent",
    ]
)