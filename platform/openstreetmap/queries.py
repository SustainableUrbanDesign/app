def create_osm_to_geojson_query(
    table=None,
    fclass="",
    limit="",
    xmin=23.5,
    ymin=61.45,
    xmax=23.8,
    ymax=61.5,
    epsg=4326,
):
    """
    Create a quuery that returns GeoJSON data from OSM data in PostGIS.
    """
    # TODO: ensure this query is secured from SQL injection
    # by using a psycopg2 parameterized query

    # TODO: determine how best to allow WHERE clause
    # to filter based on fclass and possibly geometry.
    
    if limit:
        limit = f"LIMIT {limit}"
        
    if fclass:
        fclass = f"""AND "fclass" = '{fclass}'"""
        
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
                -- where bounding box contains geometry
                -- https://postgis.net/docs/ST_Geometry_Contain.html
                WHERE ST_MakeEnvelope (
                    { xmin }, { ymin },
                    { xmax }, { ymax },
                    { epsg }
                ) ~ "geometry"
                { fclass }
                { limit }
            ) inputs
        ) features;
    """
