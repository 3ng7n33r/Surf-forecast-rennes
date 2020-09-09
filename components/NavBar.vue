<template>
  <v-toolbar dense>
    <v-toolbar-title>Surf Forecast Rennes</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn
      v-for="link in links"
      :key="link.label"
      :to="link.url"
      class="pa-0"
      >{{ link.label }}</v-btn
    >
  </v-toolbar>
</template>

<script>
export default {
  data() {
    return {
      links: [
        {
          label: 'Home',
          url: '/',
        },
        {
          label: 'About',
          url: '/about',
        },
      ],
    }
  },
}
</script>

<style lang="scss" scoped></style>
