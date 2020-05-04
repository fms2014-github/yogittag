<template>
    <v-container class="mt-5" fill-height>
        <v-card-text class="text-center">
            <img height="300px;" src="@/assets/img/main_logo.png" alt="요기딱" />
            <banner />

            <v-btn
                class="display-1 font-italic font-weight-bold"
                large
                style="font-family: 'Inconsolata';"
                @click="getLocation"
                v-if="userid!=0"
            >요기딱!</v-btn>
            <food-friend v-if="userid!=0" :tags.sync="tags" />
            <slider v-if="userid!=0" title="맞춤 추천 맛집" :cardData="cardData" />
            <slider v-if="userid!=0" title="지인 추천 맛집" :cardData="cardData2" />
        </v-card-text>
    </v-container>
</template>

<script>
import Banner from '../components/home_components/Banner'
import FoodFriend from '../components/home_components/FoodFriend'
import Slider from '../components/home_components/Slider'
import axiosApi from '@/api/axiosScript.js'
import { mapMutations, mapState, mapGetters } from 'vuex'

export default {
    components: {
        Banner,
        FoodFriend,
        Slider,
    },
    data() {
        return {
            cardData: [],
            cardData2 :[],
            tags: [],
            //map: {},
            position: {},
            userid: 0
        }
    },
    mounted() {

        if(sessionStorage.getItem('session') != null){
            this.userid = JSON.parse(sessionStorage.getItem('session')).userid
        }
        
        // 지인 추천 로그인되어있는지 확인해야하눈뎅
        if(this.userid != 0){
            axiosApi.getRecommandationByFollowers(
                this.userid,
                (res)=>{
                    console.log(res.data)
                    this.cardData2 = res.data
                    this.cardData2.forEach( card => {
                        if (card.pictures) {
                            card.pictures = card.pictures.split("|");
                        }
                    })
                },
                (err)=>{
                    console.log(err)
                }
            )
        }



        // this.map = new kakao.maps.Map(container, options) //지도 생성 및 객체 리턴
    },
    methods: {
        ...mapMutations('app', ['loadingSpinner', 'initState']),

        recommand(){
            let user = []
            for (let i=0; i<this.tags.length; i++){
                user.push(this.tags[i].key)
            }
        
            let data = {
                id : this.userid,
                latitude : this.position.latitude,
                longitude : this.position.longitude,
                area : this.position.area,
                users : user
            }

            console.log(data)

            this.initState()
            this.loadingSpinner()
            axiosApi.getRecommandationById(
                data,
                (res) => {
                    this.loadingSpinner()
                    console.log(res.data)
                    
                    this.cardData = res.data
                    this.cardData.forEach( card => {
                        if (card.pictures) {
                            card.pictures = card.pictures.split("|");
                        }
                    })
                },
                (err) => {
                    this.loadingSpinner()
                    console.log(err)
                }
            )
        },
        getLocation(){
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition((pos) => {
                    this.position.latitude = pos.coords.latitude
                    this.position.longitude = pos.coords.longitude

                    var geocoder = new kakao.maps.services.Geocoder()
                    console.log(geocoder)
                    // 현재 지도 중심좌표로 주소를 검색해서 지도 좌측 상단에 표시합니다
                    geocoder.coord2RegionCode(this.position.longitude, this.position.latitude, (result, status)=>{

                        console.log(result)
                        if (status == kakao.maps.services.Status.OK) {
                            this.position.area = result[0].region_2depth_name
                            this.recommand()
                        }
                    });        
                })
            }
        }
    
    },
}
    
</script>

<style scoped>
@font-face {
    font-family: h1c;
    src: url('../assets/fonts/DXRMbxB-KSCpc-EUC-H.ttf');
}
@font-face {
    font-family: 'Dovemayo-Medium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_four@1.0/Dovemayo-Medium.woff')
        format('woff');
    font-weight: normal;
    font-style: normal;
}

* {
    font-family: 'Dovemayo-Medium';
}
</style>
