import Vue from 'vue'
import Vuex from 'vuex'
import data from './modules/data'
import app from './modules/app'
import session from './modules/session'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        data,
        app,
        session,
    },
})
