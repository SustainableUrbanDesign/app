<template>
  <q-layout view="hHh lpr fFf">
    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg" />
          </q-avatar>
          <span>Sustainable Urban Design App</span>
        </q-toolbar-title>

        <q-btn dense flat round icon="menu" @click="right = !right" />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="drawer"
      show-if-above
      :mini="miniState"
      @mouseover="miniState = false"
      @mouseout="miniState = true"
      mini-to-overlay
      :width="200"
      :breakpoint="500"
      bordered
      content-class="bg-grey-3"
    >
      <q-scroll-area class="fit">
        <q-list padding>
          <q-item active clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="eco" />
            </q-item-section>

            <q-item-section>Environment</q-item-section>
          </q-item>

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="dashboard" />
            </q-item-section>

            <q-item-section>Land use</q-item-section>
          </q-item>

          <q-item active clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="home" />
            </q-item-section>

            <q-item-section>Housing</q-item-section>
          </q-item>

          <q-item active clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="shopping_cart" />
            </q-item-section>

            <q-item-section>Food</q-item-section>
          </q-item>

          <q-separator />

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="commute" />
            </q-item-section>

            <q-item-section>Transportation</q-item-section>
          </q-item>

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="delete" />
            </q-item-section>

            <q-item-section>Utilities</q-item-section>
          </q-item>

          <q-separator />

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="accessibility_new" />
            </q-item-section>

            <q-item-section>Health</q-item-section>
          </q-item>

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="warning" />
            </q-item-section>

            <q-item-section>Safety</q-item-section>
          </q-item>

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="school" />
            </q-item-section>

            <q-item-section>Education</q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-drawer v-model="right" side="right" overlay behavior="desktop" bordered>
      <q-scroll-area class="fit">
        <q-list padding>
          <q-item v-ripple>
            <q-item-section avatar>
              <q-icon name="build" />
            </q-item-section>

            <q-item-section>Inspector</q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg" />
          </q-avatar>
          <span>Sustainable Urban Design App</span>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script>
export default {
  data() {
    return {
      right: false,
      miniState: true
    };
  }
};
</script>