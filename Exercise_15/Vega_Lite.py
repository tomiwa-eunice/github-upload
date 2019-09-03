# JSON and Vega-lite
# ex.15.1
# JSON decode

import json
family = '''{
    "jason" : {
        "name" : "Jason Lengstorf",
        "age" : "24",
        "gender" : "male"
        },
    "kyle" : {
        "name" : "Kyle Lengstorf",
        "age" : "21",
        "gender" : "male"
        }
}'''
jsonFamliy = json.loads(family)         # this passes the python over the string
print(jsonFamliy["jason"]["name"])      # prints jason's name
print(jsonFamliy["kyle"]["age"])        # prints kyle's age
print(jsonFamliy["kyle"]["gender"])     # prints kyle's gender


# ex.15.2
# GeoJSON as normal JSON
ITCJson = '''{
    "type": "FeatureCollection",
    "features":
        [
            {
                "type": "Feature",
                "properties": {
                    "description": "ITC"
                    },
                "geometry": {
                    "type": "Point",
                    "coordinates": [6.885885000228882 ,52.223790522038215]
                    }
            },
            {
                "type": "Feature",
                "properties": {
                    "description": "ITC Hotel"
                    },
                "geometry": {
                    "type": "Point",
                    "coordinates": [6.89068078994751 ,52.21800655772852]
                    }
            }
        ]
    }
    '''
ITCData = json.loads(ITCJson)
print(ITCData["features"][0]["properties"]["description"])      # 1st feature properties description
print(ITCData["features"][0]["geometry"]["coordinates"])        # 1st feature geometry coordinates
print(ITCData["features"][1]["geometry"]["type"])               # 2nd feature geometry type


# ex.15.3
# JSON for plotting in Vega-lite
import json
import os
from osgeo import ogr

# json template to plot bar-chart no of inhabitants per municipality
myVegaSpec = json.loads('''{
    "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
    "description": "A simple bar chart with embedded data.",
    "data": {},
    "mark": "bar",
    "encoding":
    {
        "x": {"field": "Name", "type": "ordinal"},
        "y": {"field": "No_inhabit", "type": "quantitative"},
        "color":
        {
            "field": "No_inhabit",
            "scale":
            {
                "domain":[1,150000],
                "scheme": "yelloworangered"
            },
            "type": "quantitative"
        }
    }
}''')

# load and use json template for charting
dataDirectory = r'C:\GeoComProjects\Exercise_15'
# change to the data directory
os.chdir(dataDirectory)

municipalitiesDs = ogr.Open("overijssel_municipalities.shp")
municipalitiesLyr = municipalitiesDs.GetLayer()

values = []
for feature in municipalitiesLyr:
    # print(feature.GetField('Name'))
    featureDict = {}
    featureDict['Name'] = feature.GetField('Name')
    featureDict['No_inhabit'] = feature.GetField('No_inhabit')
    values.append(featureDict)
print(values)

myVegaSpec['data']['values'] = values
print(json.dumps(myVegaSpec))               # convert to string and pass

with open('popbarChart.json', 'w') as outfile:
    json.dump(myVegaSpec, outfile, indent=4, sort_keys=True)        # save json template into a file


# ex.15.4
# json template to plot no of cars per municipality
myVegaSpec1 = json.loads('''{
    "$schema": "https://vega.github.io/schema/vega-lite/v3.json",
    "description": "A simple bar chart with embedded data.",
    "data": {},
    "mark": "bar",
    "encoding":
    {
        "x": {"field": "Name", "type": "ordinal"},
        "y": {"field": "No_cars", "type": "quantitative"},
        "color":
        {
            "field": "No_cars",
            "scale":
            {
                "domain":[1,70000],
                "scheme": "yelloworangered"
            },
            "type": "quantitative"
        }
    }
}''')


dataDirectory = r'C:\GeoComProjects\Exercise_15'

os.chdir(dataDirectory)

