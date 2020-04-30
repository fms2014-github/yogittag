<template>
    <v-container class="mt-5" fill-height>
        <v-card-text class="text-center">
            <p class="display-2 pa-5" style="font-family: h1c;">🍜 코딩도 식후경</p>
            <banner />

            <v-btn
                class="display-1 font-italic font-weight-bold"
                large
                style="font-family: 'Inconsolata';"
                @click="getLocation"
            >요기딱!</v-btn>
            <food-friend :tags.sync="tags" />
            <slider title="나의 단골 맛집" :cardData="cardData" />
            <slider title="지인 추천 맛집" />
        </v-card-text>
    </v-container>
</template>

<script>
import Banner from '../components/home_components/Banner'
import FoodFriend from '../components/home_components/FoodFriend'
import Slider from '../components/home_components/Slider'
import axiosApi from '@/api/axiosScript.js'

export default {
    components: {
        Banner,
        FoodFriend,
        Slider,
    },
    data() {
        return {
            cardData: [
                {
                    title: 'TITLE',
                    content: 'CONTENT',
                },
                {
                    title: 'TITLE2',
                    content: 'CONTENT2',
                },
                {
                    title: 'TITLE3',
                    content: 'CONTENT3',
                },
                {
                    title: 'TITLE4',
                    content: 'CONTENT4',
                },
                {
                    title: 'TITLE5',
                    content: 'CONTENT5',
                },
                {
                    title: 'TITLE6',
                    content: 'CONTENT6',
                },
            ],

            tags: [],
            //map: {},
            position: {}
        }
    },
    mount() {
        // this.map = new kakao.maps.Map(container, options) //지도 생성 및 객체 리턴
    },
    methods: {
        recommand(){
            let user = []
            for (let i=0; i<this.tags.length; i++){
                user.push(this.tags[i].id)
            }
        
            let data = {
                id : 68632,
                latitude : this.position.latitude,
                longitude : this.position.longitude,
                area : this.position.area,
                users : user
            }

            console.log(data)

            axiosApi.getRecommandationById(
                data,
                (res) => {
                    console.log(res.data)
                    this.cardData = res.data
                    this.cardData.forEach( card => {
                        if (card.pictures != null) {
                            card.pictures = card.pictures.split("|");
                        }
                        else {
                            card.pictures = ""
                        }
                    })
                },
                (err) => {
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
</style>
