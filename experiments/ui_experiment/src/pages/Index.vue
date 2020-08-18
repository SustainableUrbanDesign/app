<template>
  <q-page class="flex flex-center">
    <MglMap :mapStyle="style" :zoom="zoom" :hash="false" :center="center"></MglMap>
  </q-page>
</template>

<script>
import Mapbox from "mapbox-gl";
import { MglMap } from "vue-mapbox";

export default {
  name: "PageIndex",
  components: {
    MglMap
  },
  data() {
    return {
      center: [23.7610, 61.4978],
      zoom: 10,
      style: {
        version: 8,
        sources: {
          "raster-tiles": {
            type: "raster",
            tiles: [
              "https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg"
            ],
            tileSize: 256
          },
          "finland-osm": {
            type: "geojson",
            data: "http://localhost:8000/openstreetmap/data",
          }
        },
        layers: [
          {
            id: "simple-tiles",
            type: "raster",
            source: "raster-tiles",
            minzoom: 0,
            maxzoom: 22
          },
          {
            id: "finland-osm",
            type: "circle",
            source: "finland-osm",
            paint: {
              'circle-radius': 6,
              'circle-color': 'blue'
            },
            filter: ['==', '$type', 'Point']
          }
        ]
      }
    };
  }
};
</script>

<style>
.mgl-map-wrapper {
  width: 100vw;
  height: 90vh;
}
</style>