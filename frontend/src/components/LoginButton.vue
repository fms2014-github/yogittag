<template>
    <div id="login-button" class="radius-button">
        <button title="Login" @click="openLoginPage">
            <img width="28px" src="../assets/icons/sign-in.svg" />
        </button>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
    methods: {
        ...mapMutations('app', ['openLoginPage']),
    },
}
</script>

<style lang="scss" scoped>
#login-button {
    position: absolute;
    padding: 10px;
    right: calc(54px + 96px);
    top: 18px;
    z-index: 10;
    img {
        vertical-align: bottom;
    }
}
</style>
