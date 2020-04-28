<template>
    <span>
        <template v-if="isTemp">{{ temperature }}</template>
        <template v-if="isPrecip">{{ precipitationType }}</template>
        <template v-if="isHumidity">{{ Humidity }}</template>
        <template v-if="isWindSpeed">{{ windSpeed }}</template>
    </span>
</template>

<script>
import apiAxios from '../api/axiosScript'
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

export default {
    props: {
        isTemp: {
            type: Boolean,
            default: false,
        },
        isPrecip: {
            type: Boolean,
            default: false,
        },
        isHumidity: {
            type: Boolean,
            default: false,
        },
        isWindSpeed: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            temperature: '',
            precipitationType: '',
            Humidity: '',
            windSpeed: '',
        }
    },
    async mounted() {
        function getGeolocationData(callback) {
            return new Promise((resolve, reject) => {
                navigator.geolocation.getCurrentPosition(
                    (pos) => {
                        resolve(pos)
                    },
                    (err) => {
                        reject(ree)
                    },
                    { enableHighAccuracy: true },
                )
            })
        }
        var geolocationData = await getGeolocationData()
        let crd = geolocationData.coords
        let d = new Date(geolocationData.timestamp - 2400000)

        var sn = Math.tan(Math.PI * 0.25 + slat2 * 0.5) / Math.tan(Math.PI * 0.25 + slat1 * 0.5)
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
            base_date:
                '' +
                d.getFullYear() +
                (d.getMonth() + 1 < 10 ? '0' + (d.getMonth() + 1) : d.getMonth() + 1) +
                (d.getDate() < 10 ? '0' + d.getDate() : d.getDate()),
            base_time:
                (d.getHours() < 10 ? '0' + d.getHours() : '' + d.getHours()) +
                (d.getMinutes() < 10 ? '0' + d.getMinutes() : '' + d.getHours()),
            nx: rs['x'],
            ny: rs['y'],
            numOfRows: 10,
            pageNo: 1,
            _type: 'json',
        }
        let datas = (await apiAxios.getForecastGrib(data)).data.response.body.items.item
        for (let i in datas) {
            let category = datas[i].category
            if (category === 'T1H') {
                this.temperature =
                    datas[i].obsrValue >= 900 || datas[i].obsrValue <= -900
                        ? 'N/A'
                        : datas[i].obsrValue
            } else if (category === 'REH') {
                this.Humidity =
                    datas[i].obsrValue >= 900 || datas[i].obsrValue <= -900
                        ? 'N/A'
                        : datas[i].obsrValue
            } else if (category === 'PTY') {
                this.precipitationType =
                    datas[i].obsrValue >= 900 || datas[i].obsrValue <= -900
                        ? 'N/A'
                        : datas[i].obsrValue
            } else if (category === 'WSD') {
                this.windSpeed =
                    datas[i].obsrValue >= 900 || datas[i].obsrValue <= -900
                        ? 'N/A'
                        : datas[i].obsrValue
            }
        }
    },
    methods: {
        testPrint() {
            console.log(this.$data)
        },
    },
}
</script>

<style></style>
