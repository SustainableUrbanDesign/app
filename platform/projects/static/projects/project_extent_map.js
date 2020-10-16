import Litedom from '//unpkg.com/litedom';

var osmSource = new ol.source.OSM();

var osmBaseMap = new ol.layer.Tile({
  source: osmSource,
});

var projectExtentSource = new ol.source.Vector();

var projectExtentVectorStyle = new ol.style.Style({
  fill: new ol.style.Fill({
    color: 'rgba(255, 255, 255, 0.2)',
  }),
  stroke: new ol.style.Stroke({
    color: '#ffcc33',
    width: 2,
  }),
  image: new ol.style.Circle({
    radius: 7,
    fill: new ol.style.Fill({
      color: '#ffcc33',
    }),
  }),
});

var projectExtentVector = new ol.layer.Vector({
  source: projectExtentSource,
  style: projectExtentVectorStyle,
});

var projectExtentMap = new ol.Map({
  layers: [osmBaseMap, projectExtentVector],
  target: 'map',
  view: new ol.View({
    center: [0, 0],
    zoom: 4,
  }),
});

// Project extent can only be a rectangle (box)
var draw = new ol.interaction.Draw({
  source: projectExtentSource,
  type: 'Circle',
  geometryFunction: ol.interaction.Draw.createBox()
});

// Allow only one project extent
// by clearing any previous element
draw.on("drawstart", function (event) {
  projectExtentSource.clear();
});

Litedom({
  el: '#editModeToggle',
  data: {
    editMode: 'off'
  },
  toggleEditMode() {
    var editMode = this.data.editMode;

    if (editMode === 'on') {
      projectExtentMap.addInteraction(draw);
    } else {
      projectExtentMap.removeInteraction(draw);
    }
  }
})