geojson_content = """
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": { "name": "Adana" },
      "geometry": {
        "type": "Polygon",
        "coordinates": [[[35.0, 37.0],[36.0, 37.0],[36.0, 36.0],[35.0, 36.0],[35.0, 37.0]]]
      }
    }
    /* Diğer illeri buraya ekleyebilirsin */
  ]
}
"""

with open("turkey.geojson", "w") as f:
    f.write(geojson_content)
print("turkey.geojson oluşturuldu.")
