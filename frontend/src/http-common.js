import axios from 'axios'

export default axios.create({
    baseURL: 'http://i02d105.p.ssafy.io',

    headers: {
        'Content-type': 'application/json; charset=utf-8',
    },
})
