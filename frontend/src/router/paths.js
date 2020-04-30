export default [
    {
        path: '/',
        view: 'Home',
        name: 'Home',
    },
    {
        path: '/map',
        view: 'Map',
        name: 'Map',
    },
    {
        path: '/test',
        view: 'test1',
        name: 'test',
    },
    {
        path: '/google-auth',
        view: 'GoogleAuth',
        name: 'GoogleAuth',
    },
    {
        path: '/naver-auth',
        view: 'NaverAuth',
        name: 'NaverAuth',
    },
    {
        path: '/store/:id',
        view: 'StoreDetailPage',
        name: 'StoreDetailPage',
    },
    {
        path: '/listPage/:keyword',
        view: 'ListPage',
        name: 'ListPage',
        props: true,
    },
    {
        path: '/profile',
        view: 'Profile',
        name: 'Profile',
    },
]
