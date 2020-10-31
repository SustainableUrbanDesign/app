/*
Prepare initial map with OSM and vector layers.
*/
var osmSource = new ol.source.OSM();

var osmBaseMap = new ol.layer.Tile({
  source: osmSource,
});

var projectAreaSource = new ol.source.Vector();

var projectAreaVectorStyle = new ol.style.Style({
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

var projectAreaVector = new ol.layer.Vector({
  source: projectAreaSource,
  style: projectAreaVectorStyle,
});

var projectAreaMap = new ol.Map({
  layers: [osmBaseMap, projectAreaVector],
  target: "map",
  view: new ol.View({
    center: [0, 0],
    zoom: 1,
  }),
});

/*
Add existing project area to map, if  available.
*/
var existingProjectArea = document.currentScript.dataset.projectgeographicarea;

if (existingProjectArea) {
  var GeoJSON = new ol.format.GeoJSON();

  var projectGeographicAreaGeometry = GeoJSON.readGeometry(
    existingProjectArea,
    {
      dataProjection: "EPSG:4326",
      featureProjection: "EPSG:3857",
    }
  );

  var projectGeographicAreaFeature = new ol.Feature({
    geometry: projectGeographicAreaGeometry,
    name: "Project Area",
  });

  projectAreaSource.addFeature(projectGeographicAreaFeature);

  // Zoom map to feature extent
  var layerExtent = projectAreaSource.getExtent();

  projectAreaMap.getView().fit(layerExtent, { padding: [50, 50, 50, 50] });
}

/*
  Toggle edit mode when map is used on Project form.
*/
var editMode = document.currentScript.dataset.editmode;

if (editMode) {
  // Project area can only be a rectangle (box)
  var draw = new ol.interaction.Draw({
    source: projectAreaSource,
    type: "Circle",
    geometryFunction: ol.interaction.Draw.createBox(),
  });

  // Allow only one project area
  // by clearing any previous element
  draw.on("drawstart", function (event) {
    projectAreaSource.clear();
  });

  var geographicAreaField = document.querySelector("[name='geographic_area'");

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

  projectAreaMap.addInteraction(draw);
}
