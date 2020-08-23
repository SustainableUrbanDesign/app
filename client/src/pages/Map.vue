<template>
  <q-page class="flex">
    <div>
      <div class="row">
        <vl-map
          :load-tiles-while-animating="true"
          :load-tiles-while-interacting="true"
          data-projection="EPSG:4326"
        >
          <vl-view :zoom.sync="zoom" :center.sync="center"></vl-view>

          <vl-layer-tile id="osm">
            <vl-source-osm></vl-source-osm>
          </vl-layer-tile>

          <div v-if="osmData">
            <vl-layer-vector v-if="osmData.features">
              <vl-source-vector :features="osmData.features"></vl-source-vector>

              <vl-style-box>
                <vl-style-circle :radius="5">
                  <vl-style-fill color="green"></vl-style-fill>
                  <vl-style-stroke color="white"></vl-style-stroke>
                </vl-style-circle>
              </vl-style-box>
            </vl-layer-vector>
          </div>

          <vl-feature v-if="union">
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
const polygonClipping = require("polygon-clipping");
import Vue from "vue";

import VueLayers from "vuelayers";
import "vuelayers/lib/style.css";

Vue.use(VueLayers);

export default {
  name: "MapIndex",
  data() {
    return {
      center: [23.761, 61.4978],
      zoom: 10,
      osmData: undefined,
      bufferUnitsOptions: ["kilometers", "miles"],
    };
  },
  computed: {
    bufferDistance() {
      return this.$store.state.food.bufferDistance;
    },
    bufferUnits() {
      return this.$store.state.food.bufferUnits;
    },
    buffers: function () {
      if (this.osmData != undefined) {
        const buffers = buffer(this.osmData, this.bufferDistance, {
          units: this.bufferUnits,
        });

        return buffers;
      }

      return undefined;
    },
    union: function () {
      if (this.buffers != undefined) {
        const bufferPolygons = this.buffers.features.map(function (buffer) {
          return buffer.geometry.coordinates;
        });

        const union = polygonClipping.union(...bufferPolygons);

        return union;
      }

      return undefined;
    },
  },
  mounted() {
    axios.get("http://localhost:8000/openstreetmap/data").then((response) => {
      if (response.data != undefined) {
        this.osmData = response.data;
      }
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
