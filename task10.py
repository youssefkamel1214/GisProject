import arcpy

countries =arcpy.GetParameterAsText(0)
feild_list=arcpy.ListFields(countries)
listfield=[]
for feild in feild_list:
    if feild.type=='Double':
        listfield.append(feild.name)
list=[]
for feild in listfield:
    with arcpy.da.UpdateCursor(countries,[feild,"NAME"])as city_cursor:
        for x in city_cursor:
            if x[0]<2019:
                x[0]=2019
                list.append(x[1])
                city_cursor.updateRow(x)
arcpy.AddMessage(str(len(list))+" countries updated")
for country in list:
    arcpy.AddMessage(country)