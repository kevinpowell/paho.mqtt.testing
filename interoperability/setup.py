from setuptools import setup

version = "0.0"

# put package dependencies here for pip to check against
# you can also specify version numbers for pip to resolve
   # 'A>=1,<2' -> Package A version must be geq 1 AND lt 2
   # 'B>=2' -> Package B version must be geq 2
install_requirements = [
    'asyncio-mqtt',
    'pytest'
]

setup(
    name                = "mqtt",
    version             = version,
    description         = "paho mqtt test code",
    install_requires    = install_requirements,
    python_requires     = '>=3.9'
)
