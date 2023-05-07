import arcpy

port =arcpy.GetParameterAsText(0)
updatefield=arcpy.GetParameterAsText(1)
feild_list=arcpy.ListFields(port)
listfield=[]
for feild in feild_list:
    if feild.type=='String':
        listfield.append(feild.name)
for feild in listfield:
    with arcpy.da.UpdateCursor(port,[feild])as city_cursor:
        for x in city_cursor:
            if x[0]==' ':
                x[0]=updatefield
                city_cursor.updateRow(x)
arcpy.AddMessage("Done")