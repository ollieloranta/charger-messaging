from setuptools import find_packages, setup


setup(
    version="0.0.1",
    python_requires='>3.8.0',
    name="Charger Messaging",
    author="Olli Eloranta",
    description="Simple messaging app",
    packages=find_packages(),
    install_requires=[
        "fastapi~=0.101.1",
        "motor~=3.2.0",
        "paho-mqtt~=1.6.1",
        "pymongo~=4.4.1",
        "python-dotenv~=1.0.0",
        "requests~=2.31.0",
        "uvicorn~=0.23.2"
    ]
)
