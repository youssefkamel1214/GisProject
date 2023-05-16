import arcpy
import os
from PIL import Image,ExifTags
arcpy.env.overwriteOutput = True

# Links

arcpy.env.workspace = r'data'
points = r'data//ne_10m_populated_places.shp'
countries = r'data//ne_10m_admin_0_countries.shp'
airports = r'data//ne_10m_airports.shp'
roads = r'data//ne_10m_roads.shp'
port = r'data//ne_10m_ports.shp'
imgfolder=r'images'
output = r'output'
# Task 1
def task1():
    feature_list = arcpy.ListFeatureClasses()
    print (feature_list)
# Task 2
def task2():
    arcpy.MakeFeatureLayer_management(airports , 'airports_layer' , """ type = 'military' """)
    arcpy.FeatureClassToFeatureClass_conversion('airports_layer' , output , 'military_airports')
    with arcpy.da.SearchCursor('airports_layer' , ['name'] , """ type = 'military' """) as sc:
        for x in sc:
            print(x[0])


# Task 3
def task3():
    arcpy.MakeFeatureLayer_management(roads, 'roads_layer', """ continent = 'Asia' """)
    arcpy.FeatureClassToFeatureClass_conversion('roads_layer', output, 'roads3')
    with arcpy.da.SearchCursor('roads_layer', ['name','continent']) as RC:
        count=0
        for x in RC:
            count+=1
            if x[0] != " ":
                print(x[0])
        print (count)

# Task 4
def task4():
    country_files = ['Italy', 'Spain', 'France']
    arcpy.MakeFeatureLayer_management(port,'port_layer')
    for x in country_files:
         arcpy.MakeFeatureLayer_management(countries,'country_layer', """ "NAME" = '{}' """.format(x))
         arcpy.SelectLayerByLocation_management('port_layer', 'WITHIN', 'country_layer')
         arcpy.FeatureClassToFeatureClass_conversion('port_layer', output, 'ports_in_{}'.format(x))


# Task 5
def task5():
    Arabic_countries = ['Palestine', 'Lebanon', 'S. Sudan', 'Somalia', 'Syria', 'Morocco', 'Oman', 'United Arab Emirates',
                        'Libya', 'Tunisia', 'Sudan', 'Djibouti', 'Qatar', 'Saudi Arabia', 'Kuwait',
                        'Algeria', 'Jordan', 'Egypt', 'Yemen', 'Mauritania', 'Comoros', 'Bahrain']
    arcpy.MakeFeatureLayer_management(points, 'point_layer')
    # part1
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
def task6():
    with arcpy.da.SearchCursor(airports, ['type', 'name', 'location', 'wikipedia'])  as Ac:
        for x in Ac:
            if x[0] == 'major':
                print('name = ' + x[1])
                print('location = {}'.format(x[2]))
                print('wikipedia = {}'.format(x[3]))
                print('--------------------------------')


# Task 7
def task7():
    arcpy.MakeFeatureLayer_management(roads, 'road_layer')
    with arcpy.da.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'POP_EST', 'CONTINENT', 'INCOME_GRP']) as c:
        for x in c:
            formatted_output_name = x[1].replace('(', '').replace(')', '_')
            if x[3] == 'Africa' and x[2] > 25e6:
                arcpy.MakeFeatureLayer_management(countries, 'country_layer', """ "FID" = {} """.format(x[0]))
                arcpy.SelectLayerByLocation_management('road_layer', "WITHIN", 'country_layer')
                income = x[4].replace('.', ' ')
                arcpy.FeatureClassToFeatureClass_conversion('road_layer', output, 'Roads_in_{}_{}'.format(formatted_output_name, income))
                print('Needed {}_{} '.format(formatted_output_name, income))

            else:
                print('not needed ' + formatted_output_name)

# Task 11
def task11():
    field_list = arcpy.ListFields(points)
    for field in field_list:
       print("field name : "+str(field.name))
       print("its type : " +str(field.type))
       print ("-----"*50)

# Task 12
def task12():
    field_list = arcpy.ListFields(points)
    fields=[]
    dict=[]
    for field in field_list:
        if field.type!="String":
            fields.append(field.name)

    for feild in fields:
        with arcpy.da.UpdateCursor(points, [feild])as city_cursor:
            for x in city_cursor:
                if x[0] ==0 or x[0]==None:
                    x[0] = 1
                    city_cursor.updateRow(x)
                    print (feild)

# Task 13
def task13():
   img_contets=os.listdir(imgfolder)
   for image in img_contets:
       full_path=os.path.join(imgfolder,image)
       full_path=os.path.join(os.path.abspath(__file__),full_path)
       print (full_path)
# Task 14
def task14():
    img_contets = os.listdir(imgfolder)
    for image in img_contets:
        full_path = os.path.join(imgfolder, image)
        image=Image.open(full_path)
        exif={ExifTags.TAGS[k]:v for k,v  in image._getexif().items() if k in ExifTags.TAGS}
        print (exif)
# Task 15
def task15():
    img_contets = os.listdir(imgfolder)
    for image in img_contets:
        full_path = os.path.join(imgfolder, image)
        image = Image.open(full_path)
        exif = {ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS}
        try:
            for key in exif['GPSInfo'].keys():
                print ("this is coded value {}".format(key))
                decoded_value=ExifTags.GPSTAGS.get(key)
                print ('this is its associated labal {}'.format(decoded_value))
        except:
            print ("this image has no gps info {}".format(full_path))
        finally:
            print("---------"*50)
# Task 16
def task16():
    img_contents = os.listdir(imgfolder)
    for img in img_contents:
        full_path = os.path.join(imgfolder, img)
        pillow_img = Image.open(full_path)
        exif = {ExifTags.TAGS[k]: v for k, v in pillow_img._getexif().items() if k in ExifTags.TAGS}
        gps_all = {}
        try:
            for key in exif['GPSInfo'].keys():
                decoded_value = ExifTags.GPSTAGS.get(key)
                gps_all[decoded_value] = exif['GPSInfo'][key]

            long_ref = gps_all.get('GPSLongitudeRef')
            long = gps_all.get('GPSLongitude')
            lat_ref = gps_all.get('GPSLatitudeRef')
            lat = gps_all.get('GPSLatitude')

            print long_ref, "    ", long
            print lat_ref, "    ", lat
        except:
            print("This image has no GPS Info in it {}".format(full_path))
        finally:
            print ("-----------"*50)
task16()
