<template>
    <v-app>
        <search-bar
            :latitude="latitude"
            :longitude="longitude"
            :result.sync="result"
            v-on:mouseoverid="getMouseoverId"
        />
        <!-- <div id="search-result-wrap" class="search-result-wrap">
            <div id="search-result" v-for="(item, index) in test" v-bind:key="index">
                <strong>{{ item.store_name }}</strong>
                <br />
                <span>{{item.category}}</span>
                <br />
                <small>{{item.address}}</small>
            </div>
        </div>-->
        <div id="gps-button" class="radius-button">
            <button @click="gpsFocus">
                <img src="@/assets/icons/gps.png" style="width: 2.3em;" />
            </button>
        </div>
        <div id="map" />

        <div id="menu_wrap" class="bg_white">
            <ul id="placesList"></ul>
            <div id="pagination"></div>
        </div>
    </v-app>
</template>
<style lang="scss" scoped>
#map {
    width: 100vw;
    height: 100vh;
}

#gps-button {
    position: absolute;
    padding: 10px;
    bottom: 100px;
    top: 90%;
    right: 2%;
    z-index: 10;
}

/* #search {
    position: absolute;
    top: 5em;
    left: 20vw;
    transform: translateX(-50%);
    background-color: white;
    width: 35vw;
    max-width: 35vw;
    z-index: 10;
} */

#search-result-wrap {
    position: absolute;
}
</style>

<script>
import searchBar from '@/components/map_components/Search.vue'

function clickListener(id){
    this.goToDetail(id);
}

export default {
    data() {
        return {
            latitude: 0,
            longitude: 0,
            map: {},
            result: [],
            markers: [],
            infowindows: [],
            preid: -1,
            bounds : {},
            count : 0
        }
    },
    components: {
        searchBar,
    },
    mounted() {
        var container = document.getElementById('map') //지도를 담을 영역의 DOM 레퍼런스
        var options = {
            //지도를 생성할 때 필요한 기본 옵션
            center: new kakao.maps.LatLng(this.latitude, this.longitude), //지도의 중심좌표. 33.450701, 126.570667
            level: 3, //지도의 레벨(확대, 축소 정도)
        }

        // eslint-disable-next-line no-unused-vars
        this.map = new kakao.maps.Map(container, options) //지도 생성 및 객체 리턴

        this.gpsFocus()
    },
    watch: {
        result: function (v) {
            this.addBasicMarker()
        },
    },
    methods: {
        gpsFocus() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition((pos) => {
                    this.latitude = pos.coords.latitude
                    this.longitude = pos.coords.longitude

                    var imageSrc = require('@/assets/icons/rec.png'),
                        imageSize = new kakao.maps.Size(25, 25), // 마커이미지의 크기입니다
                        imageOption = { offset: new kakao.maps.Point(9, 9) } // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.

                    // 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
                    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
                        markerPosition = new kakao.maps.LatLng(this.latitude, this.longitude) // 마커가 표시될 위치입니다

                    // 마커를 생성합니다
                    var marker = new kakao.maps.Marker({
                        position: markerPosition,
                        image: markerImage, // 마커이미지 설정
                    })

                    // 마커가 지도 위에 표시되도록 설정합니다
                    marker.setMap(this.map)
                    this.map.setCenter(markerPosition)
                })
            }
        },

        // 가장 기본형태로 해보자
        addBasicMarker() {
            for (var i = 0; i < this.markers.length; i++) {
                this.markers[i].setMap(null)
            }
            this.markers = []
            this.infowindows = []

            if(this.result.length == 0){
                return
            }

            this.bounds = new kakao.maps.LatLngBounds();    

            for (let i = 0; i < this.result.length; i++) {
                // 마커가 표시될 위치입니다
                var markerPosition = new kakao.maps.LatLng(
                    this.result[i].latitude,
                    this.result[i].longitude,
                )

                // 마커를 생성합니다
                var marker = new kakao.maps.Marker({
                    position: markerPosition,
                    title: this.result[i].id,
                    clickable: true
                })
                this.markers.push(marker)

                // 마커가 지도 위에 표시되도록 설정합니다
                marker.setMap(this.map)

                // LatLngBounds 객체에 좌표를 추가합니다
                this.bounds.extend(markerPosition);

                var iwContent = '<div style="padding:5px;">' + this.result[i].store_name + '</div>'
                //iwPosition = new kakao.maps.LatLng(this.result[i].latitude, this.result[i].longitude)

                // 인포윈도우를 생성합니다
                var infowindow = new kakao.maps.InfoWindow({
                    //position : iwPosition,
                    content: iwContent,
                })
                this.infowindows.push(infowindow)


                
                // 마우스 오버 아웃 이벤트 등록
                kakao.maps.event.addListener(
                    marker,
                    'mouseover',
                    this.makeOverListener(this.map, marker, infowindow),
                )
                kakao.maps.event.addListener(marker, 'mouseout', this.makeOutListener(infowindow))

                // 마커에 클릭이벤트를 등록합니다
                kakao.maps.event.addListener(marker, 'click', this.goToDetail(marker.mc))

            }
            this.setBounds();
        },

        makeOverListener(map, marker, infowindow) {
            return function () {
                infowindow.open(map, marker)
            }
        },

        // 인포윈도우를 닫는 클로저를 만드는 함수입니다
        makeOutListener(infowindow) {
            return function () {
                infowindow.close()
            }
        },

        // Search 리스트에서 마우스 오버 했을때 마커에도 마우스 오버 되도록하는 함수
        getMouseoverId(value) {
            //console.log(value);
            if (value == -1) {
                for (let i = 0; i < this.markers.length; i++) {
                    //console.log('this is mc : '+ this.markers[i].mc)
                    if (this.markers[i].mc == this.preid) {
                        this.infowindows[i].close()
                    }
                }
            } else {
                for (let i = 0; i < this.markers.length; i++) {
                    //console.log('this is mc : '+ this.markers[i].mc)
                    if (this.markers[i].mc == value) {
                        this.infowindows[i].open(this.map, this.markers[i])
                    }
                }
                this.preid = value
            }
        },

        setBounds() {
            // LatLngBounds 객체에 추가된 좌표들을 기준으로 지도의 범위를 재설정합니다
            // 이때 지도의 중심좌표와 레벨이 변경될 수 있습니다
            this.map.setBounds(this.bounds);
        },
        
        goToDetail(id){ 
            return ()=>{
                this.$router.push('/store-detail-page/'+ id);
            }
            
        }
    },
}
</script>
