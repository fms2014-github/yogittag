import axios from 'axios'

const searchAxios = async (data, success, error) => {
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

const axiosFunction = {
    searchAxios: (data, success, error) => searchAxios(data, success, error),
    loginAxios: (data, success, error) => loginAxios(data, success, error),
}

export default axiosFunction