# -*- coding: cp1251 -*-
import arcpy

#������ ��� ���������� � ������� ������!!! �������� ���� �� ��������� �����

arcpy.env.workspace = r"E:/���� ���� 1108" #������� �������
lyr = "--polygone" #���� � �������!!!
out_loc = r"E:/���� ���� 1108" #�������� �������
i = 0
while i <= 41:
    arcpy.FeatureClassToFeatureClass_conversion('--polygon', out_loc, "zone"+str(i), """FID = (%s)"""%i)
    i = i+1