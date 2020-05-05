const path = require('path')

module.exports = {
    publicPath: '/',
    devServer: {
        proxy: {
            '/api': {
                target: 'https://i02d105.p.ssafy.io:8000/',
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