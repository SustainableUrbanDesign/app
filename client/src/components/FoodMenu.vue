<template>
  <div>
    <q-input label="Buffer distance" v-model.number="bufferDistance" type="number" :dense="false" />

    <q-select
      v-model="bufferUnits"
      :options="bufferUnitsOptions"
      label="Units"
      stack-label
      :dense="false"
      :options-dense="false"
    />
  </div>
</template>

<script>
export default {
  name: "FoodMenu",
  data() {
    return {
      bufferUnitsOptions: ["kilometers", "miles"],
    };
  },
  computed: {
    bufferDistance: {
      get() {
        return this.$store.state.food.bufferDistance;
      },
      set(distance) {
        this.$store.commit("food/setBufferDistance", distance);
      },
    },
    bufferUnits: {
      get() {
        return this.$store.state.food.bufferUnits;
      },
      set(units) {
        this.$store.commit("food/setBufferUnits", units);
      },
    },
  },
};
</script>
