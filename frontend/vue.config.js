const path = require('path')

module.exports = {
    publicPath: '/',
    devServer: {
        proxy: {
            '/api': {
                target: 'http://i02d105.p.ssafy.io/',
            },
        },
    },
    transpileDependencies: ['vuetify'],
    configureWebpack: {
        resolve: {
            alias: {
                '@': path.join(__dirname, 'src/'),
            },
        },
    },
}
