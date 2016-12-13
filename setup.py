from setuptools import setup

setup(
    name="http-server",
    description="Week 2 Day 1 Assignment - HTTP-Server",
    version=0.0,
    author="Ted Callahan and Joey Derosa",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["http-server"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={
        'console_scripts': [
            "http-server = client:client"
        ]
    }
)