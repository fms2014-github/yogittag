<template>
    <!-- Page Content -->
    <div class="container" style="padding-top: 30px;">
        <!-- Page Heading -->
        <h1 class="my-4" style="text-align: center; font-family: h1c;">
            {{ title }}
        </h1>
        <h5>{{subTitle}}</h5>
        <div class="row">
            <SmallCard
                v-for="item in cardData"
                :key="item.id"
                :routing="item.routing"
                :img="item.img"
                :gender="item.gender"
                :title="item.title"
                :reg_time="item.reg_time"
                :content="item.content"
                :score="parseInt(item.score)"
            />
        </div>
        <div class="d-flex justify-content-center mt-5">
            <b-spinner
                class="mt-5"
                style="width: 3rem; height: 3rem;"
                label="Large Spinner"
                variant="primary"
                v-if="resData == null"
            ></b-spinner>
        </div>
        <!-- /.row -->
    </div>
    <!-- /.container -->
</template>

<script>
import SmallCard from '@/components/cards/SmallCard'
import axios from '@/api/axiosScript.js'

export default {
    props: {
        pTitle: {
            type: String,
        },
        pSubTitle: {
            type: String,
        },
        pCardData: {
            type: Array,
        },
    },

    data() {
        return {
            keyword: this.$route.params.keyword,
            title: this.$route.query.title,
            subTitle: this.$route.query.subTitle,
            cardData: [],
            latitude: 0,
            longitude: 0,
            distance: 2000,
            category: null,
            area: null,
            resData: null,
        }
    },
    components: {
        SmallCard,
    },
    mounted() {
        if (this.keyword == null) {
            this.keyword = this.pTitle
            this.title = this.pTitle
            this.subTitle = this.pSubTitle
            this.cardData = this.pCardData
        }

        this.gpsFocus()
    },
    methods: {
        gpsFocus() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition((pos) => {
                    this.latitude = pos.coords.latitude
                    this.longitude = pos.coords.longitude
                    this.searchByKeywordStore()
                }, { enableHighAccuracy: true })
            }
        },
        searchByKeywordStore() {
            axios.searchStore(
                {
                    keyword: this.keyword,
                    latitude: this.latitude,
                    longitude: this.longitude,
                    distance: this.distance,
                    category: this.category,    
                    area: this.area,

                },
                (res) => {
                    console.log(`success`)
                    this.resData = res.data.result
                    for (let s of res.data.result) {
                        if(s.pictures == null || s.pictures == ''){
                             this.cardData.push({
                                routing: `/store/${s.id}`,
                                title: s.store_name,
                                reg_time: s.area,
                                content: s.address,
                            })
                        }else{
                            this.cardData.push({
                                routing: `/store/${s.id}`,
                                img: s.pictures.split('|')[0],
                                title: s.store_name,
                                reg_time: s.area,
                                content: s.address,
                            })
                        }
                    }
                },
                (err) => {
                    console.log(err)

                    console.log(`list page search by keyword store error`)
                },
            )
        },
    },
}
</script>

<style>
@font-face {
    font-family: h1c;
    src: url('../assets/fonts/DXRMbxB-KSCpc-EUC-H.ttf');
}
</style>
