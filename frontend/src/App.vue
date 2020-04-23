<template>
    <div id="app">
        <loading-spinner v-if="this.isLoading" />
        <menu-button />
        <menu-list @closeCheckChange="menuOpenClose" />
        <login-button />
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
import mainView from './components/View.vue'
import menuButton from './components/MenuButton.vue'
import profileButton from './components/ProfileButton.vue'
import MenuList from './components/MenuList.vue'
import FAQnQNAButton from './components/FAQnQNAButton.vue'
import loadingSpinner from './components/LoadingSpinner.vue'
import loginButton from './components/LoginButton.vue'
import loginPage from './components/UserSignNewForm.vue'
import userProfile from './components/UserProfile.vue'
import weather from './components/TodayWeather.vue'
import minigame from './components/Minigame.vue'
// import userRegistrate from './components/UserRegistrate.vue'
import { mapState, mapMutations, mapGetters } from 'vuex'

export default {
    components: {
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
        ...mapGetters('app', ['menuOpenState']),
    },
    methods: {
        ...mapMutations('app', ['menuOpenClose']),
    },
}
</script>

<style scoped>
.v-application--wrap {
    min-height: 15vh important!;
}
</style>
