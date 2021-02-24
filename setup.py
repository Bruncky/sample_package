from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(
    name='sample_package',
    version="1.0",
    description="A sample package that does a few cool things.",
    packages=find_packages(),
    install_requires=requirements,
    test_suite='tests',
    # include_package_data: to install data from MANIFEST.in
    include_package_data=True,
    scripts=['scripts/sample_package-computedist'],
    zip_safe=False
)
