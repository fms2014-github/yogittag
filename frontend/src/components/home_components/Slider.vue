<template>
    <div>
        <p
            v-if="cardData.length"
            class="display-2 font-weight-thin text--secondary text-left"
        >&nbsp;{{ title }}</p>
        <swiper :options="swiperOption">
            <s-card
                class="swiper-slide"
                v-for="item in cardData"
                :key="item.id"
                :title="item.store_name"
                :content="item.category"
                :img="item.pictures[0]"
                :routing="'/store/' + item.id"
                style="padding: 0;"
            ></s-card>
            <div class="swiper-button-prev" slot="button-prev"></div>
            <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
    </div>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
import sCard from '@/components/cards/SmallCard.vue'
import 'swiper/css/swiper.css'
export default {
    props: {
        title: {
            type: String,
        },
        cardData: {
            type: Array,
        },
    },
    name: 'Slider',
    components: {
        Swiper,
        SwiperSlide,
        sCard,
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
                    1000: {
                        slidesPerGroup: 4,
                        slidesPerView: 4,
                        // spaceBetween: 20,
                    },
                    768: {
                        slidesPerGroup: 3,
                        slidesPerView: 3,
                        // spaceBetween: 20,
                    },
                    540: {
                        slidesPerGroup: 2,
                        slidesPerView: 2,
                        // spaceBetween: 20,
                    },
                    0: {
                        slidesPerGroup: 1,
                        slidesPerView: 1,
                        // spaceBetween: 20,
                    },
                },
            },
        }
    },
    methods: {},
    mounted() {},
}
</script>

<style lang="scss" scoped>
.swiper {
    height: 100%;
    width: 100%;
    // padding: 100px;

    .swiper-slide {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-weight: bold;
        font-size: 20px;

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
