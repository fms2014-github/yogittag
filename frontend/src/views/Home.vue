<template>
    <v-container class="mt-5" fill-height>
        <v-card-text class="text-center">
            <!-- <p class="display-3 pa-2">🍜</p>
            <p class="display-2 pa-5">코딩도 식후경</p>
            <v-btn large color="blue lighten-1 white--text ma-5" rounded to="/search"
                >검색하기</v-btn
            >-->
            <banner />
            <v-btn
                class="display-1 font-italic font-weight-bold"
                large
                style="font-family: 'Inconsolata';"
                >Right Now!</v-btn
            >
            <food-friend />
            <slider />
            <slider />
        </v-card-text>
    </v-container>
</template>

<script>
import Banner from '../components/Banner'
import FoodFriend from '../components/FoodFriend'
import Slider from '../components/Slider'
export default {
    components: {
        Banner,
        FoodFriend,
        Slider,
    },
    data() {
        return {}
    },
    methods: {},
    mount() {},
}
</script>
