<template>
  <q-page class="flex flex-center">
    <MglMap :mapStyle="style" :zoom="zoom" :hash="true"></MglMap>
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
      center: [0, 0],
      zoom: 2,
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
          route: {
            type: "geojson",
            data:
              "https://gist.githubusercontent.com/wavded/1200773/raw/e122cf709898c09758aecfef349964a8d73a83f3/sample.json"
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
            id: "route",
            type: "line",
            source: "route",
            filter: ["==", "$type", "LineString"],
            layout: {
              "line-join": "round",
              "line-cap": "round"
            },
            paint: {
              "line-color": "#888",
              "line-width": 3
            }
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