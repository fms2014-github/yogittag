<template>
    <div class="spinner-sentence">
        Make
        <div class="spinner" id="wordSpinner">
            <li class="active">World</li>
            <li class="next">Culture</li>
            <li>Connection</li>
            <li>Geography</li>
            <li>Challenge</li>
        </div>Discovery Awesome
    </div>
</template>

<script>
export default {
    name: 'WordSpinner',
    methods: {
        WordSpinner(el, frequency) {
            var spinner = document.getElementById('wordSpinner');
            var words = Array.from(document.getElementById('wordSpinner').children);
            var active = 0;
            var next = 1;
            
            setInterval(function() {
            spinner.classList.add('spin');

            setTimeout(function() {
                words[active].className = '';
                active = next;
                words[active].className = 'active';
                if (++next == words.length) next = 0;
                words[next].className = 'next';
                spinner.classList.remove('spin');
            }, 500);
        }, frequency);
        },
    },
    mounted() {
        this.WordSpinner('WordSpinner', 3000);
    }
}




// export default {
//     name: 'wordSpinner',
//     props: {
//         isRotate: Boolean,
//     },
//     methods: {
//         rotate(start, words) {
//             for (let i = 0; i < words.length; ++i) {
//                 const j = (start + i) % words.length
//                 let percent = j / words.length
//                 let rad = percent * 2 * Math.PI
//                 let ty = Math.sin(rad) * 200
//                 let tz = 40 * Math.cos(rad) - 40
//                 let op = (Math.cos(rad) + 1) / 3
//                 words[
//                 ].style.transform = `perspective(10px) translateZ(${tz}px) translateY(${ty}%)`
//                 words[i].style.opacity = `${op}`
//                 words[(words.length - start) % words.length].style.opacity = 1
//             }
//         },
//     },
//     mounted() {
//         const wr = document.querySelector('.word-rotate')
//         const words = wr.children
//         let x = 0
//         for (let i = 0; i < words.length; ++i) {
//             const j = i % words.length
//             let percent = j / words.length
//             let rad = percent * 2 * Math.PI
//             let ty = Math.sin(rad) * 200
//             let tz = 40 * Math.cos(rad) - 40
//             words[i].style.transform = `perspective(5px) translateZ(${tz}px) translateY(${ty}%)`
//             words[i].style.opacity = 0
//         }
//         setInterval(() => {
//             if (this.isRotate) {
//                 x = ++x % words.length
//                 this.rotate(x, words)
//             }
//         }, 1000)
//     },
// }
</script>

<style lang="scss" scoped>
$width: 200px;
$height: 55px;
$font-size: 2em;

.spinner-sentence {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: $font-size;
    font-family: sans-serif;
    height: 100%;
}

.spinner {
    width: $width;
    height: $height;
    display: inline-block;
    text-align: center;
    transform-style: preserve-3d;
    font-weight: 700;
    margin: 0 10px;

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
    background-color: gold;
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
