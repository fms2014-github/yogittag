<template>
    <div>
        <b-btton v-b-toggle.sidebar-1>
            <div id="menu" class="radius-button">
                <span class="material-icons">
                    menu
                </span>
            </div>
        </b-btton>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import '../../assets/css/button.scss'
export default {
    methods: {
        ...mapMutations('app', ['menuOpenClose']),
    },
}
</script>

<style lang="scss" scoped>
#menu {
    position: fixed;
    top: 18px;
    left: 36px;
    z-index: 10;
}
</style>
