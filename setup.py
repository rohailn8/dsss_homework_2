from setuptools import setup, find_packages

setup(
    name='math_quiz',              
    version='0.1.0',                
    packages=find_packages(),              
    author='Rohail Naushad',    
    author_email='RohailN8@gmail.com',
    description='Package for Math Quiz that tests users calculations against operations on 2 random integers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rohailn8/dsss_homework_2',  
    classifiers=[                          
        'Programming Language :: Python :: 3',
        'License :: Apache-2.0 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',               
)
