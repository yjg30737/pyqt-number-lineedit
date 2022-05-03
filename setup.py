from setuptools import setup, find_packages

setup(
    name='pyqt-number-lineedit',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='QLineEdit which allows only numeric input',
    url='https://github.com/yjg30737/pyqt-number-lineedit.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)