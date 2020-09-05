<template>
  <v-container>
    <div>
      <v-row justify="center">
        <v-spacer></v-spacer>
        <v-column>
          <h1>About</h1>
        </v-column>
        <v-spacer></v-spacer>
      </v-row>
      <v-divider></v-divider>

      <v-row justify="center">
        <v-spacer></v-spacer>
        <v-column>
          <h1>What is this?</h1>
          <p>
            Primarily, this is a portfolio piece. I'm a former mechanical
            engineer that for multiple reasons decided to switch careers. So to
            get a bit of practice, I needed to find a project. A surf forecast
            website ticked all the boxes for me:
          </p>
          <div class="center">
            <ul>
              <li>Data acquisition using API</li>
              <li>Data handling using Python and Pandas</li>
              <li>
                Building a website using a framework (Vue and Nuxt in this case)
              </li>
              <li>
                As a surfer, I wanted to make something I'd actually want to use
              </li>
            </ul>
          </div>
        </v-column>
        <v-spacer></v-spacer>
      </v-row>

      <v-row justify="center">
        <v-spacer></v-spacer>
        <v-column>
          <h1>So who are you?</h1>
          <p>
            I'm Max. I was born and raised in Germany and have recently moved to
            Rennes in France. If you'd like to find out more just visit my
            <a href="https://3ng7n33r.github.io/">Portfolio</a> or my
            <a href="https://www.linkedin.com/in/maximilian-blacher/"
              >LinkedIn</a
            >
            page. I'd also be happy to hear from you directly. Just contact me
            by
            <a href="mailto:3ng7n33r@mail.fr">mail</a>
          </p>
        </v-column>
        <v-spacer></v-spacer>
      </v-row>

      <v-row justify="center">
        <v-spacer></v-spacer>
        <v-column>
          <h1>Privacy Policy</h1>
          <p>
            I will not collect or store any of your data. I have no use for it.
            There are no ads or tracking on this website.
          </p>
        </v-column>
        <v-spacer></v-spacer>
      </v-row>

      <v-row justify="center">
        <v-spacer></v-spacer>
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
        <v-spacer></v-spacer>
      </v-row>
    </div>
  </v-container>
</template>

<script>
export default {}
</script>

<style scoped>
h1 {
  padding: 30px 0 30px 0;
}

img {
  padding: 30px;
}

v-column {
  width: 50vw;
}

ul {
  display: inline-block;
  text-align: left;
}

p {
  line-height: 150%;
  font: 1.2em;
}

.center {
  margin: auto;
  width: 80%;
  padding: 10px;
}
</style>
