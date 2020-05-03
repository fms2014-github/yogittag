<template>
    <div id="profile-button" class="radius-button">
        <router-link to="/profile" title="Profile">
            <img src="../assets/icons/person-black-24dp.svg" />
        </router-link>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import '../assets/css/button.scss'
export default {
    methods: {
    },
}
</script>

<style lang="scss" scoped>
#profile-button {
    position: absolute;
    padding: 10px;
    right: calc(36px + 48px);
    top: 18px;
    z-index: 10;
    img {
        vertical-align: bottom;
    }
}
</style>
