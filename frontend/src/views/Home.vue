<template>
    <v-container class="mt-5" fill-height>
        <v-card-text class="text-center">
            <p class="display-2 pa-5" style="font-family: h1c;">🍜 코딩도 식후경</p>
            <banner />

            <v-btn
                class="display-1 font-italic font-weight-bold"
                large
                style="font-family: 'Inconsolata';"
                >Right Now!</v-btn
            >
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

export default {
    components: {
        Banner,
        FoodFriend,
        Slider,
    },
    data() {
        return {
            cardData: [
                {
                    title: 'TITLE',
                    content: 'CONTENT',
                },
                {
                    title: 'TITLE2',
                    content: 'CONTENT2',
                },
                {
                    title: 'TITLE3',
                    content: 'CONTENT3',
                },
                {
                    title: 'TITLE4',
                    content: 'CONTENT4',
                },
                {
                    title: 'TITLE5',
                    content: 'CONTENT5',
                },
                {
                    title: 'TITLE6',
                    content: 'CONTENT6',
                },
            ],
        }
    },
    methods: {},
    mount() {},
}
</script>

<style scoped>
@font-face {
    font-family: h1c;
    src: url('../assets/fonts/DXRMbxB-KSCpc-EUC-H.ttf');
}
</style>
