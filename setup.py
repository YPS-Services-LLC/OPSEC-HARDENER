cat > setup.py <<'EOF'
from setuptools import setup, find_packages

setup(
    name="opsec-hardener",
    version="0.1.0",
    description="Sys-Snapshots + Network Hardening Toolkit",
    author="Emmanuel Angelo Rigopoulos",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pygobject",
        "psutil",
    ],
    entry_points={
        "console_scripts": [
            "opsec=opsec_hardener.cli:main",
            "opsec-gui=opsec_hardener.gui:main",
        ],
    },
    python_requires=">=3.8",
)
EOF
