<template>
    <div>
        <div class="swiper-button-prev" slot="button-prev"></div>
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
        </swiper>
        <div class="swiper-button-next" slot="button-next"></div>
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
                slidesPerView: 5,
                spaceBetween: 30,
                slidesPerGroup: 5,
                loop: true,
                loopFillGroupWithBlank: true,
                pagination: {
                    el: '.swiper-pagination',
                    clickable: true,
                },
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
            },
        }
    },
    methods: {
        test(e) {
            console.log(e)
            console.log(e.target.offsetHeight)
            console.log(e.target.offsetWidth)
            document.getElementById(e.target.id).style.width = e.target.offsetWidth * 2 + 'px'
        },
        test1(e) {
            document.getElementById(e.target.id).style.width = e.target.offsetWidth / 2
        },
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
        background-color: blue;

        -webkit-transition: transform 0.35s ease-in-out;
        -moz-transition: transform 0.35s ease-in-out;
        -o-transition: transform 0.35s ease-in-out;
        transition: transform 0.35s ease-in-out;
    }

    .swiper-slide:hover {
        -webkit-transform: scale(1.1); /*  크롬 */
        -moz-transform: scale(1.1); /* FireFox */
        -o-transform: scale(1.1); /* Opera */
        transform: scale(1.1);
        -webkit-transition: transform 0.35s ease-in-out;
        -moz-transition: transform 0.35s ease-in-out;
        -o-transition: transform 0.35s ease-in-out;
        transition: transform 0.35s ease-in-out;
    }
}
.swiper-button-prev,
.swiper-button-next {
    z-index: 0;
}
</style>
