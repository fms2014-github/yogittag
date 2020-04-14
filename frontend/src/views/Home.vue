<template>
    <v-container class="mt-5" fill-height>
        <v-card-text class="text-center">
            <!-- <p class="display-3 pa-2">🍜</p>
            <p class="display-2 pa-5">코딩도 식후경</p>
            <v-btn large color="blue lighten-1 white--text ma-5" rounded to="/search"
                >검색하기</v-btn
            >-->
            <Slider />
        </v-card-text>
    </v-container>
</template>

<script>
import Slider from '../components/Slider'
export default {
    components: {
        Slider,
    },
    data() {
        return {}
    },
    mount() {
        console.log(this.$http)
    },
}
</script>
