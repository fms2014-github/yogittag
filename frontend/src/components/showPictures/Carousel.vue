<template>
    <div>
        <b-carousel
            id="carousel-fade"
            style="text-shadow: 0px 0px 2px #000;"
            fade
            indicators
            img-width="1024"
            img-height="480"
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
                return [
                    // 'http://placehold.it/1024x480',
                    'https://picsum.photos/1024/480/?image=10',
                    'https://picsum.photos/1024/480/?image=12',
                    'https://picsum.photos/1024/480/?image=22',
                ]
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
