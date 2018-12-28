<template>
  <div id="app">
    <app-header></app-header>
    <app-footer></app-footer>
    <router-view/>
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
@import url('https://fonts.googleapis.com/css?family=Didact+Gothic');

@font-face {
  font-family: 'avant-garde-md';
  src: url('./assets/fonts/avantgarde_md_bt_tt0156m-webfont.woff2') format('woff2'),
       url('./assets/fonts/avantgarde_md_bt_tt0156m-webfont.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

/* *********** GENERAL *********** */

#app {
  font-family: 'Didact Gothic', Helvetica, Arial, sans-serif !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #fff;
}

.fp-tableCell {
  display: flex;
  align-items: center;
  justify-content: center;
}

#app a {
  text-decoration: none;
  color: #30415d;
}

#app a:hover {
  text-decoration: none;
}

#app .no-pad {
  padding: 0;
}

#app .hr-line {
  margin: 0;
  border-top: 1px solid #000;
}

.s-100 {
  height: 100vh;
}

.align-left {
  text-align: left;
}

.align-right {
  text-align: right;
}

.justif {
  text-align: justify;
}

.intentions {
  font-size: 1.25rem;
  font-weight: 600;
}

.white-bg {
  background-color: #fff;
}

.v-align-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.v-align-left-center {
  display: flex;
  align-items: center;
  justify-content: left;
}

::-webkit-scrollbar {
    width: 0.5em;
}

::-webkit-scrollbar-track {
    -webkit-box-shadow: none;
}

::-webkit-scrollbar-thumb {
  background-color: #000;
  outline: 1px solid slategrey;
}

.shallow-circle {
  border: 1px solid black;
  width: 10px;
  height: 10px;
  border-radius: 100%;
  margin: 0 3px 0 0;
}

.shallow-circle.active {
  border: 5px solid black;
  width: 10px;
  height: 10px;
  border-radius: 100%;
  margin: 0 3px 0 0;
}

/* --- lists --- */

.search-filter-item {
  display: flex;
  align-items: center;
  padding: 5px 0;
  font-weight: 600;
  font-size: 1.1rem;
}

#app ul {
  padding: 0;
}

.ns-li {
  list-style-type: none;
  font-weight: 500;
  text-align: center;
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
  font-family: 'Open Sans', sans-serif;
  font-size: 1rem;
}

.ns-li .pad {
  padding: 0 1.5rem;
}

/* --- imgs --- */

#app .skill-img {
  height: 50px;
}

.about-img {
  border-radius: 7%;
}

.logo-home {
  position: relative;
  text-align: right;
  top: 200;
  right: 350;
}

.logo-img {
  width: 38%;
}

#nav-logo {
  width:80px;
}

.img-desc-project {
  position: absolute;
  top: -34px;
  left: 102%;
  min-width: 570px;
}

.img-project {
  width: 200px;
}

.desc-project {
  position: absolute;
  top: -3px;
  left: 37%;
  font-size: 0.8rem;
  max-width: 300px;
  padding: 0 10px 0 0;
  overflow-y: visible;
}

/* --- decorations --- */

.intentions-title {
  overflow: hidden;
  font-size: 1.4rem;
}

.intentions-title:after {
  content:"";
  display: inline-block;
  height: 0.5em;
  vertical-align: bottom;
  width: 100%;
  margin-right: -100%;
  border-top: 1px solid black;
}

.intentions-title:before {
  content:"";
  display: inline-block;
  height: 0.5em;
  vertical-align: bottom;
  width: 100%;
  margin-left: -100%;
  border-top: 1px solid black;
}

.intention-word-left {
  margin: 0 10px 0 0;
}

.intention-word-center {
  margin: 0 10px;
}

.intention-word-right {
  margin: 0 0 0 10px;
}

/* --- buttons --- */

.btn-primary-outline {
  background-color: transparent;
  border-color: transparent !important;
}

/* *********** TITLES *********** */

#app h1{
  text-align: center;
  font-family: 'Cabin', sans-serif;
  font-weight: bold;
  font-size: 2.5rem;
  text-transform: uppercase;
  color: #fff;
  hyphens: auto;
}

#app h2 {
  font-family: 'Cabin', sans-serif;
  font-size: 2rem;
  font-weight: 700;
}

#app h3 small {
  font-size: 60%;
  color: #6f6f6f;
  line-height: 0;
}

.project-title {
  text-transform: uppercase;
  font-size: 1.1rem;
  font-weight: 800;
}

/* *********** PROJECTS *********** */

.project-row {
  text-align: left;
  padding: 0;
}

.project-row>ul {
  margin: 0;
}

.info-project {
  font-size: 0.9rem;
  max-width: 90%;
}

/* --- expansion panels --- */

.row .v-expansion-panel__header {
  padding: 0;
  min-height: 35px;
}

.row .all-projects .v-expansion-panel__header {
  padding: 0 15px !important;
  min-height: 35px;
}
.row .v-expansion-panel {
  -webkit-box-shadow: none;
  box-shadow: none;
}

