/*
Prepare initial map with OSM and vector layers.
*/
var osmSource = new ol.source.OSM();

var osmBaseMap = new ol.layer.Tile({
  source: osmSource,
});

var areaSource = new ol.source.Vector();

var areaVectorStyle = new ol.style.Style({
  fill: new ol.style.Fill({
    color: "rgba(255, 255, 255, 0.2)",
  }),
  stroke: new ol.style.Stroke({
    color: "#ffcc33",
    width: 2,
  }),
  image: new ol.style.Circle({
    radius: 7,
    fill: new ol.style.Fill({
      color: "#ffcc33",
    }),
  }),
});

var areaVectorLayer = new ol.layer.Vector({
  source: areaSource,
  style: areaVectorStyle,
});

var areaMap = new ol.Map({
  layers: [osmBaseMap, areaVectorLayer],
  target: "area-map",
  view: new ol.View({
    center: [0, 0],
    zoom: 1,
  }),
});

/*
Add existing area to map, if  available.
*/
var existingArea = document.currentScript.dataset.geographicarea;

if (existingArea) {
  var GeoJSON = new ol.format.GeoJSON();

  var geographicAreaGeometry = GeoJSON.readGeometry(
    existingArea,
    {
      dataProjection: "EPSG:4326",
      featureProjection: "EPSG:3857",
    }
  );

  var geographicAreaFeature = new ol.Feature({
    geometry: geographicAreaGeometry,
    name: "Project Area",
  });

  areaSource.addFeature(geographicAreaFeature);

  // Zoom map to feature extent
  var layerExtent = areaSource.getExtent();

  areaMap.getView().fit(layerExtent, { padding: [50, 50, 50, 50] });
}

/*
  Toggle edit mode when map is used on Project form.
*/
var editMode = document.currentScript.dataset.editmode;

if (editMode) {
  // Project area can only be a rectangle (box)
  var draw = new ol.interaction.Draw({
    source: areaSource,
    type: "Circle",
    geometryFunction: ol.interaction.Draw.createBox(),
  });

  // Allow only one geographic area
  // by clearing any previous element
  draw.on("drawstart", function (event) {
    areaSource.clear();
  });

  var geographicAreaField = document.querySelector("[name='geographic_area']");

  draw.on("drawend", function (event) {
    var GeoJSON = new ol.format.GeoJSON();
    var feature = event.feature;

    // Parse feature to GeoJSON with EPSG 4326 coordinate system
    var featureGeoJson = GeoJSON.writeFeatureObject(feature, {
      // We want to store data in EPSG 5326
      dataProjection: "EPSG:4326",
      // OpenLayers uses EPSG 3857 by default
      featureProjection: "EPSG:3857",
    });

    geographicAreaField.value = JSON.stringify(featureGeoJson.geometry);
  });

  areaMap.addInteraction(draw);
}
