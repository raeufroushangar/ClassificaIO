"""
setup.py for ClassificaIO package
"""
from distutils.core import setup

setup(
    name='ClassificaIO',
    packages=['ClassificaIO'],
    version='1.0.0',
    description='Graphical User Interface for machine learning classification algorithms from scikit-learn',
    author='G. Mias Lab',
    author_email='gmiaslab@gmail.com',
    license='MIT',
    url='https://github.com/gmiaslab/ClassificaIO',
    download_url='https://github.com/gmiaslab/ClassificaIO/archive/1.0.0.tar.gz',
    keywords=['machine learning', 'classification','bioinformatics'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Topic :: Research',
        'Topic :: Education',
        'Topic :: Utilities',
        ],
    install_requires=[
        'nltk>=3.2.5',
        'Pillow>=4.3',
        'pandas>=0.21',
        'numpy>=1.13',
        'scikit-learn>=0.19.1'],
    zip_safe=False
)