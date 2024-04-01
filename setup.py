import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='OptionSelect',
    version='0.0.0',
    author='Record Linking Lab',
    author_email='recordlinkinglab@gmail.com',
    description='This is a simple python package that allows you to create a menu and ensure correct user input.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/byuawsfhtl/py-option-select',
    project_urls = {
        "Bug Tracker": "https://github.com/byuawsfhtl/py-option-select/issues"
    },
    packages=['OptionSelect'],
    install_requires=[],
)