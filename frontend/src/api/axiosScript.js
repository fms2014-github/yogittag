import http from '../http-common'
import axios from 'axios'

const weatherAxios = axios.create({
    baseURL: 'https://jsonp.afeld.me/',
})

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

// post /auth/google
const googleOauthAxios = (data) => {
    return new Promise((resolve, reject) => {
        http.post('/api/auth/google', data)
            .then((res) => {
                resolve(res)
            })
            .catch((err) => {
                reject(err)
            })
    })
}

// post /auth/naver
const naverOauthAxios = (data) => {
    return new Promise((resolve, reject) => {
        http.post('/api/auth/naver', data)
            .then((res) => {
                resolve(res)
            })
            .catch((err) => {
                reject(err)
            })
    })
}

// menu
// get menu/{id}
const getMenuById = (data, success, error) => {
    http.get('/api/menu/' + data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get menu/{name}
const getMenuByName = (data, success, error) => {
    http.get('/api/menu' + data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

//get menu/{price}/price
const getMenuPriceList = (data, success, error) => {
    http.get('/api/menu/' + data + '/price')
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

//Review
//get review/{id}
const getReview = (data, success, error) => {
    http.get('/api/review/' + data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get review/{score}/score
const getReviewScoreList = (data, success, error) => {
    http.get('/api/review/' + data + '/score')
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// post session-check
const sessionCheck = (data, success, error) => {
    http.post('/api/session-check', data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

//Store
// get /store/{id}
const getStore = (data, success, error) => {
    http.get('/api/store/' + data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

//get /store/{id}/bhour
const getStoreHour = (data, success, error) => {
    http.get('/api/store/' + data + '/bhour')
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

//get store/{id}/menu
const getStoreMenu = (data, success, error) => {
    http.get('/api/store/' + data + '/menu')
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get store/{id}/review
const getStoreReview = (data, success, error) => {
    http.get('/api/store/' + data + '/review')
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get store/{name}
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
    http.get('/api/users/' + data + '/followers')
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
// get /users/{id}/review
const createReview = (data, success, error) => {
    http.post('/api/store/' + data.store + '/review', data)
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

// get /recomm/{id}
const getRecommandationById = (data, success, error) => {
    http.get('/api/recomm/' + data.id, {
            params: {
                latitude: data.latitude,
                longitude: data.longitude,
                users: data.users,
                area: data.area
            }
        })
        .then((res) => {
            success(res)
        })
        .catch((err) => {
            error(err)
        })
}

const getRecommandationByFollowers = (data, success, error) => {
    http.get('/api/recomm/' + data + '/followers')
        .then(res => {
            success(res)
        })
        .catch(err => {
            error(err)
        })
}

const axiosFunction = {
    searchStore: (data, success, error) => searchStore(data, success, error),
    loginAxios: (data, success, error) => loginAxios(data, success, error),
    getForecastGrib: (data) => getForecastGrib(data),
    googleOauthAxios: (data) => googleOauthAxios(data),
    naverOauthAxios: (data) => naverOauthAxios(data),

    //
    getMenuById: (data, success, error) => getMenuById(data, success, error),
    getMenuByName: (data, success, error) => getMenuByName(data, success, error),
    getMenuPriceList: (data, success, error) => getMenuPriceList(data, success, error),

    getReview: (data, success, error) => getReview(data, success, error),
    getReviewScoreList: (data, success, error) => getReviewScoreList(data, success, error),
    sessionCheck: (data, success, error) => sessionCheck(data, success, error),

    getStore: (data, success, error) => getStore(data, success, error),
    getStoreHour: (data, success, error) => getStoreHour(data, success, error),
    getStoreMenu: (data, success, error) => getStoreMenu(data, success, error),
    getStoreReview: (data, success, error) => getStoreReview(data, success, error),
    //

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

    getRecommandationById: (data, success, error) => getRecommandationById(data, success, error),
    createReview: (data, success, error) => createReview(data, success, error),
    getRecommandationByFollowers: (data, success, error) => getRecommandationByFollowers(data, success, error)
}

export default axiosFunction