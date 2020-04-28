<template>
    <div style="padding-top: 30px;">
        <!-- Page Content -->
        <div class="container">
            <div class="row">
                <div class="col-lg-3">
                    <h1 class="my-4" style="font-family: h1c;">{{ storeName }}🍽</h1>
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
                    <Carousel :imgs="pictures" />
                </div>
            </div>
            <div>
                <b-tabs
                    active-nav-item-class="font-weight-bold text-uppercase text-danger"
                    content-class="mt-3"
                    style="padding-bottom: 10px;"
                >
                    <b-tab title="Home" active>
                        <StoreInfoTable class="store-detail-component" :items="storeData" />
                        <div
                            class="store-detail-component"
                            id="map"
                            style="width: 100%; height: 350px;"
                        ></div>
                        <div class="store-detail-component">
                            <b-badge pill variant="secondary">{{
                                bhour.week_type | weekType
                            }}</b-badge>
                            <b-badge pill :variant="bhour.mon ? 'info' : 'light'">월</b-badge>
                            <b-badge pill :variant="bhour.tue ? 'info' : 'light'">화</b-badge>
                            <b-badge pill :variant="bhour.wed ? 'info' : 'light'">수</b-badge>
                            <b-badge pill :variant="bhour.thu ? 'info' : 'light'">목</b-badge>
                            <b-badge pill :variant="bhour.fri ? 'info' : 'light'">금</b-badge>
                            <b-badge pill :variant="bhour.sat ? 'info' : 'light'">토</b-badge>
                            <b-badge pill :variant="bhour.sun ? 'info' : 'light'">일</b-badge>

                            <div v-if="bhour.type == 1">
                                <b-badge pill variant="success">
                                    OPEN
                                    {{ bhour.start_time | dateFilter }}
                                    ~
                                    {{ bhour.end_time | dateFilter }}</b-badge
                                >
                            </div>
                            <div v-else-if="bhour.type == 2">
                                <b-badge pill variant="warning">
                                    BREAK TIME
                                    {{ bhour.start_time | dateFilter }}
                                    ~
                                    {{ bhour.end_time | dateFilter }}</b-badge
                                >
                            </div>
                            <b-badge pill variant="danger">{{ bhour.etc }}</b-badge>
                        </div>
                    </b-tab>
                    <b-tab title="Menu">
                        <SortingTable :fields="MenuKeyData" :items="MenuData" />
                    </b-tab>
                    <b-tab title="Reviews">
                        <div class="row">
                            <small-card
                                v-for="item in cardDate"
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
                        <button v-b-modal.modal id="registerButton">
                            <img id="registerButtonImg" :src="registerRiviewImg" />
                        </button>
                        <b-modal
                            :no-close-on-backdrop="true"
                            @ok="modalCilck()"
                            id="modal"
                            size="lg"
                            title="Review"
                            ><ReviewForm
                        /></b-modal>
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
import StoreInfoTable from '@/components/tables/StoreInfoTable'
import dateFilter from '@/components/filters/dateFilter.js'
import UpFocusButton from '@/components/buttons/UpFocusButton'
import ReviewForm from '@/components/forms/ReviewForm.vue'
import axios from '../api/axiosScript.js'

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
            bhour: {},
            cardDate: [],
            MenuKeyData: [
                { key: 'Food', sortable: true },
                { key: 'Price', sortable: true },
            ],
            MenuData: [],
            storeEtcInfo: {
                group_seat: null,
                reservation: null,
                delivery: null,
                take_away: null,
                parking: null,
            },
            storeData: [
                {
                    Branch: null,
                    Area: null,
                    Tel: null,
                    Address: null,
                },
            ],
            storeName: null,
            latitude: null,
            longitude: null,
            categorys: ['Category 1', 'Category 2', 'Category 3'],
            pictures: null,
            registerRiviewImg: require('@/assets/icons/registerReview.png'),
            pMap: null,
            scrollY: 0,
            timer: null,
            ux: {
                rBtnFlag: false,
            },
        }
    },
    components: {
        SmallCard,
        Carousel,
        SortingTable,
        StoreInfoTable,
        UpFocusButton,
        ReviewForm,
    },
    mounted() {
        this.aixos(this.$route.params.id)
    },
    created: function () {
        window.addEventListener('scroll', this.handleScroll)
    },
    beforeDestroy: function () {
        window.removeEventListener('scroll', this.handleScroll)
    },
    methods: {
        handleScroll() {
            if (this.timer === null) {
                this.timer = setTimeout(
                    function () {
                        this.scrollY = window.scrollY || document.documentElement.scrollTop
                        this.registerButtonUX(this.scrollY)
                        clearTimeout(this.timer)
                        this.timer = null
                    }.bind(this),
                    200,
                )
            }
        },
        registerButtonUX(scrollPosition) {
            var rb = document.getElementById('registerButtonImg')
            if (scrollPosition > 200 && !this.ux.rBtnFlag) {
                var player = rb.animate(
                    [{ transform: 'translate(0)' }, { transform: 'translate(0,-50px)' }],
                    150,
                )
                player.addEventListener('finish', function () {
                    rb.style.transform = 'translate(0,-50px)'
                })
                this.ux.rBtnFlag = true
            } else if (scrollPosition <= 200 && this.ux.rBtnFlag) {
                var player = rb.animate(
                    [{ transform: 'translate(0,-50px)' }, { transform: 'translate(0)' }],
                    150,
                )
                player.addEventListener('finish', function () {
                    rb.style.transform = 'translate(0)'
                })
                this.ux.rBtnFlag = false
            }
        },
        relayout() {
            // 지도를 표시하는 div 크기를 변경한 이후 지도가 정상적으로 표출되지 않을 수도 있습니다
            // 크기를 변경한 이후에는 반드시  map.relayout 함수를 호출해야 합니다
            // window의 resize 이벤트에 의한 크기변경은 map.relayout 함수가 자동으로 호출됩니다
            this.pMap.relayout()
            // 이동할 위도 경도 위치를 생성합니다
            var moveLatLon = new kakao.maps.LatLng(this.latitude, this.longitude)

            // 지도 중심을 이동 시킵니다
            this.pMap.setCenter(moveLatLon)
            // this.pMap.panTo(moveLatLon)
        },
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
            this.pMap = map
        },
        modalCilck(bvModalEvt) {
            console.log('modal ok click')
        },
        aixos(store_id) {
            axios.getStore(
                store_id,
                (res) => {
                    let resData = res.data.result[0]
                    this.storeName = resData.store_name
                    this.latitude = resData.latitude
                    this.longitude = resData.longitude
                    this.categorys = resData.category.split('|')
                    ;(this.storeData = [
                        {
                            Branch: resData.branch,
                            Area: resData.area,
                            Tel: resData.tel,
                            Address: resData.address,
                        },
                    ]),
                        (this.pictures = resData.pictures.split('|')),
                        (this.storeEtcInfo = {
                            group_seat: resData.group_seat,
                            reservation: resData.reservation,
                            delivery: resData.delivery,
                            take_away: resData.take_away,
                            parking: resData.parking,
                        })
                    this.createKakaoMap(this.storeName, this.latitude, this.longitude)
                },
                (err) => {
                    console.log(`getStore Data loading fail...`)
                },
            )
            axios.getStoreHour(
                store_id,
                (res) => {
                    this.bhour = res.data.result[0]
                },
                (error) => {
                    console.log(`getStoreHour Data loading fail...`)
                },
            )
            axios.getStoreReview(store_id, (res) => {
                // this.cardDate = res.data.result

                for (let r of res.data.result) {
                    this.cardDate.push({
                        title: r.user_id.toString(),
                        routing: `/profile/${r.user_id}/review`,
                        score: r.score,
                        content: r.content,
                        reg_time: r.reg_time,
                    })
                }
            })
            axios.getStoreMenu(store_id, (res) => {
                for (let m of res.data.result) {
                    this.MenuData.push({
                        Food: m.menu_name,
                        Price: m.price,
                    })
                }
            })
        },
    },
}
</script>

<style>
.store-detail-component {
    margin: 5px;
}
#registerButtonImg {
    animation: fadein 1s;
    position: fixed;
    bottom: 50px;
    right: 50px;
    height: 40px;
    width: 40px;
    z-index: 10;
    border: 1px solid #ddd;
    border-radius: 100%;
}
@keyframes fadein {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
#scroll {
    position: fixed;
    bottom: 150px;
    right: 50px;
    height: 40px;
    z-index: 10;
}
@font-face {
    font-family: h1c;
    src: url('../assets/fonts/DXRMbxB-KSCpc-EUC-H.ttf');
}
</style>