municipalitiesDs = ogr.Open("overijssel_municipalities.shp")
municipalitiesLyr = municipalitiesDs.GetLayer()

values = []
for feature in municipalitiesLyr:
    # print(feature.GetField('Name'))
    featureDict = {}
    featureDict['Name'] = feature.GetField('Name')
    featureDict['No_cars'] = feature.GetField('No_cars')
    values.append(featureDict)
print(values)

myVegaSpec1['data']['values'] = values
print(json.dumps(myVegaSpec1))               # convert to string and pass

with open('cars-barChart.json', 'w') as outfile:
    json.dump(myVegaSpec1, outfile, indent=4, sort_keys=True)        # save json template into a file


# ex.15.5
import json

# json template to plot choropleth no of inhabitants per municipality

dataDirectory = r'C:\GeoComProjects\Exercise_15'

os.chdir(dataDirectory)

file = open('choropleth_pop.json', 'r')
myVegaSpec = json.loads(file.read())
file.close()

municipalitiesDs = ogr.Open("overijssel_municipalities.shp")
municipalitiesLyr = municipalitiesDs.GetLayer()

features = []
for feature in municipalitiesLyr:
    jsonFeature = json.loads(feature.ExportToJson())
    features.append(jsonFeature)
print(features)

myVegaSpec['data']['values']['features'] = features
print(json.dumps(myVegaSpec))


with open('pop_km.json', 'w') as outfile:
    json.dump(myVegaSpec, outfile, indent=4, sort_keys=True)


# ex.15.6
# json template to plot choropleth no of cars per municipality
import os
import json
from osgeo import ogr


dataDirectory = r'C:\GeoComProjects\Exercise_15'

os.chdir(dataDirectory)

file = open('choropleth_cars.json', 'r')
myVegaSpec = json.loads(file.read())
file.close()

municipalitiesDs = ogr.Open("overijssel_municipalities.shp")
municipalitiesLyr = municipalitiesDs.GetLayer()

features1 = []
for feature in municipalitiesLyr:
    jsonFeature = json.loads(feature.ExportToJson())
    features1.append(jsonFeature)
print(features1)

myVegaSpec['data']['values']['features'] = features1
print(json.dumps(myVegaSpec))


with open('cars_pop.json', 'w') as outfile:
    json.dump(myVegaSpec, outfile, indent=4, sort_keys=True)


# ex.15.7
# json template to plot proportional symbols no of cars per municipality
dataDirectory = r'C:\GeoComProjects\Exercise_15'

os.chdir(dataDirectory)

file = open('proportional_pop.json', 'r')
myVegaSpec = json.loads(file.read())
file.close()

municipalitiesDs = ogr.Open("overijssel_municipalities.shp")
municipalitiesLyr = municipalitiesDs.GetLayer()

features1 = []
for feature in municipalitiesLyr:
    jsonFeature = json.loads(feature.ExportToJson())
    features1.append(jsonFeature)
print(features1)

myVegaSpec['data']['values']['features'] = features1
print(json.dumps(myVegaSpec))


with open('prop_pop.json', 'w') as outfile:
    json.dump(myVegaSpec, outfile, indent=4, sort_keys=True)


# ex.15.8
dataDirectory = r'C:\GeoComProjects\Exercise_15'

os.chdir(dataDirectory)

file = open('prop_choro_pop.json', 'r')
myVegaSpec = json.loads(file.read())
file.close()

municipalitiesDs = ogr.Open("overijssel_municipalities.shp")
municipalitiesLyr = municipalitiesDs.GetLayer()

features2 = []
for feature in municipalitiesLyr:
    jsonFeature = json.loads(feature.ExportToJson())
    features2.append(jsonFeature)
print(features1)

myVegaSpec['data']['values']['features'] = features2
print(json.dumps(myVegaSpec))


with open('pro__pop.json', 'w') as outfile:
    json.dump(myVegaSpec, outfile, indent=4, sort_keys=True)
















