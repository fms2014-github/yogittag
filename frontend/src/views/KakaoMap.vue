<template>
    <div>
        <search-bar />
        <div id="gps-button" class="radius-button">
            <button @click="gpsFocus">
                <img src="@/assets/icons/gps.png" style="width:2.3em;" />
            </button>
        </div>
        <div id="map" />
    </div>
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
</style>

<script>
import searchBar from '../components/Search.vue'

export default {
    data() {
        return {
            latitude : 0,
            longitude : 0,
            map: {}
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

        this.gpsFocus();
        
    },
    methods:{
        gpsFocus(){
            
            if(navigator.geolocation){

            navigator.geolocation.getCurrentPosition (pos => {
                this.latitude = pos.coords.latitude;
                this.longitude = pos.coords.longitude;

                console.log("dd");

                var imageSrc = require('@/assets/icons/rec.png'),
                imageSize = new kakao.maps.Size(34, 39), // 마커이미지의 크기입니다
                imageOption = {offset: new kakao.maps.Point(17, 39)}; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.
      
                // 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
                var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
                    markerPosition = new kakao.maps.LatLng(this.latitude, this.longitude); // 마커가 표시될 위치입니다

                // 마커를 생성합니다
                var marker = new kakao.maps.Marker({
                    position: markerPosition, 
                    image: markerImage // 마커이미지 설정 
                });

                // 마커가 지도 위에 표시되도록 설정합니다
                marker.setMap(this.map);
                this.map.setCenter(markerPosition);      
            });

        }
        }
    }
}
</script>
