# NOTE:  TO EXECUTE THIS SETUP WHICH WILL INSTALL THE 
# SUPERCLASSES FROM WHICH INHERITANCE CAN TAKE PLACE:
# The code will be converted to c before the distributable is created. 
# For the setup.py to run using c code, download the installer for 
# Build Tools for Visual Studio from https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Run the installer and select "C++ build tools" workload
# 1. pip install cython
# 2. pip install wheel
# 3. pip install --upgrade setuptools #note: this step may not be necessary
# 4. run the setup script to convert the python files into binary
#    python setup.py build_ext --inplace
# 5. Manually remove the .py files keeping only the binary files
#    Move:  details_window.py and lookup_window.py to a backup folder 
#       which is located outside of the package directory (ui_superclasses)
#    separate from the the ui_superclasses package
# 6. run the setup script:
#    python setup.py sdist bdist_wheel
# 7. The installer files will be generated in the dist folder
# 8. Distribute the .whl file to the students for installation
# 9. Use the tar.gz file if the install using the .whl file does not work
# 10. Students will install the package using the following command:
#    pip install ui_superclasses-0.1-cp312-cp312-win_amd64.whl (or the name of the .whl file)
#    OR
#    pip install ui_superclasses-0.1.tar.gz
# 11. Installed files will be located in:
#    Linux/macOS: ~/.local/lib/pythonX.Y/site-packages/
#    Windows: C:\Users\UserName\AppData\Local\Programs\Python\PythonXY\Lib\site-packages
# 12. Once installed, students can import using:
#    from ui_superclasses.account_transactions import AccountDetailsWindow
#    from ui_superclasses.client_lookup import ClientLookupWindow
# 13. To uninstall:
#    pip uninstall ui_superclasses


from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

# Define extensions that need to be compiled
extensions = [
    Extension("ui_superclasses.*", ["ui_superclasses/*.py"]),
    # Add more extensions if needed
]

setup(
    name='ui_superclasses',
    version='0.1',
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    # other necessary information like author, author_email, etc.
)
