<template>
  <v-container>
    <div>
      <v-row justify="center">
        <v-spacer></v-spacer>
        <v-column>
          <h1>Guidel - Plage des Kaolins</h1>
        </v-column>
        <v-spacer></v-spacer>
      </v-row>
    </div>
    <v-row justify="center">
      <v-spacer></v-spacer>
      <v-column>
        <h1>{{ weatherData[0].date }}</h1>
      </v-column>
      <v-spacer></v-spacer>
    </v-row>
    <v-divider></v-divider>
    <v-row justify="center">
      <v-col>
        <v-card-text class="text-md-center">
          <h2>Waves</h2>
        </v-card-text>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card outlined color="#66BB6A">
          <v-card-title>Height</v-card-title>
          <v-card-text>{{ weatherData[0].waveHeight }} m</v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card outlined color="#66BB6A">
          <v-card-title>Frequency</v-card-title>
          <v-card-text>{{ weatherData[0].wavePeriod }} s</v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card outlined color="#78909C">
          <v-card-title>Direction</v-card-title>
          <v-card-text>{{ weatherData[0].waveDirection }} °</v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-divider></v-divider>
    <v-row justify="center">
      <v-col>
        <v-card-text class="text-md-center">
          <h2>Wind</h2>
        </v-card-text>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card outlined color="#78909C">
          <v-card-title>Speed</v-card-title>
          <v-card-text>{{ weatherData[0].windSpeed }} km/h</v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card outlined color="#78909C">
          <v-card-title>Direction</v-card-title>
          <v-card-text>{{ weatherData[0].windDirection }} °</v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-divider></v-divider>
    <v-row justify="center">
      <v-col>
        <v-card-text class="text-md-center">
          <h2>Weather</h2>
        </v-card-text>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card outlined color="#78909C">
          <v-card-title>Air Temperature</v-card-title>
          <v-card-text>{{ weatherData[0].airTemperature }} °</v-card-text>
        </v-card>
      </v-col>

      <v-col>
        <v-card outlined color="#78909C">
          <v-card-title>Water Temperature</v-card-title>
          <v-card-text>{{ weatherData[0].waterTemperature }} °</v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <!--         :key="`${temp.date}-${temp.hour}-card`" -->
  </v-container>
</template>

<script>
export default {
  data() {
    const json = require('~/static/data.json')

    return {
      weatherData: json,

      colorCode: [
        {
          good: '#66BB6A',
          average: '#F4FF81',
          bad: '#EF9A9A',
        },
      ],
    }
  },
}
</script>

<style scoped></style>
