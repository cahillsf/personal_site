<template>
  <div class="homeGrid">
    <top-toolbar></top-toolbar>
    <h1 id="home-header">{{ msg }}</h1>
      <!-- loop through cards in js -->
      <vk-card v-for="card in cards" v-bind:key="card.id" v-bind:style="card.style" :data-aos="card.animation" type="primary" @click="navigateToPage(card.route)" hover>
        <vk-card-title>
          {{ card.title }}
        </vk-card-title>
        <img class="card-img" v-if="card.imgPath" :src="require(`@/assets/project_icons/${card.imgPath}`)"> 
      </vk-card>
    <bottom-bar v-bind:style="bottomBarProps"></bottom-bar>
  </div>

</template>

<script>
import axios from 'axios';
import TopToolbar from '../components/TopToolbar.vue';
import BottomBar from '../components/BottomBar.vue';
import { Card, CardTitle } from '../../node_modules/vuikit/lib/card';
export default {
  name: 'HomePage',
  components: {
    TopToolbar,
    VkCard: Card,
    VkCardTitle: CardTitle,
    BottomBar
  },
  data () {
    return {
      msg: 'Welcome',
      bottomBarProps: {
        'grid-column': '1 / 3',
        'background-image': 'linear-gradient(to top, #c4d4e0 0%,#6e9db3 100%)',
        'display': 'none'
      },
      cards: [],
      mainCards: []
      }
    },
    created(){
      this.getCards();
    },
    updated(){
      this.showBottomBar();
    },
    methods: {
      generateCards() {
        //mainCards are the cards received from calling function getCards()

        let keys = Object.keys(this.mainCards);

        //loop through the provided cards adding the proper css to display
        //cards on alternate sides of the webpage with corresponding animation
        keys.forEach(key => {  
          let i = parseInt(key) + 2;
          //define the the style properties object
          let curProps = {
            gridColumn: 0,
            gridRow: 0,
            cursor: 'pointer'
          }
          let curCard = Object.values(this.mainCards).find(el => el._id === parseInt(key));
          console.log(curCard);
          //grid row will correspond the index of the loop
          //as cards are displayed straight down the page
          curProps['gridRow'] = i;
          //column alternates page sides
          //even numbers on the right odd numbers on the left
          curProps['gridColumn'] = (i % 2 != 0)? 2 : 1;
          //assign grid props to card object
          curCard['style'] = curProps;
          //add complete card to cards array
          this.cards.push(curCard);
          console.log(curCard);
        })
        console.log(this.cards);
      },
      getCards() {
        const path = 'http://localhost:8000/cards';
        axios.get(path)
          .then((res) => { 
            this.mainCards = JSON.parse(JSON.stringify(res.data));
            this.generateCards();
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
      },
      showBottomBar() {
        this.bottomBarProps['display'] = 'grid';
        console.log("show bottom")
      },
      navigateToPage(route) {
        this.$router.push({ path: route });
      }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card-img {
  height: 125px;
  transition: transform 0.3s;
}

.uk-card:hover img{
	transform: rotate(360deg);
}


#home-header {
  font-weight: normal;
  grid-row: 1;
  grid-column: 1 / 3;
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

.innerGrid {
  display: grid;
  grid-template-rows: repeat(1fr);
}


</style>
