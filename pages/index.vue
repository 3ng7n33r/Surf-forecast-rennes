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
        <v-card outlined :style="{ backgroundColor: cCodeWaveHeight }">
          <v-card-title>Height</v-card-title>
          <v-card-text>{{ weatherData[0].waveHeight }} m</v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card outlined :style="{ backgroundColor: cCodeWaveFreq }">
          <v-card-title>Frequency</v-card-title>
          <v-card-text>{{ weatherData[0].wavePeriod }} s</v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card outlined :style="{ backgroundColor: cCodeWaveDir }">
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
        <v-card outlined :style="{ backgroundColor: cCodeWindSpeed }">
          <v-card-title>Speed</v-card-title>
          <v-card-text>{{ weatherData[0].windSpeed }} km/h</v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card outlined :style="{ backgroundColor: cCodeWindDir }">
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
        <v-card outlined :style="{ backgroundColor: cCodeAirTemp }">
          <v-card-title>Air Temperature</v-card-title>
          <v-card-text>{{ weatherData[0].airTemperature }} °</v-card-text>
        </v-card>
      </v-col>

      <v-col>
        <v-card outlined :style="{ backgroundColor: cCodeWaterTemp }">
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

      cCodeWaveHeight: '#E0E0E0',
      cCodeWaveFreq: '#E0E0E0',
      cCodeWaveDir: '#E0E0E0',
      cCodeWindSpeed: '#E0E0E0',
      cCodeWindDir: '#E0E0E0',
      cCodeAirTemp: '#E0E0E0',
      cCodeWaterTemp: '#E0E0E0',

      cCode: {
        good: '#66BB6A',
        average: '#F4FF81',
        bad: '#EF9A9A',
      },
    }
  },

  mounted() {
    if (0.6 <= this.weatherData[0].waveHeight) {
      this.cCodeWaveHeight = this.cCode.good
    } else if (0.3 < this.weatherData[0].waveHeight) {
      this.cCodeWaveHeight = this.cCode.average
    } else {
      this.cCodeWaveHeight = this.cCode.bad
    }

    if (10 <= this.weatherData[0].wavePeriod) {
      this.cCodeWaveFreq = this.cCode.good
    } else if (6 < this.weatherData[0].wavePeriod) {
      this.cCodeWaveFreq = this.cCode.average
    } else {
      this.cCodeWaveFreq = this.cCode.bad
    }

    if (15 <= this.weatherData[0].waveDirection) {
      this.cCodeWaveDir = this.cCode.good
    } else if (10 < this.weatherData[0].waveDirection) {
      this.cCodeWaveDir = this.cCode.average
    } else {
      this.cCodeWaveDir = this.cCode.bad
    }

    if (this.weatherData[0].windSpeed <= 10) {
      this.cCodeWindSpeed = this.cCode.good
    } else if (this.weatherData[0].windSpeed < 20) {
      this.cCodeWindSpeed = this.cCode.average
    } else {
      this.cCodeWindSpeed = this.cCode.bad
    }

    if (15 <= this.weatherData[0].cCodeWindDir) {
      this.cCodeWindDir = this.cCode.good
    } else if (10 < this.weatherData[0].cCodeWindDir) {
      this.cCodeWindDir = this.cCode.average
    } else {
      this.cCodeWindDir = this.cCode.bad
    }

    if (18 <= this.weatherData[0].airTemperature) {
      this.cCodeAirTemp = this.cCode.good
    } else if (12 < this.weatherData[0].airTemperature) {
      this.cCodeAirTemp = this.cCode.average
    } else {
      this.cCodeAirTemp = this.cCode.bad
    }

    if (15 <= this.weatherData[0].waterTemperature) {
      this.cCodeWaterTemp = this.cCode.good
    } else if (10 < this.weatherData[0].waterTemperature) {
      this.cCodeWaterTemp = this.cCode.average
    } else {
      this.cCodeWaterTemp = this.cCode.bad
    }
  },
}
</script>

<style scoped></style>
