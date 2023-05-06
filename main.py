import arcpy
arcpy.env.overwriteOutput = True

# Links

arcpy.env.workspace = r'data'
points = r'data//ne_10m_populated_places.shp'
countries = r'data//ne_10m_admin_0_countries.shp'
airports = r'data//ne_10m_airports.shp'
roads = r'data//ne_10m_roads.shp'
port = r'data//ne_10m_ports.shp'
output = r'output'
feature_list = arcpy.ListFeatureClasses()
# Task 2

# arcpy.MakeFeatureLayer_management(airports , 'airports_layer' , """ type = 'military' """)
# arcpy.FeatureClassToFeatureClass_conversion('airports_layer' , output , 'military_airports')
# with arcpy.da.SearchCursor('airports_layer' , ['name'] , """ type = 'military' """) as sc:
#     for x in sc:
#         print(x[0])


# Task 3

# arcpy.MakeFeatureLayer_management(roads, 'roads_layer', """ continent = 'Asia' """)
# arcpy.FeatureClassToFeatureClass_conversion('roads_layer', output, 'roads3')
# with arcpy.da.SearchCursor('roads_layer', ['name','continent']) as RC:
#     for x in RC:
#      if x[1] == 'Asia':
#         if x[0] != " ":
#             print(x[0])


# Task 4

# country_files = ['Italy', 'Spain', 'France']
# arcpy.MakeFeatureLayer_management(port,'port_layer')
# for x in country_files:
#  arcpy.MakeFeatureLayer_management(countries,'country_layer', """ "NAME" = '{}' """.format(x))
#  arcpy.SelectLayerByLocation_management('port_layer', 'WITHIN', 'country_layer')
#  arcpy.FeatureClassToFeatureClass_conversion('port_layer', output, 'ports_in_{}'.format(x))


# Task 5

# part1
Arabic_countries = ['Egypt', 'Saudi Arabia', 'Iraq', 'Jordan', 'United Arab Emirates', 'Lebanon', 'Tunisia',
                    'Algeria', 'Morocco', 'Oman', 'Qatar', 'Bahrain', 'Yemen', 'Sudan', 'Syria']

arcpy.MakeFeatureLayer_management(points, 'point_layer')
# for x in Arabic_countries:
#  arcpy.MakeFeatureLayer_management(countries,'country_layer', """ "NAME" = '{}' """.format(x))
#  arcpy.SelectLayerByLocation_management('point_layer', 'WITHIN', 'country_layer')
#  arcpy.FeatureClassToFeatureClass_conversion('point_layer', output, 'points_in_{}'.format(x))


# part2
with arcpy.da.SearchCursor(countries, ['NAME']) as CC:
  for x in CC:
    if x[0] in Arabic_countries:
     arcpy.MakeFeatureLayer_management(countries,'country_layer', """ "NAME" = '{}' """.format(x[0]))
     arcpy.SelectLayerByLocation_management('point_layer', 'WITHIN', 'country_layer')
     arcpy.FeatureClassToFeatureClass_conversion('point_layer', output, 'points_in_{}'.format(x[0]))


# Task 6

# with arcpy.da.SearchCursor(airports, ['type', 'name', 'location', 'wikipedia'])  as Ac:
#     for x in Ac:
#         if x[0] == 'major':
#             print('name = ' + x[1])
#             print('location = {}'.format(x[2]))
#             print('wikipedia = {}'.format(x[3]))
#             print('--------------------------------')


# Task 7

# arcpy.MakeFeatureLayer_management(roads, 'road_layer')
# with arcpy.da.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'POP_EST', 'CONTINENT', 'INCOME_GRP']) as c:
#     for x in c:
#         formatted_output_name = x[1].replace('(', '').replace(')', '_')
#         if x[3] == 'Africa' and x[2] > 25e6:
#             arcpy.MakeFeatureLayer_management(countries, 'country_layer', """ "FID" = {} """.format(x[0]))
#             arcpy.SelectLayerByLocation_management('road_layer', "WITHIN", 'country_layer')
#             income = x[4].replace('.', ' ')
#             arcpy.FeatureClassToFeatureClass_conversion('road_layer', output, 'Roads_in_{}_{}'.format(formatted_output_name, income))
#             print('Needed {}_{} '.format(formatted_output_name, income))
#
#         else:
#             print('not needed ' + formatted_output_name)