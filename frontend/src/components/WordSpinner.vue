<template>
    <div class="spinner-sentence">
        <div class="spinner" id="wordSpinner" @click="bannerMenuClickEvent">
            <li class="active">{{ banner_menu[0] }}</li>
            <li class="next">{{ banner_menu[1] }}</li>
            <li>{{ banner_menu[2] }}</li>
            <li>{{ banner_menu[3] }}</li>
            <li>{{ banner_menu[4] }}</li>
        </div>
        <span>어때요?</span>
    </div>
</template>

<script>
import axios from '@/api/axiosScript.js'
export default {
    
    name: 'WordSpinner',
    props: {
        banner_menu: {
            type: Array,
        },
    },
    data() {
        return {
            event: null
        }
    },
    methods: {
        bannerMenuClickEvent(e){
            let menuName = e.target.innerText
            console.log(menuName);
            this.$router.push({path:`/listPage/${menuName}` , query: {title : menuName, subTitle : '메뉴 검색'}})
        },
        WordSpinner(el, frequency) {
            var spinner = document.getElementById('wordSpinner')
            var words = Array.from(document.getElementById('wordSpinner').children)
            var active = 0
            var next = 1

            setInterval(function () {
                spinner.classList.add('spin')

                setTimeout(function () {
                    words[active].className = ''
                    active = next
                    words[active].className = 'active'
                    if (++next == words.length) next = 0
                    words[next].className = 'next'
                    spinner.classList.remove('spin')
                }, 500)
            }, frequency)
        },
    },
    mounted() {
        this.WordSpinner('WordSpinner', 3000)
    },
}
</script>

<style lang="scss" scoped>
$width: 200px;
$height: 45px;
$font-size: 1em;

#wordSpinner{
    cursor: pointer;
}

.spinner-sentence {
    // display: flex;
    align-items: right;
    justify-content: right;
    font-size: $font-size;
    font-family: h1c;
    height: 100%;
}

.spinner {
    width: $width;
    height: $height;
    display: inline-block;
    text-align: center;
    transform-style: preserve-3d;
    font-size: 1.2em;
    font-weight: 700;
    margin: 20px 20px 0px 20px;

    &.spin {
        transform: rotateX(-90deg);
        transition: transform 0.3s ease-in-out;
    }
}

/* The two faces of the cube */
.spinner li {
    position: absolute;
    width: $width;
    height: $height;
    background-color: rgba(255, 217, 0, 0.863);
    list-style: none;
    display: none;
    align-items: center;
    justify-content: center;

    &.active {
        display: flex;
        transform: translateZ($height/2);
    }

    &.next {
        display: flex;
        transform: rotateX(90deg) translateZ($height/2);
    }
}
</style>
