<template>
  <div id="app">
    <app-header></app-header>
    <router-view/>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from './components/Shared/Header.vue'
import Footer from './components/Shared/Footer.vue'

export default {
  name: 'App',
  components: {
    'app-header': Header,
    'app-footer': Footer
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Avenir');
@import url('https://fonts.googleapis.com/css?family=Oswald');
@import url('https://fonts.googleapis.com/css?family=Cabin');
@import url('https://fonts.googleapis.com/css?family=Open+Sans');

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #fff;
}

.container {
  max-width: 100% !important;
}

section {
  min-height: 100%;
  padding: 4rem;
}

.card {
  border: 0 !important;
}

.card-img-top {
  width: 100% !important;
  height: 26vw !important;
  object-fit: cover !important;
  border-radius: 0 !important;
}

.card-body {
  text-align: left !important;
  background-color: #fff !important;
}

.card-body ul {
  margin: 15px 35px !important;
}

a {
  text-decoration: none;
  color: #30415d ! important;
}

a:hover {
  text-decoration: none;
}

.navbar {
  color: #000;
}

nav a, nav a:hover, nav a:active{
  color: #000;
}

.skill-img {
  height: 50px;
}

h1{
  text-align: center;
  font-family: 'Cabin', sans-serif;
  font-weight: bold;
  font-size: 2.5rem;
  text-transform: uppercase;
  color: #fff;
}

h2 {
  font-family: 'Cabin', sans-serif;
  font-size: 2rem;
  font-weight: 700;
}

h3 small {
  font-size: 60%;
  color: #6f6f6f;
  line-height: 0;
}

.ns-li {
  list-style-type: none;
  font-weight: 500;
  text-align: left;
}

.ns-li a {
  text-decoration: none;
  font-weight: 600;
}

.ns-li a:hover {
  color: #0e5c59;
  text-decoration: none;
}

.ns-li p {
  font-family: 'Avenir', sans-serif;
  font-size: 1rem;
}

.ns-li .pad {
  padding: 0 1.5rem;
}

ul {
  padding: 0;
}

.no-pad {
  padding: 0 !important;
}

.hr {
  border-top: 4px solid #000;
  width: 5%;
  margin: -10px 0 20px 0;
}

@media all and (max-width: 1200px) {
  .img-wrapper {
    overflow: hidden;
    max-height: 250px;
  }
}

@media all and (max-width: 900px) {
  .img-wrapper {
    overflow: hidden;
    max-height: 190px;
  }
}

</style>
