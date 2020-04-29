<template>
    <div id="banner">
        <!-- <p id="temp">
            <TodayWeather @handleTemperature="" isTemp="true" />˚C
        </p>-->
        <p id="banner_info">
            <!-- <TimeNow /> -->
            <TodayWeather :weather.sync="weather" :isIcon="true" :isTemp="true" />˚C
        </p>
        <br />
        <p id="banner_text">{{this.banner_text}}</p>

        <word-spinner :banner_menu="banner_menu" />
    </div>
</template>

<script>
import WordSpinner from '../../components/WordSpinner'
import TodayWeather from '../../components/TodayWeather'
import TimeNow from '../../components/TimeNow'
export default {
    name: 'Banner',
    components: {
        WordSpinner,
        TodayWeather,
        TimeNow,
    },
    data() {
        return {
            weather: {},
            isRotate: true,
            mylist: [],
            banner_image: '../../assets/img/bannerImg01.jpg',
            banner_text: '',
            banner_menu: [],
        }
    },
    watch: {
        
        weather: function(v) {
            console.log(v.temperature)
            if (v.precipitationType == '0' && parseFloat(v.temperature) <= 10) {
                this.banner_image = '../../assets/img/banner_ocean.jpg'
                this.banner_text = '무더운 날씨에요. 몸보신 어때요?'
                this.banner_menu = ['삼계탕', '장어탕', '팥빙수', '냉면']
                console.log(this.banner_text)
            }
            else {
                this.banner_image = '../../assets/img/banner_ocean.jpg'
                this.banner_text = '한적한 오후에요.'
                this.banner_menu = ['곱창', '족발', '치킨']
                console.log(this.banner_text)
            }

            // document.getElementById('banner').style.backgroundImage=`url(${(banner_image)})`
            document.getElementById('banner').classList.add('banner')
        } 
        // temperature: function(v) {
        //     precipitationType()
        //     if (parseFloat(temperature) <= 10) {
        //         console.log("Hello")
        //         banner_image = '@/assets/img/banner_afternoon.jpg'
        //     }
        // },

        // precipitationType: function(v){
            
        // },

        // temperature: function() {

        //     ret = []

        //     if(T >= 10) {
        //         // el = document.getElementById("banner");
        //         // el.style.background-image = 0.5;
        //     }
        //     this.mylist = ret;
        // }
    },
    methods: {
        toggleRotate() {
            this.isRotate = !this.isRotate
        },
        handleTemperature(changed) {
            // this.temperature = changed;
        }
    },
    mounted() {},
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Inconsolata:400,700');

* {
    font-family: 'Inconsolata';
    box-sizing: border-box;
}

.banner {
    background-image: url('../../assets/img/banner_afternoon.jpg');
}

#banner {
    position: relative;
    text-align: center;
    margin: 50px 0;
    padding: 5px;
    width: 100%;
    height: 180px;
    border-radius: 10px;
    box-shadow: 0 8px 6px -6px black;
    background-color: lightgray;
    background-size: cover;
    // background-image: url('../../assets/img/banner_afternoon.jpg');
    #banner_info {
        font-family: h1c;
        font-size: 30px;
        float: right;
        padding-right: 5px;
        color: rgb(51, 50, 50);
    }
    #banner_text {
        padding-bottom: 0px;
        font-family: h1c;
        font-size: 35px;
    }
}
</style>
