<template>
  <div class='FormView'>
   <LabelComponent typeOfInput='email'/>
   <DatePicker/>
   <DropDownComponent/>
  </div>
</template>

<script>
import LabelComponent from './components/Label';
import DatePicker from './components/DatePicker'
import DropDownComponent from './components/DropDown'

import axios from './axios'

export default {
  name: 'FormView',
  components: {
    LabelComponent,
    DatePicker,
    DropDownComponent,
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
    };
  },
  created: function() {
    axios.get('/singlerisk')
    .then((res)=> {
      console.log(JSON.stringify(res));
    })
    .catch((err)=> {
      console.log(err);
    })
  }
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
