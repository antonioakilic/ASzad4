from setuptools import find_packages, setup

package_name = 'zad4_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='antonioakilic',
    maintainer_email='antonio.akilic@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'brojcanik = zad4_pubsub.brojcanik:main',
            'kvadriranje_broja = zad4_pubsub.kvadriranje_broja:main',
        ],
    },
)
