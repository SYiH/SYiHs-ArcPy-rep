# -*- coding: cp1251 -*-
import arcpy

#Скрипт для выполнения в проекте аркмап!!! Рабиение слоя на отдельные шейпы

arcpy.env.workspace = r"E:/зоны куги 1108" #рабочая область
lyr = "--polygone" #слой В ПРОЕКТЕ!!!
out_loc = r"E:/зоны куги 1108" #выходная область
i = 0
while i <= 41:
    arcpy.FeatureClassToFeatureClass_conversion('--polygon', out_loc, "zone"+str(i), """FID = (%s)"""%i)
    i = i+1