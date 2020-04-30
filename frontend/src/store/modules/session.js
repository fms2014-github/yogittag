import axios from '../../api/axiosScript.js'

const state = {
    session: '',
    login: false,
}

//getters
const getters = {
    jwtCheck: async (state) => {
        if (state.session.jwt != '') {
            state.session = (await axios.sessionCheck(state.session)).data.data
        }
    },
}

// action
const action = {}

// mutations
const mutations = {
    sessionSave: (state, getSession) => {
        state.session = getSession
        state.login = true
    },
    sessionDelte: (state) => {
        state.session = null
        state.login = false
        sessionStorage.removeItem('session')
    },
}

export default {
    namespaced: true,
    state,
    mutations,
    action,
    getters,
}
