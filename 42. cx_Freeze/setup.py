# https://pypi.python.org/pypi?:action=display&name=cx_Freeze&version=4.3.3

# from command window, now you would go to the dir, run python setup.py build...
# this makes a build directory, within which you can find your new .exe! 


from cx_Freeze import setup, Executable

setup(name = "reandurllib" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("reandurllib.py")])
