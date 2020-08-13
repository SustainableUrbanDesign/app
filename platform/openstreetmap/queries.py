def create_osm_to_geojson_query(table=None, fclass=None, limit=10):
    """
    Create a quuery that returns GeoJSON data from OSM data in PostGIS.
    """
    # TODO: determine how best to allow WHERE clause
    # to filter based on fclass and possibly geometry.
    return f"""
        SELECT jsonb_build_object(
            'type',     'FeatureCollection',
            'features', jsonb_agg(feature)
        )
        FROM (
            SELECT jsonb_build_object(
                'type',       'Feature',
                'id',         osm_id,
                'geometry',   ST_AsGeoJSON(geometry)::jsonb,
                'properties', to_jsonb(inputs) - 'geometry'
            ) AS feature
            FROM (
                SELECT 
                    "osm_id",
                    "code",
                    "fclass",
                    "name",
                    "geometry"
                FROM { table }
                limit { limit }
            ) inputs
        ) features;
    """