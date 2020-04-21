<template>
    <go-top :max-width="width" :src="url" :size="size" :bottom="bottom"></go-top>
</template>

<script>
import GoTop from '@inotom/vue-go-top'

export default {
    data() {
        return {
            width: 320,
            url: 'https://sandbox.serendip.ws/top.png',
            size: 40,
            bottom: 50,
        }
    },
    components: {
        GoTop,
    },
}
</script>
