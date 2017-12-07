<template>
  <div class="LabelComponent">
    <div class="field">
      <label class="label level-left">{{labelName}}</label>
      <div class="control has-icons-left has-icons-right">
        <input class="input is-success" :type="typeOfInput" :placeholder="placeHolder" value="">
        <span class="icon is-small is-left">
          <i class="fa fa-user"></i>
        </span>
        <span class="icon is-small is-right">
          <i class="fa fa-check"></i>
        </span>
      </div>
      <p class="help is-success">This username is available</p>
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
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<!--style scoped>
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
