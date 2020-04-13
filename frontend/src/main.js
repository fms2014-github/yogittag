import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
// import infiniteScroll from "vue-infinite-scroll";
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
Vue.config.productionTip = false
// Vue.use(infiniteScroll);

new Vue({
    vuetify,
    router,
    store,
    render: (h) => h(App),
}).$mount('#app')
