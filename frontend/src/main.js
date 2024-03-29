import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import './plugins/bootStrapVue'
// import infiniteScroll from "vue-infinite-scroll";
import router from './router'
import store from './store'
import LoadScript from 'vue-plugin-load-script'

import infiniteScroll from 'vue-infinite-scroll'
import VueAwesomeSwiper from 'vue-awesome-swiper'

Vue.use(LoadScript)
Vue.config.productionTip = false
Vue.use(infiniteScroll)
Vue.use(VueAwesomeSwiper)

Vue.use(vuetify)

new Vue({
    vuetify,
    router,
    store,
    render: (h) => h(App),
}).$mount('#app')