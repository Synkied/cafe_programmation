<template>
  <div id="app">
    <v-app>
      <app-header></app-header>
      <router-view/>
    </v-app>
  </div>
</template>

<script>
import Header from './components/Shared/Header.vue'
import Footer from './components/Shared/Footer.vue'

export default {
  name: 'App',
  components: {
    'app-header': Header
  }
}
</script>

<style>

/* *********** GENERAL *********** */

#app {
  font-family: AvantGardeGothicITCW02Md, Helvetica, Arial, sans-serif !important;
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

.list-inline-item.active {
  font-weight: 600;
  font-size: 1.5rem;
}

/* --- lists --- */

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
  width: 280px;
}

#nav-logo {
  width:80px;
}

.img-desc-project {
  position: absolute;
  top: -34px;
  left: 102%;
  min-width: 750px !important;
}

.img-project {
  width: 170px;
  height: 170px;
}

/* --- animations --- */

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.shiftx-enter-active {
  transition: all .6s ease-in-out;
}
.shiftx-leave-active {
    transition: all .1s ease-in-out;
}

.shiftx-enter, .shiftx-leave-to {
  transform:  translateX(-100px);
  opacity: 0;
}

.slide-fade-left-enter-active {
  transition: all 1s ease;
}
.slide-fade-left-leave-active {
  transition: all 2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-left-enter, .slide-fade-left-leave-to {
  transform: translateX(-150px);
  opacity: 0;
}

.slide-fade-right-enter-active {
  transition: all 1s ease;
}
.slide-fade-right-leave-active {
  transition: all 2s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-right-enter, .slide-fade-right-leave-to {
  transform: translateX(150px);
  opacity: 0;
}

/* --- decorations --- */

.container-fluid .row.row-home {
  margin: 0 0 0 300px;
}

.cafe-title {
  overflow: hidden;
  font-size: 1.4rem;
}

.cafe-sub-title {
  overflow: hidden;
  font-size: 2.05rem;
  margin: -15px 0;
}

.cafe-logo-line {
  position: absolute;
  top: 102px;
  left: 305px;
  width: 300px;
  border: 3px black solid;
}

/* --- buttons --- */

.btn-primary-outline {
  background-color: transparent;
  border-color: transparent !important;
}

/* --- navbar ----*/
#header .navbar-light .navbar-toggler {
  border-color: #fff !important;
}

.navbar-collapse {
  font-family: FuturaBT-CondMedium;
  font-size: 1.3rem;
  flex-basis: 0;
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

/* *********** PROJECTS *********** */

.section .container.projects-container {
  padding: 70px 10px;
}

/* --- expansion panels --- */

.row .v-expansion-panel__header {
  padding: 0;
  min-height: 35px;
}

.row .all-projects .v-expansion-panel__header {
  padding: 0 15px;
  min-height: 35px;
}

/*.row .all-projects.v-expansion-panel__container--active, .row .filtered-projects.v-expansion-panel__container--active {
  height: 170px;
}*/

.row .v-expansion-panel {
  -webkit-box-shadow: none;
  box-shadow: none;
}

.v-card__text.card-text {
  padding: 0 0 10px 0;
}

.all-projects .v-card__text.card-text {
  padding: 0 15px;
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

/* *********** FOOTER *********** */

footer a {
  color: #000;
  text-decoration: none;
}

footer a:hover {
  color: #17252A;
  text-decoration: none;
}

.footer {
  border-top: 1px solid #000;
  height: 50px;
  display: block;
  width: 100%;
  z-index: 9;
  margin: 150px auto auto auto;
  padding: 10px 0 0 0;
  max-width: 80%;
}

.footer-text {
  color: #000;
  background: #fff;
  text-align: center;
  font-size: 1.2rem;
}

.fixed-elem-wrap {
  position: relative;
  height: 0;
}

.back-to-top {
  position: absolute;
  z-index: 500;
  top: 0;
  left: -160px;
  transition: top 0.5s cubic-bezier(0, 1.4, 1, 1);
}

/* *********** MEDIA QUERIES *********** */

@media all and (max-width: 1904px) {
  .img-desc-project {
    min-width: 600px !important;
  }
  .back-to-top {
    position: absolute;
    z-index: 500;
    top: 0;
    left: -120px;
    transition: top 0.5s cubic-bezier(0, 1.4, 1, 1);
  }
}

@media all and (max-width: 1400px) {

  .footer {
    border-top: 1px solid #000;
    height: 50px;
    display: block;
    width: 100%;
    z-index: 9;
    margin: auto;
    margin-top: 150px;
    padding: 10px 0 0 0;
    max-width: 80%;
  }

  .footer-text {
    color: #000;
    background: #fff;
    text-align: center;
    font-size: 1.2rem;
  }

  .back-to-top {
    position: absolute;
    z-index: 500;
    top: 0;
    left: -100px;
    transition: top 0.5s cubic-bezier(0, 1.4, 1, 1);
  }

  .intentions {
    font-size: 1.1rem;
    font-weight: 500;
  }
}

@media all and (max-width: 1264px) {
  .img-desc-project {
    position: static;
  }
}

@media all and (max-width: 1200px) {
  .img-wrapper {
    overflow: hidden;
    max-height: 100%;
  }

  .container-fluid .row.row-home {
    margin: 0;
  }

  .logo-img {
    width: 250px;
  }

  .cafe-sub-title {
    overflow: hidden;
    font-size: 1.8rem;
    margin: -15px 0;
  }

  .cafe-logo-line {
    position: absolute;
    top: 91px;
    left: 280px;
    width: 250px;
    border: 3px black solid;
  }

  .search-terms {
    text-align: center;
  }

  .search-terms li {
    display: inline;
  }

  .intentions {
    font-size: 1.2rem;
    font-weight: 500;
  }

  .footer {
    border-top: 1px solid #000;
    height: 50px;
    display: block;
    width: 100%;
    z-index: 9;
    margin: auto;
    margin-top: 150px;
    padding: 10px 0 0 0;
    max-width: 100%;
  }

  .footer-text {
    color: #000;
    background: #fff;
    text-align: center;
    font-size: 1.05rem;
  }

  .back-to-top {
    position: absolute;
    width: 20px;
    top: 0;
    left:25px;
  }
}

@media all and (max-width: 900px) {
  .img-wrapper {
    overflow: hidden;
  }

  .container-fluid .row.row-home {
    margin: 0;
  }

  .logo-img {
    width: 150px;
  }

  .cafe-sub-title {
    overflow: hidden;
    font-size: 1.45rem;
    margin: -15px 0;
  }

  .cafe-logo-line {
    position: absolute;
    top: 54px;
    left: 180px;
    width: 250px;
    border: 2px black solid;
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

  .list-inline-item.active {
    font-weight: 600;
    font-size: 1.2rem;
  }


  .img-desc-project {
    position: static;
    min-width: 100%;
  }

  .intentions {
    font-size: 1rem;
    font-weight: 500;
  }

  p.intentions {
    margin: 0 0 5px 0;
  }

  .footer {
    border-top: 1px solid #000;
    height: 50px;
    display: block;
    width: 100%;
    z-index: 9;
    margin: auto;
    margin-top: 150px;
    padding: 10px 0 0 40px;
    max-width: 100%;
  }

  .footer-text {
    color: #000;
    background: #fff;
    text-align: center;
    font-size: 1.2rem;
  }

  .back-to-top {
    position: absolute;
    width: 20px;
    top: 0;
    left:-20px;
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

  .cafe-sub-title {
    overflow: hidden;
    font-size: 1.3rem;
    margin: -15px 0;
  }

  .cafe-logo-line {
    position: absolute;
    top: 54px;
    left: 180px;
    width: 210px;
    border: 2px black solid;
  }

  .intentions-title {
    overflow: hidden;
    font-size: 1rem;
  }

  p.intentions-title {
    margin: 0;
  }

  .intentions {
    font-size: 0.9rem;
    font-weight: 500;
  }

}

@media all and (max-width: 440px) {

  .cafe-sub-title {
    overflow: hidden;
    font-size: 1.2rem;
    margin: -15px 0;
  }

  .cafe-logo-line {
    position: absolute;
    top: 54px;
    left: 180px;
    width: 182px;
    border: 2px black solid;
  }

}

@media all and (max-width: 360px) {

  .cafe-sub-title {
    overflow: hidden;
    font-size: .9rem;
    margin: -15px 0;
  }

  .cafe-logo-line {
    position: absolute;
    top: 54px;
    left: 180px;
    width: 95px;
    border: 2px black solid;
  }

}

</style>
