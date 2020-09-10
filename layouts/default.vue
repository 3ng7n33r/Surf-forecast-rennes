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
import ogImage from '@/static/SBScreenshot.png'

export default {
  head() {
    return {
      meta: [
        {
          hid: 'og:image',
          property: 'og:image',
          content: this.BASE_URL + ogImage,
        },
      ],
    }
  },

  components: {
    NavBar,
    MainFooter,
  },
}
</script>

<style scoped></style>
