from osgeo import ogr, gdal
import os.path



def clean_shapefile(shp):
    driver = ogr.GetDriverByName('KML')
    datasource = driver.Open(shp)

    layer = datasource.GetLayer()

    for feature in layer:
        geom = feature.GetGeometryRef()
        if not geom.IsValid():
            feature.SetGeometry(geom.Buffer(0))
            layer.SetFeature(feature)
            assert feature.GetGeometryRef().IsValid()

    layer.ResetReading()
    assert all(feature.GetGeometryRef().IsValid() for feature in layer)


# function to clip raster by a polygon (shapefile)
def clip_raster(raster, shp, output_raster):
    clean_shapefile(shp)
    result = gdal.Warp(output_raster, raster, cutlineDSName=shp, cropToCutline=True, dstNodata=0)





shp = "zi.kml"
list_pan = []
list_ms = []
list_name = []
count = 0

try:
    for address, dirs, files in os.walk('images'):
        for name in files:
            if ".tif" in os.path.join(address, name):
                path = os.path.join(address, name)
                output_raster = os.getcwd() + r'\\' + address + r'\\' + "new_imagery.tif"
                raster = path
                clip_raster(raster, shp, output_raster)
                os.rename(path, address + r'\\' + "old_imagery.tif")
                os.rename(address + r'\\' "new_imagery.tif", path)
                count  = count + 1
                cnt = dirs
                print(str(count) + ") " + path + " снимок обрезан. Не забудьте удалить исходные снимки")
    print("Обрезано снимков: " + str(count));
except NameError:
    print("NameError: x is not defined.")






a = input()
