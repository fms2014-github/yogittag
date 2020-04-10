<template>
    <div id="menu" class="radius-button">
        <button title="Menu" class="menu-button" @click="menuOpenClose">
            <span class="material-icons">
                menu
            </span>
        </button>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import '../assets/css/button.scss'
export default {
    methods: {
        ...mapMutations('app', ['menuOpenClose']),
    },
}
</script>

<style lang="scss" scoped>
#menu {
    position: absolute;
    top: 18px;
    left: 36px;
    z-index: 10;
}
</style>
