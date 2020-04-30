<template>
    <div></div>
</template>

<script>
import axiosApi from '../api/axiosScript'
import { mapState, mapGetters, mapMutations } from 'vuex'
export default {
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
            let data = (await axiosApi.naverOauthAxios({ oauthCode: params })).data.session
            sessionStorage.setItem('session', JSON.stringify(data))
            this.sessionSave(data)
        }
        this.$router.push('/')
    },
    methods: {
        ...mapMutations('session', ['sessionSave']),
    },
}
</script>
