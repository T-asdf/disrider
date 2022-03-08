from setuptools import setup, find_packages

setup(name='disrider',
    version='1.0.3',
    description='더 쉽게, 더 빠르게. 카트라이더 전적 검색.',
    author='ㅁㄴㅇㄹ#5332',
    author_email='seojune5383@naver.com',
    url='https://blog.naver.com/seojune5383',
    license='MIT',
    py_modules=['disrider'],
    python_requires='>=3',
    install_requires=['discord', 'requests'],
    packages=['disrider']
)