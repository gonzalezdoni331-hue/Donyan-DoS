from setuptools import setup, find_packages

setup(
    name='medusa-ddos',
    version='3.1.0',
    py_modules=['medusa'],
    install_requires=[
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'medusa=medusa:main',
        ],
    },
    author='TrashDono',
    author_email='contact@trashdono.com',
    description='A high-performance Layer 7 DDoS tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
