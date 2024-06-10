<template>
 <div>
    {{ count }}

    <button @click="add">add</button>
    <ul>
      
      <li v-for="todo in doneTodos" :key="todo.id">
        {{ todo.text }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState,mapGetters } from 'vuex';
export default {
  name: 'HelloWorld',
  methods: {
    add(){
      this.$store.commit("increment")
    }
  },
  computed: {
    ...mapState([
      'count','todos'
    ]),
    ...mapGetters([
      'doneTodos'
    ])
  },
 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
