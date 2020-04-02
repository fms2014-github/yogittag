<template>
    <div id="menu" class="radius-button">
        <button title="Menu" class="menu-button" @click="menuOpenClose">
            <span class="material-icons">
                menu
            </span>
        </button>
    </div>
</template>

<style lang="scss" scoped>
#menu {
    position: absolute;
    top: 18px;
    left: 18px;
    z-index: 10;
}
</style>

<script>
import { mapMutations } from 'vuex'
import '../assets/css/button.scss'
export default {
    methods: {
        ...mapMutations('app', ['menuOpenClose']),
    },
}
</script>
