# -*- coding: cp1251 -*-

import arcpy

#Заполнение <NULL> пустых ячеек
path = r'way_to_table' #путь к таблице
fieldObs = arcpy.ListFields(path)  
fieldNames = []  
for field in fieldObs:  
    fieldNames.append(field.name)  
del fieldObs  
fieldCount = len(fieldNames)  

with arcpy.da.UpdateCursor(path, fieldNames) as curU:  
    for row in curU:  
        rowU = row  
        for field in range(fieldCount):  
            if rowU[field] == " ":  
                rowU[field] = "<NULL>"  
      
      
        curU.updateRow(rowU)

del curU
