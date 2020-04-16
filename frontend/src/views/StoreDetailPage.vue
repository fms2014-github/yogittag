<template>
    <div style="padding-top: 30px;">
        <!-- Page Content -->
        <div class="container">
            <div class="row">
                <div class="col-lg-3">
                    <h1 class="my-4">{{ storeName }}</h1>
                    <div class="list-group">
                        <router-link
                            to="#"
                            v-for="item in categorys"
                            :key="item.id"
                            class="list-group-item"
                        >
                            {{ item }}
                        </router-link>
                    </div>
                </div>

                <div class="col-lg-9">
                    <Carousel />
                </div>
            </div>
            <div>
                <b-tabs
                    active-nav-item-class="font-weight-bold text-uppercase text-danger"
                    content-class="mt-3"
                    style="padding-bottom: 10px;"
                >
                    <b-tab title="Home" active>
                        <StackedTable :items="testStoreData" />
                        <div id="map" style="width: 100%; height: 350px;"></div>
                        <div>
                            <b-badge pill variant="secondary">{{
                                testBHour.week_type | weekType
                            }}</b-badge>
                            <b-badge pill :variant="testBHour.mon ? 'info' : 'light'">월</b-badge>
                            <b-badge pill :variant="testBHour.tue ? 'info' : 'light'">화</b-badge>
                            <b-badge pill :variant="testBHour.wed ? 'info' : 'light'">수</b-badge>
                            <b-badge pill :variant="testBHour.thu ? 'info' : 'light'">목</b-badge>
                            <b-badge pill :variant="testBHour.fri ? 'info' : 'light'">금</b-badge>
                            <b-badge pill :variant="testBHour.sat ? 'info' : 'light'">토</b-badge>
                            <b-badge pill :variant="testBHour.sun ? 'info' : 'light'">일</b-badge>

                            <div v-if="testBHour.type == 1">
                                <b-badge pill variant="success">
                                    OPEN
                                    {{ testBHour.start_time | dateFilter }}
                                    ~
                                    {{ testBHour.end_time | dateFilter }}</b-badge
                                >
                            </div>
                            <div v-else-if="testBHour.type == 2">
                                <b-badge pill variant="warning">
                                    BREAK TIME
                                    {{ testBHour.start_time | dateFilter }}
                                    ~
                                    {{ testBHour.end_time | dateFilter }}</b-badge
                                >
                            </div>
                            <b-badge pill variant="danger">{{ testBHour.etc }}</b-badge>
                        </div>
                    </b-tab>
                    <b-tab title="Menu">
                        <SortingTable :fields="testMenuKeyData" :items="testMenuData" />
                    </b-tab>
                    <b-tab title="Reviews">
                        <div class="row">
                            <small-card
                                v-for="item in testCardDate"
                                :key="item.id"
                                :routing="item.routing"
                                :img="item.img"
                                :gender="item.gender"
                                :title="item.title"
                                :reg_time="item.reg_time"
                                :content="item.content"
                                :score="item.score"
                            />
                        </div>
                        <button v-b-modal.modal>
                            <img id="registerButton" :src="registerRiviewImg" />
                        </button>
                        <b-modal :no-close-on-backdrop="true" @ok="modalCilck()" id="modal" size="lg" title="Review"><ReviewForm /></b-modal>
                    </b-tab>
                </b-tabs>
            </div>
        </div>
        <UpFocusButton />
    </div>
</template>

<script>
import SmallCard from '@/components/cards/SmallCard'
import Carousel from '@/components/showPictures/Carousel'
import SortingTable from '@/components/tables/SortingTable'
import StackedTable from '@/components/tables/StackedTable'
import dateFilter from '@/components/filters/dateFilter.js'
import UpFocusButton from '@/components/buttons/UpFocusButton'
import infiniteScroll from 'vue-infinite-scroll'
import ReviewForm from '@/components/forms/ReviewForm.vue'

