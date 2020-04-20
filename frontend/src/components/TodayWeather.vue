<template>
    <div></div>
</template>

<script>
import apiAxios from '../api/axiosScript'

export default {
    async mounted() {
        navigator.geolocation.getCurrentPosition(
            (pos) => {
                let crd = pos.coords
                let today_minus_40 = new Date().getTime() - 2400000
                let setTime = new Date(today_minus_40)

                var RE = 6371.00877 // 지구 반경(km)
                var GRID = 5.0 // 격자 간격(km)
                var SLAT1 = 30.0 // 투영 위도1(degree)
                var SLAT2 = 60.0 // 투영 위도2(degree)
                var OLON = 126.0 // 기준점 경도(degree)
                var OLAT = 38.0 // 기준점 위도(degree)
                var XO = 43 // 기준점 X좌표(GRID)
                var YO = 136 // 기1준점 Y좌표(GRID)
                var DEGRAD = Math.PI / 180.0
                var RADDEG = 180.0 / Math.PI

                var re = RE / GRID
                var slat1 = SLAT1 * DEGRAD
                var slat2 = SLAT2 * DEGRAD
                var olon = OLON * DEGRAD
                var olat = OLAT * DEGRAD

                var sn =
                    Math.tan(Math.PI * 0.25 + slat2 * 0.5) / Math.tan(Math.PI * 0.25 + slat1 * 0.5)
                sn = Math.log(Math.cos(slat1) / Math.cos(slat2)) / Math.log(sn)
                var sf = Math.tan(Math.PI * 0.25 + slat1 * 0.5)
                sf = (Math.pow(sf, sn) * Math.cos(slat1)) / sn
                var ro = Math.tan(Math.PI * 0.25 + olat * 0.5)
                ro = (re * sf) / Math.pow(ro, sn)
                var rs = {}
                rs['lat'] = crd.latitude
                rs['lng'] = crd.longitude
                var ra = Math.tan(Math.PI * 0.25 + crd.latitude * DEGRAD * 0.5)
                ra = (re * sf) / Math.pow(ra, sn)
                var theta = crd.longitude * DEGRAD - olon
                if (theta > Math.PI) theta -= 2.0 * Math.PI
                if (theta < -Math.PI) theta += 2.0 * Math.PI
                theta *= sn
                rs['x'] = Math.floor(ra * Math.sin(theta) + XO + 0.5)
                rs['y'] = Math.floor(ro - ra * Math.cos(theta) + YO + 0.5)
                let data = {
                    serviceKey:
                        'MmNR527nIcJmqhP2M%2BPQlHzggriBTSHcKX%2FzbZavPFHXQKtm70BmY%2Bq%2BUPznFX8M34H0mQjHMsWODi7%2BE%2F%2BZ6A%3D%3D',
                    base_date: 20200420,
                    base_time:
                        (setTime.getHours() < 10
                            ? '0' + setTime.getHours()
                            : '' + setTime.getHours()) +
                        (setTime.getMinutes() < 10
                            ? '0' + setTime.getMinutes()
                            : '' + setTime.getHours()),
                    nx: rs['x'],
                    ny: rs['y'],
                    numOfRows: 10,
                    pageNo: 1,
                    _type: 'json',
                }
                apiAxios.getForecastGrib(
                    data,
                    (res) => {
                        console.log(res.data.response)
                    },
                    (err) => {
                        console.log(err)
                    },
                )
            },
            (err) => {
                console.warn('ERROR(' + err.code + '): ' + err.message)
            },
            { enableHighAccuracy: true },
        )
    },
}
</script>

<style></style>
