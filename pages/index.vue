<template>
  <!--   <v-container
    :style="{
      backgroundImage: 'url(' + require('@/static/Background_sunset.jpg') + ')',
    }"
  > -->
  <v-container>
    <div>
      <v-row justify="center">
        <v-spacer></v-spacer>
        <v-column>
          <h1>Guidel - Plage des Kaolins</h1>
        </v-column>
        <v-spacer></v-spacer>
      </v-row>

      <v-row justify="center">
        <v-spacer></v-spacer>
        <v-column>
          <h1>{{ weatherData[toggle_one].date }}</h1>
        </v-column>
        <v-spacer></v-spacer>
      </v-row>
      <v-row class="center" justify="center">
        <v-btn-toggle v-model="toggle_one" mandatory>
          <div
            v-for="daytime in dayTime"
            :key="daytime.time"
            class="buttonspace"
          >
            <v-btn v-bind="size">{{ daytime.time }}</v-btn>
          </div>
        </v-btn-toggle>
      </v-row>
    </div>

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
        <v-card
          outlined
          min-width="145px"
          :style="{ backgroundColor: cCodeWaveHeight }"
        >
          <v-card-title>Height</v-card-title>
          <v-card-text>{{ weatherData[toggle_one].waveHeight }} m</v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card
          outlined
          min-width="145px"
          :style="{ backgroundColor: cCodeWaveFreq }"
        >
          <v-card-title>Frequency</v-card-title>
          <v-card-text>{{ weatherData[toggle_one].wavePeriod }} s</v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card
          outlined
          min-width="145px"
          :style="{ backgroundColor: cCodeWaveDir }"
        >
          <v-card-title>Direction</v-card-title>
          <v-card-text
            >{{ weatherData[toggle_one].waveDirection }} °</v-card-text
          >
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
        <v-card
          outlined
          min-width="135px"
          :style="{ backgroundColor: cCodeWindSpeed }"
        >
          <v-card-title>Speed</v-card-title>
          <v-card-text
            >{{ weatherData[toggle_one].windSpeed }} km/h</v-card-text
          >
        </v-card>
      </v-col>
      <v-col>
        <v-card
          outlined
          min-width="135px"
          :style="{ backgroundColor: cCodeWindDir }"
        >
          <v-card-title>Direction</v-card-title>
          <v-card-text
            >{{ weatherData[toggle_one].windDirection }} °</v-card-text
          >
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
        <v-card
          outlined
          min-width="240px"
          :style="{ backgroundColor: cCodeAirTemp }"
        >
          <v-card-title>Air Temperature</v-card-title>
          <v-card-text
            >{{ weatherData[toggle_one].airTemperature }} °</v-card-text
          >
        </v-card>
      </v-col>

      <v-col>
        <v-card
          outlined
          min-width="240px"
          :style="{ backgroundColor: cCodeWaterTemp }"
        >
          <v-card-title>Water Temperature</v-card-title>
          <v-card-text
            >{{ weatherData[toggle_one].waterTemperature }} °</v-card-text
          >
        </v-card>
      </v-col>
    </v-row>
    <!--         :key="`${temp.date}-${temp.hour}-card`" -->
  </v-container>
</template>

<script>
export default {
  data() {
    const json = require('~/py_scripts/data.json')

    return {
      toggle_one: 0,

      dayTime: [
        {
          time: '09:00',
          action: 0,
        },
        {
          time: '12:00',
          action: 1,
        },
        {
          time: '15:00',
          action: 2,
        },
        {
          time: '18:00',
          action: 3,
        },
        {
          time: '21:00',
          action: 4,
        },
      ],

      weatherData: json,

      BGColor: '#E3F2FD',
      BGColorHead: '#BBDEFB',

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
  computed: {
    size() {
      const size = { xs: 'x-small', sm: 'small', lg: 'large', xl: 'x-large' }[
        this.$vuetify.breakpoint.name
      ]
      return size ? { [size]: true } : {}
    },
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

<style lang="scss" scoped>
h1 {
  height: 90%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.buttonspace {
  padding: 5px;
  align-items: center;
}
.center {
  justify-content: center;
}
</style>
