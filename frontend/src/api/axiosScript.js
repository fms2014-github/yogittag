import axios from 'axios'

const weatherAxios = axios.create({
    baseURL: 'https://jsonp.afeld.me/'
})

const searchStore = async (data, success, error) => {
    await axios({
            url: 'http://127.0.0.1:8000/api/store-name',
            method: 'post',
            data: {
                name: data.keyword,
                latitude: data.latitude,
                longitude: data.longitude
            },
        })
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

const loginAxios = async (data, success, error) => {
    await axios({
            url: 'http://192.168.0.46:8080/apiTest/3sec-return',
            method: 'post',
        })
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

const getForecastGrib = (data) => {
    return new Promise((resolve, reject) => {
        let url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib?'
        for (var key in data) {
            url += encodeURIComponent('&' + key + '=' + data[key])
        }
        weatherAxios
            .get('?url=' + url)
            .then((res) => {
                resolve(res)
            })
            .catch((err) => {
                reject(err)
            })
    })
}

const googleOauthAxios = (data, success, error) => {
    axios({
            url: 'http://localhost:9999/api/check',
            method: 'post',
            data: data,
        })
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

const naverOauthAxios = (data, success, error) => {
    axios({
            url: 'http://localhost:9999/api/check2',
            method: 'post',
            data: data,
        })
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

const axiosFunction = {
    searchStore: (data, success, error) => searchStore(data, success, error),
    loginAxios: (data, success, error) => loginAxios(data, success, error),
    getForecastGrib: (data) => getForecastGrib(data),
    googleOauthAxios: (data, success, error) => googleOauthAxios(data, success, error),
    naverOauthAxios: (data, success, error) => naverOauthAxios(data, success, error),
    getStoreById: (data, success, error) => getStoreById(data, success, error),
    getStoreBhourById: (data, success, error) => getStoreBhourById(data, success, error),
    getStoreMenuById: (data, success, error) => getStoreMenuById(data, success, error),
    getStoreReviewById: (data, success, error) => getStoreReviewById(data, success, error),
}

export default axiosFunction