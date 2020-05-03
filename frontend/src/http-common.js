import axios from 'axios'

export default axios.create({
    baseURL: 'http://i02d105.p.ssafy.io:8000',

    headers: {
        'Content-type': 'application/json; charset=utf-8',
    },
})
