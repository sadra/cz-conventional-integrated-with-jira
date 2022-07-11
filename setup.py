from setuptools import setup

setup(
    name='CzConventionalIntegratedWithJira',
    version='0.1.0',
    description='Cz Conventional Integrated with Jira',
    author='Sadra',
    author_email='hello@sadra.me',
    license="MIT",
    url='https://github.com/sadra/cz-conventional-integrated-with-jira',
    install_requires=["commitizen"],
    py_modules=["cz_int_jira"],
)