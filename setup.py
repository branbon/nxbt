from setuptools import setup

setup(
    name="nxbt",
    include_package_data=True,
    long_description_content_type="text/markdown",
    install_requires=[
        "dbus-python==1.3.2",
        "Flask==2.2.2",
        "Flask-SocketIO==5.3.2",
        "eventlet==0.33.2",
        "blessed==1.19.1",
        "pynput==1.7.6",
        "psutil==5.9.4",
        "cryptography==38.0.4",
        "dnspython==2.2.1",
    ],
    extra_require={
        "dev": [
            "pytest"
        ]
    }
)
