#antes de tudo instale o pip install pyqrcode
#pip install pypng


import pyqrcode
code = pyqrcode.create('https://pt.stackoverflow.com/users/132/victor-stafusa')
code.png('codigo.png', scale=6,)
code.show()


