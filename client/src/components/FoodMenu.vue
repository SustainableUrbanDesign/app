<template>
  <div>
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
</template>