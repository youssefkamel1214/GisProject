import arcpy

port =arcpy.GetParameterAsText(0)
updatefield=arcpy.GetParameterAsText(1)
with arcpy.da.UpdateCursor(port,['website'])as city_cursor:
    for x in city_cursor:
        if x[0]==' ':
            x[0]=updatefield
            city_cursor.updateRow(x)
arcpy.AddMessage("Done")