.black-header {
  background-color: #000 !important;
  border-color: #000 !important;
  font-weight: 600;
  font-size: 1.1rem;
}

.v-card__text.card-text {
  padding: 0 0 10px 0 !important;
}

.all-projects .v-card__text.card-text {
  padding: 0 15px !important;
}

/* *********** BOOTSTRAP *********** */

#app .container {
  max-width: 100%;
}

#app section {
  min-height: 100%;
  padding: 4rem;
}

#app .navbar {
  color: #000;
}

#app nav a, nav a:hover, nav a:active{
  color: #000;
}

/* --- cards --- */

#app .card {
  border: 0 ;
}

#app .card-img-top {
  width: 100%;
  height: 26vw;
  object-fit: cover;
  border-radius: 0;
}

#app .card-body {
  text-align: left;
  background-color: #fff;
}

#app .card-body ul {
  margin: 15px 35px;
}

/* *********** MORE INFO *********** */

#app .more-info {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #138496;
  font-size: 0.75rem;
  padding: 15px;
  overflow: auto;
  color: #fff;
}

#app .btn-bottom-right {
  position: absolute;
  top: 0;
  right: 20px;
  border-radius: 0;
  width: 15px;
}

#app .btn-bottom-right:focus {
  box-shadow: none;
}

.search-terms {
  text-align: left;
  list-style-type: none;
}

.info-project p {
  margin: 0 0 6px 0;
}

.info-project p:last-child {
  margin: 0 0 15px 0;
}

/* *********** FOOTER *********** */

footer a {
  color: #000;
  text-decoration: none;
}

footer a:hover {
  color: #17252A;
  text-decoration: none;
}

footer {
  border-top: 1px solid #000;
  position: fixed;
  color: #000;
  background: #fff;
  height: 50px;
  display: block;
  width: 100%;
  z-index: 9;
  text-align: center;
  margin: auto;
  margin-top: 100px;
  padding: 10px 0 0 0;
  bottom: 0;
  font-size: 1.2rem;
}

footer .container{
  padding: 10px 0;
}

/* *********** MEDIA QUERIES *********** */

@media all and (max-width: 1400px) {
  .desc-project {
    position: absolute;
    top: -3px;
    left: 37%;
    font-size: 0.8rem;
    max-width: 200px;
    padding: 0 10px 0 0;
    overflow-y: visible;
  }

  .intentions {
    font-size: 1.1rem;
    font-weight: 600;
  }
}

@media all and (max-width: 1200px) {
  .img-wrapper {
    overflow: hidden;
    max-height: 100%;
  }
  .logo-img {
    width: 60%;
  }

  .img-desc-project {
    position: static;
  }

  .desc-project {
    position: static;
    min-width: 100%;
  }

  .search-terms {
    text-align: center;
  }

  .search-terms li {
    display: inline;
  }

  .intentions {
    font-size: 1.2rem;
    font-weight: 600;
  }

  footer {
    border-top: 1px solid #000;
    position: fixed;
    color: #000;
    background: #fff;
    height: 50px;
    display: block;
    width: 100%;
    z-index: 9;
    text-align: center;
    margin: auto;
    margin-top: 100px;
    padding: 5px 0 0 0;
    bottom: 0;
    font-size: 1.05rem;
  }
}

@media all and (max-width: 900px) {
  .img-wrapper {
    overflow: hidden;
  }

  .logo-img {
    width: 100%;
  }

  .logo-home {
    position: relative;
    text-align: right;
    top: 180;
    right: 0;
  }

  #app .more-info {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #138496;
    font-size: 0.75rem;
    padding: 15px;
    overflow: auto;
    color: #fff;
  }

  #app h1{
    font-size: 1.8rem;
  }

  #app section {
    min-height: 100%;
    padding: 4rem 1rem;
  }

  .img-desc-project {
    position: static;
    min-width: 100%;
  }

  .desc-project {
    position: static;
    width: 100%;
  }

  .intentions {
    font-size: 1.1rem;
    font-weight: 600;
  }

  p.intentions {
    margin: 0 0 5px 0;
  }

  footer {
    border-top: 1px solid #000;
    position: fixed;
    color: #000;
    background: #fff;
    height: 72px;
    display: block;
    width: 100%;
    z-index: 9;
    text-align: center;
    margin: auto;
    margin-top: 100px;
    padding: 5px 0 0 0;
    bottom: 0;
    font-size: 0.95rem;
  }
}

@media all and (max-width: 640px) {

  .btn-primary-outline {
    background-color: transparent;
    border-color: transparent !important;
  }

  #app .btn-bottom-right {
    position: absolute;
    top: 5px;
    right: 10px;
    border-radius: 0;
    width: 38px;
    font-size: 1.2rem;
  }

  .project-title {
    max-width: 80%;
    font-size: 0.9rem;
  }

  .intentions-title {
    overflow: hidden;
    font-size: 1.1rem;
  }

  p.intentions-title {
    margin: 0;
  }

  .intentions {
    font-size: 0.9rem;
    font-weight: 600;
  }

}

</style>
