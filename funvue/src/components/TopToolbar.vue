<template>
    <div class="toolbar" role="banner"> 
        <div id="logo-name">
          <img id="logo" src="@/assets/initials.png"/>
          <ul>
							<li>Stephen Cahill</li>
							<li>Developer</li>
          </ul>
        </div>
        <div class="spacer"></div>

        <div id="button-wrapper" class="menu-button-in" v-bind:class="{ 'menu-button-invisible':  smallScreenOnLoad, 'menu-button-out':buttonAnimate }">
          <!-- TO DO: add in routing once I have additional pages -->
          <vk-button size="small" class="menu-button" v-bind:class="{ 'selected':  page.selected }" type="primary" v-for="page in pages" v-bind:key="page.id" @click="navigateToPage(page.path)">
            {{ page.title }}
          </vk-button>
          <!-- <vk-button size="small" class="menu-button" type="primary" @click="$refs.childModal.showModal()">Login</vk-button> -->
          <!-- <vk-button size="small" class="menu-button" type="primary" @click="goToCreateAccount">Create Account</vk-button> -->
        </div>
        <login-modal ref="childModal"></login-modal>
      
        <div id="icon-div" class="icon-animate-in" v-bind:class="{ 'icon-div-invisible': largeScreenOnLoad, 'icon-animate-out': iconAnimate}">
          <img @click="showDropdown" ref="sandwichIcon" id="menu-icon2" src="../assets/icons8-menu.svg"/>
          <vk-drop animation="slide-top-small" position="top-right" mode="click" ref="dropMenu">
            <vk-navbar-nav-dropdown-nav align="right" navbar-aligned="true" id="nav-dropdown">
              <!-- TO DO: add in routing once I have additional pages -->
              <vk-nav-item v-for="page in pages" v-bind:key="page.id" :title="page.title"></vk-nav-item>
            </vk-navbar-nav-dropdown-nav>
          </vk-drop>
        </div>
    </div>

</template>

<script>
import '@vuikit/theme';
import { Button, ButtonLink } from '../../node_modules/vuikit/lib/button';
import { Icon, IconButton } from '../../node_modules/vuikit/lib/icon';
import { IconMenu } from '@vuikit/icons';
import { Drop } from '../../node_modules/vuikit/lib/drop';
import { NavbarNavItem, NavbarNavDropdownNav } from '../../node_modules/vuikit/lib/navbar';
import LoginModal from './LoginModal.vue';
export default {
  name: 'TopToolbar',
  components: {
      LoginModal,
      VkButton: Button,
      VkButtonLink: ButtonLink,
      VkMenu: IconMenu,
      VkIcon: Icon,
      VkIconButton: IconButton,
      VkDrop: Drop,
      VkNavItem: NavbarNavItem, 
      VkNavbarNavDropdownNav: NavbarNavDropdownNav
  },
  data () {
    return {
      msg: 'Talk Tungsten 2 Me',
      dropDisplayed: false,
      largeScreenOnLoad: false,
      smallScreenOnLoad: false,
      firstTime: true,
      iconAnimate: null,
      buttonAnimate: null,
      pages: [
        {
          '_id': 0,
          'title': 'Home',
          'path':'/',
        },
        {
          '_id': 1,
          'title': 'About Me',
          'path':'/'
        },
        {
          '_id': 2,
          'title': 'CV',
          'path':'/'
        },
        {
          '_id': 3,
          'title': 'Contact Me',
          'path':'/'
        },
      ]
    }
  },
  mounted(){

    if(window.innerWidth > 650){
      this.largeScreenOnLoad = true;
      console.log("large screen is " + this.largeScreenOnLoad)
      return;
    }
    this.smallScreenOnLoad = true;

  },
  created(){
    window.addEventListener("resize", this.trackResize);
    this.setCurPageClass();
  },
  destroyed(){
    window.removeEventListener("resize", this.trackResize);
  },
  methods: {
    setCurPageClass() {
      let pageKeys = Object.keys(this.pages);
      pageKeys.forEach(key => {
        let curPage = Object.values(this.pages).find(el => el._id === parseInt(key));
        let jsonCurPage = JSON.parse(JSON.stringify(curPage));
        console.log(jsonCurPage.path);
        if (this.$router.currentRoute.path == jsonCurPage.path){
          console.log("match found!");
          curPage['selected'] = true;
        }
      })
    },
    doSomething() {
      this.msg= 'TopToolbar!;'
    },
    showDropdown(){
      console.log("in show dropdown");
      this.dropDisplayed = (this.dropDisplayed ? false : true);
    },
    trackResize(){
      if(window.innerWidth >= 650){
        if(this.dropDisplayed){
          this.$refs.sandwichIcon.click();
          console.log("flipping display");
        }
        if(this.smallScreenOnLoad && this.firstTime){
          console.log("buttonAnimate = true");
          this.smallScreenOnLoad = false;
          this.firstTime = false;
          this.buttonAnimate = true;
          this.iconAnimate = true;
        }
      }
      else if(this.largeScreenOnLoad && this.firstTime){
        console.log("in else if");
        this.largeScreenOnLoad = false;
        this.firstTime = false;
        this.iconAnimate = true;
        this.buttonAnimate = true;
      }
    },
    goToCreateAccount(){
      this.$router.push({ path: '/createaccount' });
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#logo-name {
  margin-left: 10px;
  font-size: 18px;
  display: grid;
}
#logo-name * {
  grid-row: 1;
}

#logo-name ul {
  list-style-type: none;
  padding-left: 5px;
}

