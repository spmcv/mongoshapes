# MongoShapes


This project is a complete replacement of the GeoJSON field functionality of [MongoEngine] which exploits the
[__geo_interface__] protocol to handle BSON serialization and deserialization from MongoDB. This is accomplished by 
integrating [Shapely]'s corresponding GeoJSON-like geometry types:

 * Point
 * LineString
 * Polygon
 * MultiPoint
 * MultiLineString
 * MultiPolygon
 * GeometryCollection
 
For substituting the [MongoEngine] field types:

 * PointField
 * LineStringField
 * PolygonField
 * MultiPointField
 * MultiLineStringField
 * MultiPolygonField
 
And additionally providing:
 
 * GeometryCollectionField
 
Wherein the field value stored in memory is the corresponding geometry instance rather than a GeoJSON mapping. This 
provides direct access to all of [Shapely]'s geometry operations and manipulations as well as access to an 
[__array_interface__] protocol for [NumPy].

Field validation is overridden with [Shapely]'s implementation of [OpenGIS] standards. Geo-querying via MongoDB's 
[2dsphere] is also supported (with exception of GeometryCollection) in the usual manner.

## Usage

Usage is intended to be consistent with the [MongoEngine] documentation:

```python
import random
import mongoengine as me
import mongoshapes as ms

from shapely.geometry import box, mapping
from shapely.geometry.base import BaseGeometry


class Doc(me.Document):
    point = ms.PointField()


def bbox(geometry: BaseGeometry) -> ms.PolygonDict:
    buffered = geometry.buffer(5)
    bounds = buffered.bounds
    polygon = box(*bounds)
    mapped = mapping(polygon)
    return mapped


me.connect('mydb')

new = ms.Point(map(lambda x: random.uniform(-x, x), (180, 90)))

doc = Doc()
doc.point = new
doc.validate()
doc.save()

qry = doc.objects(point__geo_within=bbox(new))
assert qry.first() is not None
```

## Testing

Using provided examples from MongoDB's [GeoJSON] documentation as fixtures, a full [py.test] suite exists:

 * **unit** for testing GeoJSON fixtures with [Shapely] and [MongoEngine].
 * **func** for testing validation and querying with new field types.


[py.test]: https://docs.pytest.org/
[NumPy]: http://www.numpy.org/
[Shapely]:  https://shapely.readthedocs.io/en/stable/manual.html
[MongoEngine]: http://mongoengine.org/
[OpenGIS]: http://www.opengeospatial.org/standards/sfa
[2dsphere]: https://docs.mongodb.com/manual/core/2dsphere/
[GeoJSON]: https://docs.mongodb.com/manual/reference/geojson/
[__geo_interface__]: https://gist.github.com/zzpwelkin/2279867
[__array_interface__]: https://docs.scipy.org/doc/numpy/reference/arrays.interface.html
