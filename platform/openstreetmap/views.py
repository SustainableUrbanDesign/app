import json

from django.conf import settings
from django.http import HttpResponse

import psycopg2

from .queries import create_osm_to_geojson_query


def get_osm_data(request):
    """
    Fetch OSM data from PostGIS in GeoJSON and return it in the response.
    """

    osm_db = settings.DATABASES["openstreetmap"]

    connection = psycopg2.connect(
        database=osm_db["NAME"],
        user=osm_db["USER"],
        password=osm_db["PASSWORD"],
        host=osm_db["HOST"],
    )

    cursor = connection.cursor()

    osm_query = create_osm_to_geojson_query(table="osm_points_of_interest")

    cursor.execute(osm_query)

    result = cursor.fetchone()

    response = json.dumps(result[0], indent=2)

    return HttpResponse(response)
