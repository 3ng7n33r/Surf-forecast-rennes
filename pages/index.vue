<template>
  <div class="container">
    <h2>This is a Homepage</h2>
  </div>
</template>

<script>
export default {
  head() {
    return {
    title: "Surf forecast",
    meta: [
      {hid: "description", name: "description", content: "My content"},
      {hid: "ogtitle", property: "og:title", content: "Blablabla"}
    ]
    }
  }
}
</script>

<style>
.container {
  margin: 0 auto;
}
</style>
