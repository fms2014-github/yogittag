<template>
    <div>
        <b-carousel
            id="carousel-1"
            v-model="slide"
            :interval="4000"
            controls
            indicators
            background="#ababab"
            img-width="1024"
            img-height="480"
            style="text-shadow: 1px 1px 2px #333;"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
        >
            <b-carousel-slide v-for="item in imgs" :key="item.id" :img-src="item" />
        </b-carousel>
    </div>
</template>

<script>
export default {
    props: {
        imgs: {
            type: Array,
            default: function () {
                return ['http://placehold.it/1024x480']
            },
        },
    },
    data() {
        return {
            slide: 0,
            sliding: null,
        }
    },
    methods: {
        onSlideStart(slide) {
            this.sliding = true
        },
        onSlideEnd(slide) {
            this.sliding = false
        },
    },
}
</script>
