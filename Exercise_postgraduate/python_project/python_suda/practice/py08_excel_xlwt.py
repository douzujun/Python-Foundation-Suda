# -*- coding: utf-8 -*-

from xlwt import *

book = Workbook()
sheet1 = book.add_sheet('First')
a1 = Alignment()      # 对齐方式
a1.horz = Alignment.HORZ_CENTER
a1.vert = Alignment.VERT_CENTER

borders = Borders()
borders.bottom = Borders.THICK  # 边框样式

style = XFStyle()
style.alignment = a1
style.borders = borders
row0 = sheet1.row(0)
row0.write(0, 'test', style=style)

book.save(r'./file/test.xls')


