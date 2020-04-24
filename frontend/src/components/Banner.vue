<template>
    <div id="banner">
        <word-spinner />
    </div>
</template>

<script>
import WordSpinner from '../components/WordSpinner'
export default {
    name: 'Banner',
    components: {
        WordSpinner,
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
    width: 100%;
    height: 180px;
    border-radius: 10px;
    box-shadow: 0 8px 6px -6px black;
    background-color: lightgray;
    #bannerImage {
        position: relative;
        width: 50vw;
        height: 100%;
    }
}
</style>
