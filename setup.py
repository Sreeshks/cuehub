from setuptools import setup, find_packages

setup(
    name='cuehub',
    version='0.1.0',
    py_modules=['cli'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cue=cli:cue
    ''',
    author="Adhivp",
    author_email="adhivp910@gmail.com",
    description="CueHub CLI for setting up project frameworks",
    url="https://github.com/Adhivp/cuehub",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
