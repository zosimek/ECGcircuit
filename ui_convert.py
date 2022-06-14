from PyQt4 import uic

""" Write .ui file int .py file in order to initialise 
    component default values and attributes"""

file_in = open('ui_main.ui', 'r')
file_out = open('ui_main.py', 'w')
uic.compileUi(file_in, file_out, execute=False)
file_in.close()
file_out.close()