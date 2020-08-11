# -*- coding: cp1251 -*-
import arcpy
table = 'table_name_in_project'
field = 'field_name_in_project'
with arcpy.da.SearchCursor(table, [field]) as cursor:
    a = sorted({row[0] for row in cursor})
a = str(a)
b = a.split(',')
len(b) #вывод количества объектов