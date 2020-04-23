<template>
    <ul
        class="display-1 word-rotate"
        @mouseover="$emit('toggleRotate')"
        @mouseout="$emit('toggleRotate')"
    >
        <li>creative</li>
        <li>innovative</li>
        <li>curious</li>
        <li>experimental</li>
        <li>creative</li>
        <li>innovative</li>
        <li>curious</li>
        <li>experimental</li>
    </ul>
</template>

<script>
export default {
    name: 'WordSpinner',
    props: {
        isRotate: Boolean,
    },
    methods: {
        rotate(start, words) {
            for (let i = 0; i < words.length; ++i) {
                const j = (start + i) % words.length
                let percent = j / words.length
                let rad = percent * 2 * Math.PI
                let ty = Math.sin(rad) * 200
                let tz = 40 * Math.cos(rad) - 40
                let op = (Math.cos(rad) + 1) / 3
                words[
                    i
                ].style.transform = `perspective(10px) translateZ(${tz}px) translateY(${ty}%)`
                words[i].style.opacity = `${op}`
                words[(words.length - start) % words.length].style.opacity = 1
            }
        },
    },
    mounted() {
        const wr = document.querySelector('.word-rotate')
        const words = wr.children
        let x = 0
        for (let i = 0; i < words.length; ++i) {
            const j = i % words.length
            let percent = j / words.length
            let rad = percent * 2 * Math.PI
            let ty = Math.sin(rad) * 200
            let tz = 40 * Math.cos(rad) - 40
            words[i].style.transform = `perspective(5px) translateZ(${tz}px) translateY(${ty}%)`
            words[i].style.opacity = 0
        }
        setInterval(() => {
            if (this.isRotate) {
                x = ++x % words.length
                this.rotate(x, words)
            }
        }, 1000)
    },
}
</script>

<style lang="scss" scoped>
.word-rotate {
    position: absolute;
    display: inline-block;
    margin: 0;
    padding: 0;
    top: 50%;
    left: 50%;
    color: white;
    transform: translate(-50%, -50%);
    list-style-type: none;
    li {
        position: absolute;
        transition: all 1s;
    }
}
</style>
