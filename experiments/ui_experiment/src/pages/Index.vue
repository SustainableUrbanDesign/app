<template>
  <q-page class="flex">
    <div>
      <div class="row q-mx-auto">
        <q-input
          label="Buffer distance"
          v-model.number="bufferDistance"
          type="number"
          :dense="true"
          class="q-mx-sm"
        />

        <q-select

          v-model="bufferUnits"
          :options="bufferUnitsOptions"
          label="Units"
          stack-label
          :dense="true"
          :options-dense="true"
        />
      </div>

      <div class="row">
        <vl-map
          :load-tiles-while-animating="true"
          :load-tiles-while-interacting="true"
          data-projection="EPSG:4326"
        >
          <vl-view 
            :zoom.sync="zoom" 
            :center.sync="center"></vl-view>

          <vl-layer-tile id="osm">
            <vl-source-osm></vl-source-osm>
          </vl-layer-tile>

          <vl-layer-vector :if="osmData">
            <vl-source-vector :features="osmData.features"></vl-source-vector>

            <vl-style-box>
              <vl-style-circle :radius="3">
                <vl-style-fill color="green"></vl-style-fill>
                <vl-style-stroke color="white"></vl-style-stroke>
              </vl-style-circle>
            </vl-style-box>
          </vl-layer-vector>

          <vl-feature :if="union">
            <vl-geom-multi-polygon :coordinates="union"></vl-geom-multi-polygon>
          </vl-feature>

        </vl-map>
      </div>
    </div>
  </q-page>
</template>

<script>
import axios from "axios";
import buffer from "@turf/buffer";
const polygonClipping = require('polygon-clipping')
import Vue from "vue";

import VueLayers from "vuelayers";
import "vuelayers/lib/style.css";

Vue.use(VueLayers);

export default {
  name: "PageIndex",
  data() {
    return {
      center: [23.761, 61.4978],
      zoom: 10,
      osmData: false,
      bufferDistance: 1,
      bufferUnits: "kilometers",
      bufferUnitsOptions: ["kilometers", "miles"],
    };
  },
  computed: {
    buffers: function () {
      if (this.osmData) {
        const buffers = buffer(
          this.osmData, 
          this.bufferDistance, 
          {
            units: this.bufferUnits,
          }
        );

        return buffers;
      }

      return false;
    },
    union: function () {
      if (this.buffers) {
        const bufferPolygons = this.buffers.features.map(function (buffer) {
          return buffer.geometry.coordinates;
        });
        
        const union = polygonClipping.union(...bufferPolygons)

        return union;
      }

      return false;
    }
  },
  mounted() {
    axios.get("http://localhost:8000/openstreetmap/data").then((response) => {
      this.osmData = response.data;
    });
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