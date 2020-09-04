<template>
  <v-card height="150">
    <v-footer absolute class="font-weight-medium">
      <v-row>
        <v-col class="text-center">
          <div>
            {{ new Date().getFullYear() }} —
            <strong>Surf Forecast Rennes</strong>
          </div>
        </v-col>
        <v-spacer></v-spacer>
        <v-col>
          <img src="~assets/emailIcon.svg" />
        </v-col>
      </v-row>
    </v-footer>
  </v-card>
</template>
