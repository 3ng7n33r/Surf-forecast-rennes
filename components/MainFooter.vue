<template>
  <v-card height="150">
    <v-footer absolute class="font-weight-medium">
      <v-row>
        <v-col class="text-center">
          <div>
            {{ new Date().getFullYear() }} —
            <strong>Surf-Bretagne</strong>
          </div>
        </v-col>
        <v-spacer></v-spacer>
        <v-col>
          <a href="mailto:3ng7n33r@mail.fr">
            <img src="~assets/emailIcon.svg" />
          </a>
          <a href="https://www.linkedin.com/in/maximilian-blacher/">
            <img src="~assets/linkedIcon.svg" />
          </a>
          <a href="https://github.com/3ng7n33r">
            <img src="~assets/gitHubIcon.svg" />
          </a>
          <a href="https://3ng7n33r.github.io/">
            <img src="~assets/portfolioIcon.svg" />
          </a>
        </v-col>
      </v-row>
    </v-footer>
  </v-card>
</template>

<style scoped>
img {
  padding: 0 30px 0 30px;
}
</style>
