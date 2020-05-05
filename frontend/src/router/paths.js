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
        path: '/detail-profile',
        view: 'Auth',
        name: 'Auth',
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
    {
        path: '/profile/:id',
        view: 'Profile',
        name: 'ProfileById',
        props: true,
    },
]
