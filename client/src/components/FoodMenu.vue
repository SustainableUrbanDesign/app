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
      bufferDistance: 1,
      bufferUnits: "kilometers",
      bufferUnitsOptions: ["kilometers", "miles"],
    };
  },
};
</script>
