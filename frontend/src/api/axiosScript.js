import http from '../http-common'
import axios from 'axios'

const weatherAxios = axios.create({
    baseURL: 'https://jsonp.afeld.me/',
})

const searchStore = async (data, success, error) => {
    http.get('/api/store/' + data.keyword, {
        params: {
            latitude: data.latitude,
            longitude: data.longitude,
            category: data.category,
            distance: data.distance,
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

//// users
// get /users
const getAllUser = (success, error) => {
    http.get('/api/users')
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// post /users
const createUser = (data, success, error) => {
    http.post('/api/users', data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get /users/{fId}/followers
const getAllFollowers = (data, success, error) => {
    http.get('/api/users/' + data.fId + '/followers')
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// post /users/{fId}/followers/{tId}
const updateFollow = (data, success, error) => {
    http.post('/api/users/' + data.fId + '/followers/' + data.tId, data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// delete /users/{fId}/followers/{tId}
const deleteFollow = (data, success, error) => {
    http.delete('api/users/' + data.fId + '/followers/' + data.tId)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get /users/{id}
const getUser = (data, success, error) => {
    http.get('/api/users/' + data.id)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// put /users/{id}
const updateUser = (data, success, error) => {
    http.put('/api/users/' + data.id, data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// delete /users/{id}
const deleteUser = (data, success, error) => {
    http.delete('/api/users/' + data.id)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get /users/{id}/favorite-list
const getAllFavoriteList = (data, success, error) => {
    http.get('/api/users/' + data.id + '/favorite-list')
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// post /users/{id}/favorite-list
const createFavoriteList = (data, success, error) => {
    http.post('/api/users/' + data.id + '/favorite-list', data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get /users/{id}/favorite-list/{list_id}
const getFavoriteList = (data, success, error) => {
    http.get('/api/users/' + data.id + '/favorite-list/' + data.list_id)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// post /users/{id}/favorite-list/{list_id}
const updateFavoriteListStore = (data, success, error) => {
    http.post('/api/users/' + data.id + '/favorite-list/' + data.list_id, data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// delete /users/{id}/favorite-list/{list_id}/favorite-store/{store}
const deleteFavoriteListStore = (data, success, error) => {
    http.delete(
        '/api/users/' +
            data.id +
            '/favorite-list/' +
            data.list_id +
            '/favorite-store/' +
            data.store,
    )
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get /users/{id}/favorite-store
const getAllFavoriteStore = (data, success, error) => {
    http.get('/api/users/' + data.id + '/favorite-store')
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get /users/{id}/review
const getAllReview = (data, success, error) => {
    http.get('/api/users/' + data.id + '/review')
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

const imageUpload = async (data, success, error) => {
    return new Promise((resolve, reject) => {
        axios({
            url: 'https://api.imgur.com/3/image',
            method: 'post',
            headers: {
                Authorization: 'Client-ID e4b1b507e84fdc3',
            },
            data: data,
        })
            .then((res) => {
                resolve(res.data.data.link)
            })
            .catch((err) => {
                reject(err)
            })
    })
}

const axiosFunction = {
    searchStore: (data, success, error) => searchStore(data, success, error),
    loginAxios: (data, success, error) => loginAxios(data, success, error),
    getForecastGrib: (data) => getForecastGrib(data),
    googleOauthAxios: (data, success, error) => googleOauthAxios(data, success, error),
    naverOauthAxios: (data, success, error) => naverOauthAxios(data, success, error),

    getAllUser: (success, error) => getAllUser(success, error),
    createUser: (data, success, error) => createUser(data, success, error),
    getAllFollowers: (data, success, error) => getAllFollowers(data, success, error),
    updateFollow: (data, success, error) => updateFollow(data, success, error),
    deleteFollow: (data, success, error) => deleteFollow(data, success, error),
    getUser: (data, success, error) => getUser(data, success, error),
    updateUser: (data, success, error) => updateUser(data, success, error),
    deleteUser: (data, success, error) => deleteUser(data, success, error),
    getAllFavoriteList: (data, success, error) => getAllFavoriteList(data, success, error),
    createFavoriteList: (data, success, error) => createFavoriteList(data, success, error),
    getFavoriteList: (data, success, error) => getFavoriteList(data, success, error),
    updateFavoriteListStore: (data, success, error) =>
        updateFavoriteListStore(data, success, error),
    deleteFavoriteListStore: (data, success, error) =>
        deleteFavoriteListStore(data, success, error),
    getAllFavoriteStore: (data, success, error) => getAllFavoriteStore(data, success, error),
    getAllReview: (data, success, error) => getAllReview(data, success, error),
    imageUpload: (data, success, error) => imageUpload(data, success, error),
}

export default axiosFunction
