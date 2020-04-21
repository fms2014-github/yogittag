import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import store from './store'

import infiniteScroll from 'vue-infinite-scroll'
import VueAwesomeSwiper from 'vue-awesome-swiper'

Vue.config.productionTip = false
Vue.use(infiniteScroll)
Vue.use(VueAwesomeSwiper)

new Vue({
    vuetify,
    router,
    store,
    render: (h) => h(App),
}).$mount('#app')
