<template>
    <div id="banner">
        <p id="temp"><TodayWeather isTemp="true" />˚C</p>
        <word-spinner
            style="padding-bottom: 20px; padding-right: 120px;"
            :isRotate="isRotate"
            @toggleRotate="toggleRotate"
        />
    </div>
</template>

<script>
import WordSpinner from '../../components/WordSpinner'
import TodayWeather from '../../components/TodayWeather'
export default {
    name: 'Banner',
    components: {
        WordSpinner,
        TodayWeather,
    },
    data() {
        return {
            isRotate: true,
        }
    },
    methods: {
        toggleRotate() {
            this.isRotate = !this.isRotate
        },
    },
    mounted() {},
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Inconsolata:400,700');

* {
    font-family: 'Inconsolata';
}
#banner {
    position: relative;
    text-align: center;
    margin: 50px 0;
    padding: 20px 0;
    width: 100%;
    height: 180px;
    border-radius: 10px;
    box-shadow: 0 8px 6px -6px black;
    background-color: lightgray;
    background-size: cover;
    background-image: url('../../assets/img/bannerImg01.jpg');
    #temp {
        font-family: h1c;
        font-size: 50px;
        float: right;
        padding-right: 15px;
        color: rgb(214, 122, 127);
    }
}
</style>
