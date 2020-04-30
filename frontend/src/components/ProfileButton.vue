<template>
    <div id="profile-button" class="radius-button">
        <button title="Profile" @click="openUserProfilePage">
            <img src="../assets/icons/person-black-24dp.svg" />
        </button>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
import '../assets/css/button.scss'
export default {
    methods: {
        openUserProfilePage() {
            this.$router.push('/profile')
        },
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
