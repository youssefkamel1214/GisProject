import arcpy

countries =arcpy.GetParameterAsText(0)
pop_number=arcpy.GetParameterAsText(1)

list=[]
with arcpy.da.UpdateCursor(countries,['POP_EST','POP_YEAR',"NAME"])as city_cursor:
    for x in city_cursor:
        if x[1]<2019:
            x[0]=float(pop_number)
            list.append(x[2])
            city_cursor.updateRow(x)
arcpy.AddMessage(str(len(list))+" countries updated")
for country in list:
    arcpy.AddMessage(country)