from setuptools import find_packages, setup

packages = [
    "pytest<7,>=5",
    "pytest-timeout",
]

setup(
    name="entry_level_coding_exercise",
    version="1.0.0",
    author="Zuhlke Engineering Ltd",
    author_email="recruiting@zuhlke.com",
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
    install_requires=packages
    + [
        "wheel",
        "setuptools==50.3.2",
    ],
    setup_requires=["pytest-runner"],
    tests_require=packages,
)
