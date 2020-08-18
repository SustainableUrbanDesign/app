<template>
  <q-page class="flex flex-center">
    <vl-map
      :load-tiles-while-animating="true"
      :load-tiles-while-interacting="true"
      data-projection="EPSG:4326">
      <vl-view :zoom.sync="zoom" :center.sync="center"></vl-view>

      <vl-layer-tile id="osm">
        <vl-source-osm></vl-source-osm>
      </vl-layer-tile>

      <vl-layer-vector>
        <vl-source-vector
          url="http://localhost:8000/openstreetmap/data"
          :features.sync="osmData"></vl-source-vector>

        <vl-style-box>
          <vl-style-circle :radius="3">
            <vl-style-fill color="green"></vl-style-fill>
            <vl-style-stroke color="white"></vl-style-stroke>
          </vl-style-circle>
        </vl-style-box>
      </vl-layer-vector>
    </vl-map>
  </q-page>
</template>

<script>
import buffer from "@turf/buffer";
import Vue from 'vue'

import VueLayers from 'vuelayers';
import 'vuelayers/lib/style.css';

Vue.use(VueLayers)

export default {
  name: "PageIndex",
  data() {
    return {
      center: [23.7610, 61.4978],
      zoom: 10,
      osmData: false
    }
  },
};
</script>

<style>
.vl-map {
  width: 100vw;
  height: 100vh;
  position: absolute;
}
</style>