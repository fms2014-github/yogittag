<template>
    <div>
        <p class="display-2 font-weight-thin text--secondary text-left">&nbsp;Recommandation</p>
        <swiper class="swiper" :options="swiperOption">
            <swiper-slide>Slide 01</swiper-slide>
            <swiper-slide>Slide 02</swiper-slide>
            <swiper-slide>Slide 03</swiper-slide>
            <swiper-slide>Slide 04</swiper-slide>
            <swiper-slide>Slide 05</swiper-slide>
            <swiper-slide>Slide 06</swiper-slide>
            <swiper-slide>Slide 07</swiper-slide>
            <swiper-slide>Slide 08</swiper-slide>
            <swiper-slide>Slide 09</swiper-slide>
            <swiper-slide>Slide 10</swiper-slide>
            <swiper-slide>Slide 11</swiper-slide>
            <swiper-slide>Slide 12</swiper-slide>
            <div class="swiper-button-prev" slot="button-prev"></div>
            <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
    </div>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'
export default {
    name: 'Slider',
    components: {
        Swiper,
        SwiperSlide,
    },
    data() {
        return {
            swiperOption: {
                loop: true,
                loopFillGroupWithBlank: true,
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
                breakpoints: {
                    1264: {
                        slidesPerGroup: 5,
                        slidesPerView: 5,
                        spaceBetween: 30,
                    },
                    960: {
                        slidesPerGroup: 4,
                        slidesPerView: 4,
                        spaceBetween: 30,
                    },
                    768: {
                        slidesPerGroup: 3,
                        slidesPerView: 3,
                        spaceBetween: 30,
                    },
                    500: {
                        slidesPerGroup: 2,
                        slidesPerView: 2,
                        spaceBetween: 30,
                    },
                    0: {
                        slidesPerGroup: 1,
                        slidesPerView: 1,
                        spaceBetween: 30,
                    },
                },
            },
        }
    },
    methods: {
    },
    mounted() {
        document.querySelectorAll('.swiper-slide').forEach((ss) => {
            ss.addEventListener('mouseover', (e) => {
                console.log(e, 'over')
            })
        })

        document.querySelectorAll('.swiper-slide').forEach((ss) => {
            ss.addEventListener('mouseout', (e) => {
                console.log(e, 'out')
            })
        })
    },
}
</script>

<style lang="scss" scoped>
.swiper {
    height: 200px;
    width: 100%;
    padding: 10px;

    .swiper-slide {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        background-color: red;

        -webkit-transition: transform 0.35s ease-in-out;
        -moz-transition: transform 0.35s ease-in-out;
        -o-transition: transform 0.35s ease-in-out;
        transition: transform 0.35s ease-in-out;
    }

    .swiper-slide:hover {
        -webkit-transform: scale(1.1);
        -moz-transform: scale(1.1);
        -o-transform: scale(1.1);
        transform: scale(1.1);
        -webkit-transition: transform 0.35s ease-in-out;
        -moz-transition: transform 0.35s ease-in-out;
        -o-transition: transform 0.35s ease-in-out;
        transition: transform 0.35s ease-in-out;
    }
}
.swiper-button-prev,
.swiper-button-next {
    z-index: 1;
}
</style>
