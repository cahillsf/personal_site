<template>
 <div>
</div>
</template>

<script>

export default {
  name: 'RouterMethods',
  data () {
    return {
    }
  },
  methods: {
    navigateToPage(route) {
        this.$router.push({ path: route });
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
