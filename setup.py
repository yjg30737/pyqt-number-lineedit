from setuptools import setup, find_packages

setup(
    name='number-lineedit',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='QLineEdit which can input number only',
    url='https://github.com/yjg30737/number-lineedit.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)