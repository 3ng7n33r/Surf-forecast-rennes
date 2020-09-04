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
      <v-divider></v-divider>
    </div>
    <v-row justify="center">
      <v-spacer></v-spacer>
      <v-column>
        <h1>04.09.2020 12:07</h1>
      </v-column>
      <v-spacer></v-spacer>
    </v-row>
    <v-row justify="center">
      <v-col>
        <v-card-text class="text-md-center">
          <h2>Waves</h2>
        </v-card-text>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-for="wave in Waves" :key="`${wave.label}-card`">
        <v-card outlined color="#78909C">
          <v-card-title>{{ wave.label }}</v-card-title>
          <v-card-text>{{ wave.dim }}</v-card-text>
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
      <v-col v-for="wind in Wind" :key="`${wind.label}-card`">
        <v-card outlined color="#78909C">
          <v-card-title>{{ wind.label }}</v-card-title>
          <v-card-text>{{ wind.dim }}</v-card-text>
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
      <v-col v-for="weather in Weather" :key="`${weather.label}-card`">
        <v-card outlined color="#78909C">
          <v-card-title>{{ weather.label }}</v-card-title>
          <v-card-text>{{ weather.dim }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!--       <v-row>
        <div>
          <div
            v-for="(data, index) in $options.myJson"
            :key="`${index}-weather`"
          >
            date: {{ data.date }} hour: {{ data.hour }}
          </div>
        </div>
    </v-row>-->
  </v-container>
</template>

<script>
// const getTides = () => import('~/static/tides.json').then((m) => m.default || m)
import MY_JSON from '~/static/data.json'

export default {
  /*   async asyncData({ req }) {
    const tides = await getTides()

    return { tides }
  }, */
  myJson: MY_JSON,

  data() {
    return {
      Waves: [
        {
          label: 'Height',
          dim: '0,2 m',
        },
        {
          label: 'Frequency',
          dim: '10 s',
        },
        {
          label: 'Direction',
          dim: '272°',
        },
      ],
      Wind: [
        {
          label: 'Strength',
          dim: '10 km/h',
        },
        {
          label: 'Direction',
          dim: '272°',
        },
      ],
      Weather: [
        {
          label: 'Air Temperature',
          dim: '18°C',
        },
        {
          label: 'Water Temperature',
          dim: '12°C',
        },
        {
          label: 'Tide',
          dim: 'Receding Low tide at 15:32',
        },
        {
          label: 'Sky',
          dim: 'Sunny',
        },
      ],
    }
  },
}
</script>

<style scoped></style>
