<template>
  <v-card color="grey lighten-4" flat height="200px" tile>
    <v-toolbar dense>
      <v-toolbar-title>Surf</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon to="/">
        <v-icon>mdi-home</v-icon>
      </v-btn>

      <v-btn text>
        <n-link n-link to="/about"> About </n-link>
      </v-btn>
    </v-toolbar>
  </v-card>
</template>
