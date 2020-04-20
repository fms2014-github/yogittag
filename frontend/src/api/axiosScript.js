import axios from 'axios'

const searchAxios = async (data, success, error) => {
    await axios({
        url: 'http://122.199.87.81:11223/apiTest/3sec-return',
        method: 'post',
        data: '',
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

const getForecastGrib = (data, success, error) => {
    let url = 'http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib?'
    for (var key in data) {
        url += encodeURIComponent('&' + key + '=' + data[key])
    }
    axios({
        url: 'https://jsonp.afeld.me/?url=' + url,
        method: 'get',
    })
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

const axiosFunction = {
    searchAxios: (data, success, error) => searchAxios(data, success, error),
    loginAxios: (data, success, error) => loginAxios(data, success, error),
    getForecastGrib: (data, success, error) => getForecastGrib(data, success, error),
}

export default axiosFunction
