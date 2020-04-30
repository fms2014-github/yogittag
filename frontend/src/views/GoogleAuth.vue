<template>
    <div id="profile-edit">
        <profile-edit :isFullSize="true" />
    </div>
</template>

<script>
import axiosApi from '../api/axiosScript'
import profileEdit from './profileEditPage.vue'
import { mapState, mapGetters, mapMutations } from 'vuex'
export default {
    components: {
        profileEdit,
    },
    async mounted() {
        var fragmentString = location.search.substring(1)

        // Parse query string to see if page request is coming from OAuth 2.0 server.
        var params = {}
        var regex = /([^&=]+)=([^&]*)/g,
            m
        while ((m = regex.exec(fragmentString))) {
            params[decodeURIComponent(m[1])] = decodeURIComponent(m[2])
        }
        if (Object.keys(params).length > 0) {
            console.log('asdasd', params)
            let data = (await axiosApi.googleOauthAxios({ oauthCode: params })).data.session
            sessionStorage.setItem('session', JSON.stringify(data))
            this.sessionSave(data)
            if (data.isCompleted) {
                this.$router.push('/')
            }
        }
    },
    methods: {
        ...mapMutations('session', ['sessionSave']),
    },
}
</script>

<style lang="scss" scoped>
#profile-edit {
    position: absolute;
    top: 0px;
    width: 100vw;
    height: 100vh;
    background-color: rgba(128, 128, 128);
}
</style>
