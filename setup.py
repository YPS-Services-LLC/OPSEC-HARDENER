from setuptools import setup, find_packages

setup(
    name="opsec-hardener",
    version="0.1.0",
    description="OPSEC Hardener - tools for network, snapshots, and GUI hardening",
    author="YPS Services LLC",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "psutil",
    ],
    entry_points={
        "console_scripts": [
            "opsec=opsec_hardener.cli:main",
            "opsec-gui=opsec_hardener.gui:main",
        ],
    },
)
