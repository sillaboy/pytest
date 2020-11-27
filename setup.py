from distutils.core import setup
# python setup.py build
# python setup.py sdist
# python setup.py install
# python
# >>> import yl.hello
# >>> yl.hello.hello("hai")

setup(
    name='hello',  # 需要打包的名字
    version='v1.0',  # 版本
    py_modules=['yl.hello']  # 需要打包的模块
)
