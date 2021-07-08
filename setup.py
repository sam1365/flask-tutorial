from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    # packages tells Python what package directories (and the Python files they contain) 
    # to include. 
    # find_packages() finds these directories automatically so you don’t have to type them out.
    packages=find_packages(),
    # To include other files, such as the static and templates directories, 
    # include_package_data is set.
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)