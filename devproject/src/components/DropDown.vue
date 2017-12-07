<template>
  <div class="DropDownComponent">
    <h1 class="label level-left">{{labelName}}</h1>
    <div class="control">
      <div class="select">
        <select>
          <option v-for="option in options" :key="option.id">{{option}}</option>
        </select>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'LabelComponent',
  props: {
    labelName: {
      default: '',
      type: String,
    },
    placeHolder: {
      default: '',
      type: String,
    },
    typeOfInput: {
      default: 'text',
      type: String,
    },
  },
  data() {
    return {
      options: [
        'red',
        'blue',
        'orange',
      ],
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
