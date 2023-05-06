import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'data'
# points = r'data//ne_10m_populated_places.shp'
# airports = r'data//ne_10m_airports.shp'
roads = arcpy.GetParameterAsText(0)
countries = arcpy.GetParameterAsText(1)
# port = r'data//ne_10m_ports.shp'
output = arcpy.GetParameterAsText(2)
pop_number=arcpy.GetParameterAsText(3)
arcpy.MakeFeatureLayer_management(roads, 'road_layer')
total_count=0
created_count=0
with arcpy.da.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'POP_EST', 'CONTINENT', 'INCOME_GRP']) as c:
    total_count+=1
    for x in c:
        formatted_output_name = x[1].replace('(', '').replace(')', '_')
        if x[3] == 'Africa' and x[2] > float(pop_number):
            arcpy.MakeFeatureLayer_management(countries, 'country_layer', """ "FID" = {} """.format(x[0]))
            arcpy.SelectLayerByLocation_management('road_layer', "WITHIN", 'country_layer')
            income = x[4].replace('.', ' ')
            arcpy.FeatureClassToFeatureClass_conversion('road_layer', output, 'Roads_in_{}_{}'.format(formatted_output_name, income))
            created_count+=1
            print('Needed {}_{} '.format(formatted_output_name, income))

        else:
            print('not needed ' + formatted_output_name)
outputlog="[0] contries created out of [1]".format(created_count,total_count)
arcpy.AddMessage(outputlog)