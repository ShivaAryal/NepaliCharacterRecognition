import cx_Freeze
import sys
import matplotlib

import os

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
	base = "Win32GUI"

additional_mods = ['numpy.core._method','numpy.lib.format']
executables = [cx_Freeze.Executable("painttest.py", base = base)]
cx_Freeze.setup(
	name = "NepaliCharacterRecognizer",
	opiton = {"build_exe": {"packages": ["tkinter","keras","PIL","cv2","numpy"],"include_files":["final_model.hs"], 'includes': additional_mods}},
	version = "0.01",
	executables = executables

	)
