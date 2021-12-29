<template>
 <div class="singleColGrid">
    <router-methods ref="routerMethods"></router-methods>
    <top-toolbar></top-toolbar>
    <h1>Three.js Example</h1>
    <p>This is a page I put together while exploring the three.js library.  
        I modeled the tooth using Meshmixer, a very cool free 3-D modeling software, then loaded it as a object into my Three scene.  
        Just click the front tooth to add another row of teeth to this floating phalanx!  </p>
    <div class="bigtoothdiv">
      <div id="imgdiv">
          <a @click="$refs.routerMethods.navigateToPage('/threescene')" id="bigtootha" target="_blank">
              <img src="@/assets/texttooth.png" id="bigtooth" alt="big tooth"/>
          </a>
      </div>
    </div>
    <!-- <div id="spacer"></div> -->
    <bottom-bar class="bottomBarProps"></bottom-bar>
  </div>
  
    
</template>

<script>
import RouterMethods from '../components/RouterMethods.vue';
import TopToolbar from '../components/TopToolbar.vue';
import BottomBar from '../components/BottomBar.vue';
export default {
  name: 'ToothPage',
  components: {
    TopToolbar,
    BottomBar,
    RouterMethods
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
    }
  },
  methods: {
    doSomething() {
      this.msg= 'another page hahahahahahahaha!';
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.bottomBarProps {
    grid-column: 1;
    background-image: linear-gradient(to top, #c4d4e0 0%,#6e9db3 100%);
    /* grid-column: 1 / 3; */
    display: grid;
}

.bigtoothdiv{
	text-align: center;
	display: grid;
	grid-template-columns: 1fr 1fr 1fr;
}

#bigtooth{
	position: relative;
	text-align: center;
	width: 100%;  
	margin-top: 0;
}

#imgdiv{
	grid-column: 2/3;
}

/* #spacer{
  grid-row: 4;
  height: 5vh;
} */

</style>
