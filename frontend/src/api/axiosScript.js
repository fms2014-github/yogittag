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
    searchAxios: (data, success, error) => searchAxios(data, success, error),
    loginAxios: (data, success, error) => loginAxios(data, success, error),
    googleOauthAxios: (data, success, error) => googleOauthAxios(data, success, error),
    naverOauthAxios: (data, success, error) => naverOauthAxios(data, success, error),
}

export default axiosFunction
