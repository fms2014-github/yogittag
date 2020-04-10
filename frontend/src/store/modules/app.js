// import { set, toggle } from "@/utils/vuex";

const state = {
    menuOpenCheck: false,
    isLoading: false,
    isLogin: false,
    isProfile: false,
}

//getters
const getters = {
    menuOpenState: (state) => {
        return state.menuOpenCheck
    },
}

// action
const action = {}

// mutations
const mutations = {
    menuOpenClose(state) {
        document.getElementById('menu-list').classList.toggle('menu-close')
    },
    loadingSpinner(state) {
        state.isLoading = !state.isLoading
    },
    openLoginPage(state) {
        state.isLogin = !state.isLogin
    },
    openUserProfilePage(state) {
        state.isProfile = !state.isProfile
    },
}

export default {
    namespaced: true,
    state,
    mutations,
    action,
    getters,
}
