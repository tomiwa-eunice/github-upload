import json
import os
from osgeo import ogr
myVegaSpec=json.loads('''{
"$schema": "https://vega.github.io/schema/vega-lite/v3.json",
"description": "A simple bar chart with embedded data.",
"data": {
},
"mark": "bar",
"encoding": {
"x": {"field": "Name", "type": "ordinal"},
"y": {"field": "No_inhabit", "type": "quantitative"},
"color":{
"field":"No_inhabit",
"scale":{
"domain":[1,150000],
"scheme":"yelloworangered"
},
"type":"quantitative"
}
}
}''')