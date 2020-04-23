import http from "../http-common";
import axios from "axios";

const weatherAxios = axios.create({
    baseURL: 'https://jsonp.afeld.me/'
})

const searchStore = async (data, success, error) => {
    http
        .get('/api/store/' + data.keyword, {
            params: {
                latitude: data.latitude,
                longitude: data.longitude,
                category: data.category,
                distance: data.distance
            }
        })
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

const loginAxios = async (data, success, error) => {
    /* await axios({
            url: 'http://192.168.0.46:8080/apiTest/3sec-return',
            method: 'post',
        }) 
    
    .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })*/
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
    /* axios({
            url: 'http://localhost:9999/api/check',
            method: 'post',
            data: data,
        }) 
    .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })*/
}

const naverOauthAxios = (data, success, error) => {
    /* axios({
            url: 'http://localhost:9999/api/check2',
            method: 'post',
            data: data,
        }) 
    .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })*/
}

const getUserById = (data, success, error) => {
    http
        .get('/api/users/' + data)
        .then(success => {
            success(data);
        })
        .catch(error => {
            error(data);
        })
}

const axiosFunction = {
    searchStore: (data, success, error) => searchStore(data, success, error),
    loginAxios: (data, success, error) => loginAxios(data, success, error),
    getForecastGrib: (data) => getForecastGrib(data),
    googleOauthAxios: (data, success, error) => googleOauthAxios(data, success, error),
    naverOauthAxios: (data, success, error) => naverOauthAxios(data, success, error),
    getUserById: (data, success, error) => getUserById(data, success, error)
}

export default axiosFunction