<template>
  <q-page class="flex flex-center">
    <MglMap :mapStyle="style" :zoom="zoom" :hash="true" />
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
          }
        },
        layers: [
          {
            id: "simple-tiles",
            type: "raster",
            source: "raster-tiles",
            minzoom: 0,
            maxzoom: 22
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