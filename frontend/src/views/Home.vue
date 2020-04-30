<template>
    <v-container class="mt-5" fill-height>
        <v-card-text class="text-center">
            <p class="display-2 pa-5" style="font-family: h1c;">🍜 코딩도 식후경</p>
            <banner />

            <v-btn
                class="display-1 font-italic font-weight-bold"
                large
                style="font-family: 'Inconsolata';"
            >Right Now!</v-btn>
            <food-friend />
            <slider title="나의 단골 맛집" :cardData="cardData" />
            <slider title="지인 추천 맛집" />
        </v-card-text>
    </v-container>
</template>

<script>
import Banner from '../components/home_components/Banner'
import FoodFriend from '../components/home_components/FoodFriend'
import Slider from '../components/home_components/Slider'
import axiosApi from '@/api/axiosScript.js'

export default {
    components: {
        Banner,
        FoodFriend,
        Slider,
    },
    data() {
        return {
            cardData: [],
        }
    },
    methods: {},
    mounted() {
        axiosApi.getRecommandationById(
            {
                id: 68632,
                latitude: 37.556862,
                longitude: 126.926666,
                users: [539244, 21180, 209301],
                area: "마포구",
            },
            (res) => {
                console.log(res.data)
                this.cardData = res.data
                this.cardData.forEach( card => {
                    if (card.pictures != null && card.pictures != "") {
                        card.pictures = card.pictures.split("|");
                    }
                    else if ( card.pictures == null ){
                        card.pictures = ""
                    }
                })
                console.log(this.cardData)
            },
            (err) => {
                console.log(err)
            }
        )
    },
}
</script>

<style scoped>
@font-face {
    font-family: h1c;
    src: url('../assets/fonts/DXRMbxB-KSCpc-EUC-H.ttf');
}
</style>
