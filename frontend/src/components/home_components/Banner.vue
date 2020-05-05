<template>
    <div id="banner">
        <div id="banner_info">
            <TimeNow style="display: inline; float: left;" />
            <TodayWeather :weather.sync="weather" :isIcon="true" :isTemp="true" />˚C
        </div>
        <div id="banner_sentence">
            <div id="banner_text">{{ banner_text }}</div>
            <word-spinner :banner_menu="banner_menu" />
        </div>
    </div>
</template>

<script>
import WordSpinner from '../../components/WordSpinner.vue'
import TodayWeather from '../../components/TodayWeather.vue'
import TimeNow from '../../components/TimeNow.vue'
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
            banner_image: '',
            banner_text: '',
            banner_menu: [],
        }
    },
    methods: {
        searchByCategoryStore() {
            
        }
    },
    watch: {
        weather: function (v) {
            let today = new Date()
            let hour = today.getHours() // 시간 정보 (0 ~ 23)
            let day = today.getDay() // 요일 정보 (일요일 0, 월요일 1, 토요일 6)
            let month = today.getMonth() // 월 정보 (0 ~ 11 1월 0)
            let prec = v.precipitationType // 날씨 정보 맑음(0), 비(1), 비/눈(2), 눈(3), 소나기(4)
            let temp = parseFloat(v.temperature)
            if ((17 <= hour && hour <= 23 && prec == 0) || (0 <= hour && hour <= 4 && prec == 0)) {
                this.banner_image = 'day_afternoon'
                this.banner_text = '오늘 하루의 마무리는...'
                this.banner_menu = ['피자', '족발', '치킨', '곱창', '연탄불고기']
            } else if ((day == 0 || day == 6) && prec == 0 && 9 <= hour && hour <= 14) {
                this.banner_image = 'day_weekend'
                this.banner_text = '기분 좋은 주말 오전에는'
                this.banner_menu = ['브런치', '케이크', '파스타', '마카롱', '초밥']
            } else if (prec == '2' || prec == '3') {
                this.banner_image = 'day_snow'
                this.banner_text = '하얀 눈이 오는 날, 눈 오는 날에는'
                this.banner_menu = ['우동', '떡볶이', '붕어빵', '라멘', '어묵탕']
            } else if (2 <= month && month <= 4) {
                if (prec == '0' && temp >= 15) {
                    this.banner_image = 'spring_blossom'
                    this.banner_text = '따뜻한 봄날, 꽃 구경이나 소풍에는'
                    this.banner_menu = ['김밥', '샌드위치', '도다리쑥국', '파스타', '마카롱']
                } else if (prec == '1' || prec == '4') {
                    this.banner_image = 'spring_rain'
                    this.banner_text = '지금처럼 봄비가 내리는 순간에는'
                    this.banner_menu = ['부침개', '쌀국수', '막걸리', '칼국수', '어묵탕']
                } else if (temp >= 25) {
                    this.banner_image = 'spring_hot'
                    this.banner_text = '어느덧 봄이 가고 여름이 오려나 봐요.'
                    this.banner_menu = ['메밀소바', '초밥', '비빔냉면', '빙수', '국수']
                } else {
                    this.banner_image = 'spring_hot'
                    this.banner_text = '봄날의 출출한 이 시간,'
                    this.banner_menu = ['햄버거', '샌드위치', '짜장면', '떡볶이', '치킨']
                }
            } else if (5 <= month && month <= 7) {
                if (prec == '1' || prec == '4') {
                    this.banner_image = 'summer_rain'
                    this.banner_text = '비 오는 여름날에는 이게 딱이죠!'
                    this.banner_menu = ['파전', '칼국수', '짬뽕', '막걸리', '국밥']
                } else if (temp >= 30) {
                    this.banner_image = 'summer_hot'
                    this.banner_text = '오늘처럼 무더운 여름날에는 몸보신으로'
                    this.banner_menu = ['삼계탕', '장어탕', '팥빙수', '냉면', '해물탕']
                } else {
                    this.banner_image = 'summer'
                    this.banner_text = '여름하면 떠오르는 음식... 오늘은'
                    this.banner_menu = ['콩국수', '초밥', '비빔냉면', '빙수', '물회']
                }
            } else if (8 <= month && month <= 10) {
                if (prec == '1' || prec == '4') {
                    this.banner_image = 'autumn_rain'
                    this.banner_text = '선선한 가을비 내리는 날에는'
                    this.banner_menu = ['짬뽕', '아구찜', '부대찌개', '해물탕', '칼국수']
                } else if (prec == '0') {
                    this.banner_image = 'autumn_sunny'
                    this.banner_text = '하늘도 맑고 날씨 좋은 가을날,'
                    this.banner_menu = ['굴', '회', '게장', '돈까스', '피자']
                } else {
                    this.banner_image = 'autumn'
                    this.banner_text = '알록달록 물드는 가을, 오늘은'
                    this.banner_menu = ['햄버거', '된장찌개', '치킨', '초밥', '돈까스']
                }
            } else if (11 == month || month <= 1) {
                if (temp <= 5) {
                    this.banner_image = 'winter_cold'
                    this.banner_text = '오늘은 유난히 추운 날이네요.'
                    this.banner_menu = ['국밥', '우동', '설렁탕', '해물탕', '어묵탕']
                } else {
                    if (prec == '1' || prec == '4') {
                        this.banner_image = 'autumn_rain'
                    } else {
                        this.banner_image = 'winter'
                    }
                    this.banner_text = '쌀쌀한 겨울 이 시간, 출출하시죠?'
                    this.banner_menu = ['돈까스', '짜장면', '파스타', '초밥', '칼국수']
                }
            } else {
                this.banner_image = 'day_normal'
                this.banner_text = '이 시간, 출출하지 않으세요?'
                this.banner_menu = ['파스타', '짜장면', '초밥', '피자', '치킨']
            }
            document.getElementById('banner').classList.add(this.banner_image)
        },
    },
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Inconsolata:400,700');

