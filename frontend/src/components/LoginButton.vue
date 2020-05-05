<template>
    <div id="login-button" class="radius-button">
        <button title="Login" @click="buttonAction">
            <img v-if="loginState" width="28px" src="../assets/icons/sign-in.svg" />
            <img v-if="!loginState" width="28px" src="../assets/icons/logout-icon-23398.png" />
        </button>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
    props: ['loginState'],
    methods: {
        ...mapMutations('app', ['openLoginPage']),
        ...mapMutations('session', ['sessionDelte']),
        buttonAction() {
            console.log(this.loginState)
            if (this.loginState) {
                this.openLoginPage()
            } else {
                alert('로그아웃 되었습니다.')
                this.sessionDelte()
                if (this.$route.path === '/profile' || this.$route.path ==='/detail-profile') {
                    this.$router.push('/')
                }
            }
        },
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
