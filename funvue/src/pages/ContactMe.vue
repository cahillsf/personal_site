<template>
 <div class="contactMeGrid">
    <top-toolbar></top-toolbar>
    <div class="header">
      <h1>Get In Touch</h1>
    </div>
    <div id="mainDiv">
        <div id="emailDiv" @click="sendEmail">
            <img id="emailImg" src="@/assets/mail-64.png"/>
            <h2>cahillsf9@gmail.com</h2>
            <img id="arrowImg" src="@/assets/arrow-28-32.png"/>
        </div>
        
        <h4>Or tell me a bit about yourself and send a message below:</h4>
        <form>
            <p>Email:</p>
            <input class="uk-textarea" type="text"  placeholder="Enter your email" v-model="email">
            <p>Name:</p>
            <input class="uk-textarea" type="text" placeholder="Enter your name" v-model="submitterName">
            <p>Message:</p>
            <input class="uk-textarea" type="text" placeholder="Enter your message" v-model="message">
        </form>
        <vk-button id="submitButton">Submit</vk-button>
    </div>
    <bottom-bar v-bind:style="bottomBarProps"></bottom-bar>
  </div>
  
    
</template>

<script>
import TopToolbar from '../components/TopToolbar.vue';
import BottomBar from '../components/BottomBar.vue';
import { Button } from '../../node_modules/vuikit/lib/button';
export default {
  name: 'ContactMe',
  components: {
    TopToolbar,
    BottomBar,
    VkButton: Button,
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      bottomBarProps: {
        'grid-column': '1/4',
        'background-image': 'linear-gradient(to top, #c4d4e0 0%,#6e9db3 100%)',
        'display': 'grid',
        'grid-row': 5,
      },
      email: '',
      submitterName: '',
      message: '',
    }
  },
  methods: {
    sendEmail() {
      window.open("mailto:cahillsf9@gmail.com")
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

form{
    grid-column: 2;
}

form p {
    text-align: left;
    margin: 3% 0 3% 0;
    font-weight: bold;
}
h2{
    grid-column: 2;
    grid-row: 1;
    margin: 0;
    color: blue;
}

h4{
    grid-column: 2;
    text-align: left;

}
input{
    width: 100%;
}
.header {
    grid-row: 2;
}

.contactMeGrid{
  position: relative;
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 60px 60px 1fr 60px 60px;
}

#emailDiv {
    grid-column: 2;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    justify-items: center;
    align-items: center;
    cursor: pointer;
}

#emailDiv:hover #arrowImg{
    padding-left: 30px;
}

#mainDiv{
    grid-row: 3;
    position: relative;
    display: grid;
    grid-template-columns: 0.2fr 0.6fr 0.2fr;
}

#emailImg {
    height: 38px;
    grid-column: 1;
    justify-self: end;
    padding-right: 8px;
    margin-top: 3px;
}

#arrowImg {
    height: 38px;
    grid-column: 3;
    justify-self: start;
    padding-left: 8px;
    margin-top: 3px;
    transition-property: padding-left;
    transition-duration: 0.3s;
    transition-timing-function: linear;
}

#submitButton {
    grid-column: 2;
    margin-top: 20px;
}

@media only screen and (max-width: 650px){
    #mainDiv{
      grid-template-columns: 0.05fr 0.9fr 0.05fr;
    }
}


</style>
