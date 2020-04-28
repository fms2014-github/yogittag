<template>
    <div></div>
</template>

<script>
import axiosApi from '../api/axiosScript'
export default {
    beforeMount() {
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
            axiosApi.naverOauthAxios(
                { oauthCode: params },
                (res) => {
                    console.log(res)
                },
                (err) => {
                    console.log(err)
                },
            )
        }
    },
}
</script>
