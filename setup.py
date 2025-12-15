from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="forensic-printer-dots-analyzer",
    version="1.0.0",
    author="Abokabera2024",
    description="Forensic analysis tool for detecting and decoding printer tracking dots (Yellow Dots/MIC)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Abokabera2024/forensic-printer-dots-analyzer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Security",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Legal Industry",
    ],
    python_requires='>=3.8',
    install_requires=[
        'opencv-python>=4.8.0',
        'numpy>=1.24.0',
        'Pillow>=10.0.0',
        'scikit-image>=0.21.0',
        'Flask>=3.0.0',
        'Flask-CORS>=4.0.0',
        'scipy>=1.11.0',
        'matplotlib>=3.8.0',
        'reportlab>=4.0.0',
    ],
    entry_points={
        'console_scripts': [
            'forensic-dots=cli.cli_tool:main',
        ],
    },
)
