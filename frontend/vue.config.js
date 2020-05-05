const path = require('path')

module.exports = {
    publicPath: '/',
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8000/',
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