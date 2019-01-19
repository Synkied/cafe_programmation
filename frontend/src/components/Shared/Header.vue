<!-- Header file, used to define the navbar -->
<!--  Quentin Lathiere - synkx@hotmail.fr -->

<template>
  <div id="header">
    <b-navbar toggleable="md" type="light" class="white-bg" fixed="top">

      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

      <b-navbar-brand href="#home">
        <a class="navbar-brand js-scroll-trigger" href="#home" v-smooth-scroll="{ duration: 1000, offset: -50}">
          <img id="nav-logo" src="../../assets/cafe_logo_solo.svg" alt="Café logo">
        </a>
      </b-navbar-brand>

      <b-collapse is-nav id="nav_collapse">

        <ul id="menu">
          <b-navbar-nav>
            <li data-menuanchor="intentions"><a href="#intentions">Intentions</a></li>
          </b-navbar-nav>
          <b-navbar-nav>
            <li data-menuanchor="realisations"><a href="#realisations">Réalisations</a></li>
          </b-navbar-nav>
          <b-navbar-nav>
            <li data-menuanchor="contact" class="active"><a href="#contact">Contact</a></li>
          </b-navbar-nav>
        </ul>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Header',
  components: {
  }
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Noto+Sans');
  .logo_txt {
    font-family: 'Noto Sans', sans-serif;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: -10px;
    text-align: right;
  }
  #header {
    background-color: #fff;
  }
</style>