* {
    font-family: 'h1c';
    box-sizing: border-box;
}
p {
    margin: 0;
}

.day_normal {
    background-image: url('../../assets/img/banner/banner_normal.jpg');
}
.day_afternoon {
    background-image: url('../../assets/img/banner/banner_afternoon.jpg');
}
.day_weekend {
    background-image: url('../../assets/img/banner/banner_morning.jpg');
}
.day_snow {
    background-image: url('../../assets/img/banner/banner_snow.jpg');
}
.spring_blossom {
    background-image: url('../../assets/img/banner/banner_cherryblossom.jpg');
}
.spring_rain {
    background-image: url('../../assets/img/banner/banner_raindrop.jpg');
}
.spring_hot {
    background-image: url('../../assets/img/banner/banner_spring.jpg');
}
.summer_rain {
    background-image: url('../../assets/img/banner/banner_rain2.jpg');
}
.summer_hot {
    background-image: url('../../assets/img/banner/banner_hotsummer.jpg');
}
.summer {
    background-image: url('../../assets/img/banner/banner_ocean.jpg');
}
.autumn_rain {
    background-image: url('../../assets/img/banner/banner_rain.jpg');
}
.autumn_sunny {
    background-image: url('../../assets/img/banner/banner_fall.jpg');
}
.autumn {
    background-image: url('../../assets/img/banner/banner_autumn.jpg');
}
.winter_cold {
    background-image: url('../../assets/img/banner/banner_winter2.jpg');
}
.winter {
    background-image: url('../../assets/img/banner/banner_winter.jpg');
}

#banner {
    z-index: -1;
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
    background-position: center;
    #banner_info {
        text-align: right;
        font-family: h1c;
        font-size: 30px;
        padding-right: 15px;
        color: rgb(51, 50, 50);
    }
    #banner_sentence {
        padding-top: 18px;
        padding-bottom: 10px;
        font-size: 33px;
        #banner_text {
            padding-left: 8vw;
            text-align: left;
            font-family: h1c;
        }
    }
}
</style>
