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

      <vl-layer-vector :if="osmData">
        <vl-source-vector
          :features="osmData.features"></vl-source-vector>

        <vl-style-box>
          <vl-style-circle :radius="3">
            <vl-style-fill color="green"></vl-style-fill>
            <vl-style-stroke color="white"></vl-style-stroke>
          </vl-style-circle>
        </vl-style-box>
      </vl-layer-vector>
      
      <vl-layer-vector :if="buffers">
        <vl-source-vector
          :features="buffers.features"></vl-source-vector>

        <vl-style-box>
          <vl-style-stroke color="green" :width="3"></vl-style-stroke>
          <vl-style-fill color="rgba(255,255,255,0.5)"></vl-style-fill>
        </vl-style-box>
      </vl-layer-vector>
      
    </vl-map>
  </q-page>
</template>

<script>
import axios from "axios";
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
  computed: {
    buffers: function () {
      if (this.osmData) {
        const buffers =buffer(
          this.osmData,
          1000,
          {
            units: 'meters'
          }
        );

        return buffers;
      }

      return false;
    }
  },
  mounted() {
    axios
      .get('http://localhost:8000/openstreetmap/data')
      .then((response) => {
        this.osmData = response.data;
      });
  }
};
</script>

<style>
.vl-map {
  width: 100vw;
  height: 100vh;
  position: absolute;
}
</style>