export default {
    filters: {
        dateFilter: dateFilter,
        weekType: function (val) {
            switch (val) {
                case 1:
                    return '매주'
                case 2:
                    return '첫째주'
                case 3:
                    return '둘째주'
                case 4:
                    return '셋째주'
                case 5:
                    return '넷째주'
                case 6:
                    return '공휴일'
            }
        },
    },
    data() {
        return {
            badgesColor: {
                light: 'light',
                mint: 'info',
            },
            testBHour: {
                type: 1,
                week_type: 1,
                mon: 0,
                tue: 1,
                wed: 1,
                thu: 1,
                fri: 1,
                sat: 1,
                sun: 1,
                start_time: '10:00:00',
                end_time: '21:00:00',
                etc: '매주 일요일 휴무',
            },
            testCardDate: [
                {
                    routing: '/',
                    img: 'https://loremflickr.com/700/400',
                    gender: '남',
                    title: 'Reivew Title',
                    reg_time: '2020-04-09 03:48:40.799058',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                    score: 4,
                },
                {
                    routing: '#',
                    img: 'https://picsum.photos/700/400',
                    gender: '여',
                    title: 'Reivew Title2',
                    reg_time: '2020-04-09 03:48',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                    score: 1,
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
                {
                    title: 'Reivew Title3',
                    content:
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
                },
            ],
            testMenuKeyData: [
                { key: 'Food', sortable: true },
                { key: 'Price', sortable: true },
            ],
            testMenuData: [
                { Food: '아메리카노', Price: '1,000' },
                { Food: '핫초코', Price: '13,500' },
                { Food: '고기국수', Price: '6,000' },
                { Food: '생맥주', Price: '7,000' },
            ],
            testStoreData: [
                {
                    Branch: null,
                    Area: '홍대',
                    Tel: '010-6689-5886',
                    Address: '서울특별시 마포구 동교동 170-13',
                },
            ],
            storeName: 'Shop Name',
            latitude: 37.556862,
            longitude: 126.926666,
            categorys: ['Category 1', 'Category 2', 'Category 3'],
            registerRiviewImg: require('@/assets/icons/registerReview.png'),
        }
    },
    components: {
        SmallCard,
        Carousel,
        SortingTable,
        StackedTable,
        UpFocusButton,
        infiniteScroll,
        ReviewForm,
    },
    mounted() {
        this.createKakaoMap(this.storeName, this.latitude, this.longitude)
    },
    methods: {
        createKakaoMap(storeName, lat, lng) {
            var container = document.getElementById('map')
            var options = {
                center: new kakao.maps.LatLng(lat, lng),
                level: 3,
            }

            var map = new kakao.maps.Map(container, options)

            // 마커가 표시될 위치입니다
            var markerPosition = new kakao.maps.LatLng(lat, lng)

            // 마커를 생성합니다
            var marker = new kakao.maps.Marker({
                position: markerPosition,
            })

            // 마커가 지도 위에 표시되도록 설정합니다
            marker.setMap(map)

            var iwContent = `<div style="padding:5px;">${storeName}<br><a href="https://map.kakao.com/link/map/${storeName},${lat},${lng}" style="color:blue" target="_blank">큰지도보기</a> <a href="https://map.kakao.com/link/to/${storeName},${lat},${lng}" style="color:blue" target="_blank">길찾기</a></div>`, // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
                iwPosition = new kakao.maps.LatLng(lat, lng) //인포윈도우 표시 위치입니다

            // 인포윈도우를 생성합니다
            var infowindow = new kakao.maps.InfoWindow({
                position: iwPosition,
                content: iwContent,
            })

            // 마커 위에 인포윈도우를 표시합니다. 두번째 파라미터인 marker를 넣어주지 않으면 지도 위에 표시됩니다
            infowindow.open(map, marker)
        },
        modalCilck(bvModalEvt){
            console.log('modal ok click');
        }
    },
}
</script>

<style>
#registerButton {
    position: fixed;
    bottom: 100px;
    right: 50px;
    height: 40px;
    width: 40px;
    z-index: 10;
    border: 1px solid #ddd;
    border-radius: 100%;
}
</style>
