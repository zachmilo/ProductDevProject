<template>
  <div id="app">
    <FormComponent/>
  </div>
</template>

<script>
import FormComponent from './FormView';

export default {
  name: 'app',
  components: {
    FormComponent,
  },
};
</script>

<!--<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style> -->
