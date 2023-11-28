<template>
  <div id="app">

    <nav class="navbar bg-body-tertiary">
      <form class="container-fluid justify-content-start">
        <button class="btn btn-outline-success me-2" type="button"><router-link to="/">Go Table</router-link></button>
        <button class="btn btn-sm btn-outline-secondary" type="button"><router-link to="/Ping">Ping</router-link></button>
      </form>
    </nav>

    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ba8585;
}
</style>
