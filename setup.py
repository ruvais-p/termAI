from setuptools import setup, find_packages
import os

setup(
    name="termAI",
    version="1.0.0",
    packages=find_packages(include=['ai_terminal_assistant', 'ai_terminal_assistant.*']),
    include_package_data=True,
    install_requires=[
        "click",
        "google-generativeai",
    ],
    entry_points={
        "console_scripts": [
            "ata=ai_terminal_assistant.cli:main",
        ],
    },
    author="Ruvais",
    author_email="ruvaispuv@gmail.com",
    description="AI-powered terminal assistant to convert natural language into shell commands.",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/ruvais-p/termAI.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