#logo-name li{
	text-align: left;
	margin: 0;
	padding: 0;
}

#logo {
  width: 50px;
	height: 50px;
	position: relative;
  top: 21px;
}

#menu-icon2{
  cursor: pointer;
  position: relative;
  width: 30px;
  height: 30px;
  padding: 2px;
  right: 3vw;
}


#button-wrapper {
  display: grid;
  grid-column-gap: 20px;
  position: relative;
  margin-right: 2%;
}

.selected {
  background-color: #486988;
  color: #fff;
}
.spacer {
  flex: 1;
}

.menu-button{
  grid-row: 1;
  width: 100%;
}

.toolbar {
  /* grid-row: 1; */
  position: absolute;
  left: 0;
  right: 0;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-around;
  background-image: linear-gradient(to top, #c4d4e0 0%,#6e9db3 100%);
  color: white;
  font-weight: 600;
}

.icon-div{
  display: grid;
  position: absolute;
  right: -10vw;
}

.icon-div-invisible{
  display: grid;
  /* position: absolute; */
  right: -10vw;
  /* width: 0; */
  position: relative;
  left: -700vw;
  opacity: 0;
  width: 0;
}

.menu-button-invisible{
  left: -100vw;
  position: relative;
  opacity: 0;
  width: 0;
  height: 100%;
}


@media only screen and (min-width: 650px){
  .icon-animate-out{
    animation-duration: 1s; 
    animation-name: icon-animate-out;
    animation-fill-mode: forwards;
  }
  .menu-button-in{
    animation-duration: 0.7s;
    animation-name: buttons-animate-in;
    animation-fill-mode: forwards;
  }
  
}

@media only screen and (max-width: 650px){
  .menu-button-out{
    animation-duration: 0.7s;
    animation-name: buttons-animate-out;
    animation-fill-mode: forwards;
  }

  .icon-animate-in {
    animation-duration: 1s;
    animation-name: icon-animate-in;
    animation-fill-mode: forwards;
  }

  #nav-dropdown{
    position: absolute;
    background: rgb(225, 241, 225);
    right: 0px;
    top: 60px;
  }

}
@keyframes icon-animate-out {
    0% {
      right: 0;
      position:relative
    }
    100% {
      position: relative;
      left: -700vw;
      opacity: 0;
      width: 0;
    }
}

@keyframes icon-animate-in {
    from {
      right: -10vw;
      position:relative;
    }

    to {
      right: 0;
      position: relative;
    }
}

@keyframes buttons-animate-in {
    100% {
      margin-right: 2%;
      position: relative;
    }

    50% {
      left: -10vw;
      position: relative;
      opacity: 0.9;
    }
    
    10% {
      left: -50vw;
      position: relative;
      opacity: 0.5;
    }
    0% {
      left: -100vw;
      position: relative;
      opacity: 0;
    }
}

@keyframes buttons-animate-out {
    0% {
      margin-right: 2%;
      position: relative;
    }

    10% { 
      left: -50vw;
      position: relative;
      opacity: 0.9;
    }
    
    90% {
      left: -500vw;
      position: relative;
      opacity: 0.5;
    }

    100% {
      left: -700vw;
      position: relative;
      opacity: 0;
      width: 0;
    }
}


</style>
