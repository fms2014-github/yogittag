/* eslint-disable no-undef */
import Vue from 'vue'
import Router from 'vue-router'
import appx from '../store/modules/app.js'

// Routes
import paths from './paths'

function route(path, view, name) {
    if (path === '/profile') {
        return {
            name: name || view,
            path,
            component: (resolve) => import(`@/views/${view}.vue`).then(resolve),
            beforeEnter: (to, from, next) => {
                let session = JSON.parse(sessionStorage.getItem('session'))
                if (session === null) {
                    appx.state.isLogin = true
                    next({ path: '/' })
                } else {
                    next()
                }
            },
        }
    }
    return {
        name: name || view,
        path,
        component: (resolve) => import(`@/views/${view}.vue`).then(resolve),
    }
}

Vue.use(Router)

// Create a new router
const router = new Router({
    mode: 'history',
    routes: paths
        .map((path) => route(path.path, path.view, path.name))
        .concat([
            {
                path: '*',
                redirect: '/',
            },
        ]),
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        }
        if (to.hash) {
            return {
                selector: to.hash,
            }
        }
        return {
            x: 0,
            y: 0,
        }
    },
})

export default router
