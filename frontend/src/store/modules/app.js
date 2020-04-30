import { set, toggle } from '@/utils/vuex'
import axios from '../../api/axiosScript.js'

const state = {
    drawer: null,
    isEdit: false,
    menuOpenCheck: false,
    isLoading: false,
    isLogin: false,
    isProfile: false,
    isRegistrate: false,
    selecterFilter: 'filter 1',
    isFilter: false,
}

//getters
const getters = {
    menuOpenState: (state) => {
        return state.menuOpenCheck
    },
    useFilter: (state) => {
        if (state.selecterFilter === 'filter 1') {
            return false
        } else {
            return true
        }
    },
}

// action
const action = {}

// mutations
const mutations = {
    setDrawer: set('drawer'),
    toggleDrawer: toggle('drawer'),
    initState(state) {
        state.menuOpenCheck = false
        state.isLogin = false
        state.isProfile = false
        state.isRegistrate = false
    },
    menuOpenClose(state) {
        document.getElementById('menu-list').classList.toggle('menu-close')
    },
    loadingSpinner(state) {
        state.isLoading = !state.isLoading
    },
    openLoginPage(state) {
        state.isLogin = !state.isLogin
        if (state.isLogin) {
            state.menuOpenCheck = false
            state.isProfile = false
            state.isRegistrate = false
        }
    },
    openUserProfilePage(state) {
        state.isProfile = !state.isProfile
        if (state.isProfile) {
            state.menuOpenCheck = false
            state.isLogin = false
            state.isRegistrate = false
        }
    },
    openUserRegistratePage(state) {
        state.isRegistrate = !state.isRegistrate
        state.isLogin = !state.isLogin
    },
    registrateFinish(state) {
        state.isRegistrate = !state.isRegistrate
        state.isLogin = !state.isLogin
    },
    setSelecterFilter(state, value) {
        state.selecterFilter = value
    },
    switchIsEdit(state) {
        state.isEdit = !state.isEdit
    },
}

export default {
    namespaced: true,
    state,
    mutations,
    action,
    getters,
}
