<template>
  <div class="DatePickerComponent">
    <div class="datePicker">
      <h1 class="label level-left">{{labelName}}</h1>
        <Datepicker :placeholder="placeHolder" />
    </div>
  </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker';

export default {
  name: 'LabelComponent',
  components: {
    Datepicker
  },
  props: {
    labelName: {
      default: '',
      type: String,
    },
    placeHolder: {
      default: 'Select Date',
      type: String,
    },
  },
  data() {
    return {
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!--<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style> -->
