<template>
    <div id="app">
        <loading-spinner v-if="this.isLoading" />
        <menu-button />
        <menu-list @closeCheckChange="menuOpenClose" />
        <login-button :loginState="!login" />
        <login-page v-if="this.isLogin" />
        <user-registrate v-if="isRegistrate" />
        <profile-button />
        <userProfile v-if="this.isProfile"></userProfile>
        <FAQnQNAButton />
        <main-view />
        <minigame />
        <weather />
    </div>
</template>

<script>
import Drawer from './components/Drawer.vue'
import Toolbar from './components/Toolbar.vue'
import RouteView from './components/RouteView.vue'
import GoTop from './components/GoTop.vue'

import mainView from './components/View.vue'
import menuButton from './components/sidebar_components/MenuButton'
import MenuList from './components/sidebar_components/MenuList'
import profileButton from './components/ProfileButton.vue'
import FAQnQNAButton from './components/FAQnQNAButton.vue'
import loadingSpinner from './components/LoadingSpinner.vue'
import loginButton from './components/LoginButton.vue'
import loginPage from './components/UserSign.vue'
import userProfile from './components/UserProfile.vue'
import weather from './components/TodayWeather.vue'
import minigame from './components/Minigame.vue'
// import userRegistrate from './components/UserRegistrate.vue'
import { mapState, mapMutations, mapGetters } from 'vuex'

export default {
    components: {
        Drawer,
        Toolbar,
        RouteView,
        GoTop,

        mainView,
        menuButton,
        MenuList,
        profileButton,
        FAQnQNAButton,
        loadingSpinner,
        loginButton,
        loginPage,
        userProfile,
        weather,
        minigame,
    },
    computed: {
        ...mapState('app', ['menuOpenCheck', 'isLoading', 'isLogin', 'isProfile', 'isRegistrate']),
        ...mapState('session', ['login']),
        ...mapGetters('app', ['menuOpenState']),
    },
    methods: {
        ...mapMutations('app', ['menuOpenClose']),
        ...mapMutations('session', ['sessionSave']),
    },
    mounted() {
        let session = JSON.parse(sessionStorage.getItem('session'))
        if (session != undefined) {
            this.sessionSave(session)
        }
    },
}
</script>

<style scoped>
.v-application--wrap {
    min-height: 15vh important!;
}
</style>
