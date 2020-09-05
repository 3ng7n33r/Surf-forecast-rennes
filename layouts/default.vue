<template>
  <div>
    <NavBar />
    <nuxt />
    <MainFooter />
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import MainFooter from '@/components/MainFooter.vue'

export default {
  components: {
    NavBar,
    MainFooter,
  },
}
</script>

<style scoped></style>
