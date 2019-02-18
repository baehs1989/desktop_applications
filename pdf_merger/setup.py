from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [Executable("pdf_merger.py", base=base)]

setup(
    name = "TEST",
    options = {"build_exe": {"packages":["tkinter","sqlite3"], "include_files":[]}},
    version = "0.01",
    description = "TEST",
    executables = executables
)

# from distutils.core import setup
# import py2exe
#
# setup(console=["bookstore.py"])
#

# from setuptools import setup
#
# OPTIONS = {
#     'packages':['tkinter', 'PyPDF2']
# }
#
# setup(
#     app=["pdf_merger.py"],
#     options={'py2app':OPTIONS},
#     setup_requires=["py2app"]
# )
