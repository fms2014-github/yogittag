<template>
    <div id="app">
        <loading-spinner v-show="this.isLoading" />
        <menu-button />
        <menu-list @closeCheckChange="menuOpenClose" />
        <login-button />
        <login-page v-show="this.isLogin" />
        <user-registrate v-show="isRegistrate" />
        <profile-button />
        <userProfile v-show="this.isProfile"></userProfile>
        <FAQnQNAButton />
        <main-view />
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
import loginPage from './components/UserSign.vue'
import userProfile from './components/UserProfile.vue'
import userRegistrate from './components/UserRegistrate.vue'
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
        userRegistrate,
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
