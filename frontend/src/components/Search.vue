<template>
    <div id="search">
        <div id="search-bar" class="search-bar">
            <input
                id="search-bar-input"
                v-model="keyword"
                @keyup.enter="findData"
                placeholder="입력하세요"
                type="text"
            />

            <button id="search-button" @click="findData" style="float:left;">
                <span class="material-icons">search</span>
            </button>
            <!-- <button id="filter-button">
                <span class="material-icons" @click="openFilter">filter_list</span>
                <span id="is-filter" v-show="useFilter">필터 사용</span>
            </button>-->
            <hr />
            <!-- <filter-list />
            <hr />-->
            <v-chip-group multiple active-class="primary--text">
                <v-chip v-for="tag in tags" :key="tag" @click="tagClick">{{ tag }}</v-chip>
            </v-chip-group>
            <div
                v-show="isshow"
                style="display:block; width:100%;opacity: 0.65;background: white; max-height:30em;overflow-y:scroll;"
            >
                <div id="search-result" v-for="item in result" v-bind:key="item.id">
                    <strong>{{item.store_name}}</strong>
                    <br />
                    <small>{{item.category}}</small>
                    <br />
                    <small>{{item.address}}</small>
                    <hr />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import filterList from '../components/FilterList.vue'
import axiosApi from '../api/axiosScript.js'
import { mapMutations, mapState, mapGetters } from 'vuex'
export default {
    props:{
        latitude : {
            type : Number,
            require : true
        },
        longitude : {
            type : Number,
            require : true
        }
    },
    data() {
        return {
            keyword:'',
            result: [],
            isshow: false,
            tags: [
                '음식점',
                '카페',
                '술집',
                '300m',
                '500m',
                '1km'
            ],
        }
    },
    components: {
        filterList,
    },
    computed: {
        //...mapGetters('app', ['useFilter']),
    },
    methods: {
        ...mapMutations('app', ['loadingSpinner', 'initState']),
        openFilter() {
            document.getElementById('search-bar').classList.toggle('open-filter')
        },
        async findData() {
            let data = {
                keyword : this.keyword,
                latitude : this.latitude,
                longitude : this.longitude
            }
            this.initState()
            this.loadingSpinner()
            await axiosApi.searchAxios(
                data,
                (res) => {
                    this.loadingSpinner()
                    //console.log(res.data)
                    this.result = res.data.result
                    this.isshow = true
            

                },
                (err) => {
                    this.loadingSpinner()
                    console.log(err.data)
                },
            )
            //console.log(this.test)
        },

        tagClick(event){
            //console.log(event)
            console.log(event.target.innerText)
        }
    },
}
</script>

<style lang="scss" scoped>
#search {
    position: absolute;
    left: 50vw;
    top: 36px;
    transform: translateX(-50%);
    background-color: white;
    width: 50vw;
    max-width: 500px;
    z-index: 10;
    .search-bar {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        flex-wrap: wrap;
        padding: 0 1vw;
        width: 100%;
        height: 48px;
        border-radius: 7px;
        //overflow: hidden;
        box-shadow: 0px 0px 4px 2px rgba(128, 128, 128, 0.7);
        #search-bar-input {
            width: calc(100% - 112px);
            //margin-top: 10px;
            height: 48px;
            font-size: 15pt;
        }
        hr {
            margin-top: 8px;
            width: 100%;
            border: {
                width: 1px;
                style: dots;
                color: rgba(128, 128, 128, 0.4);
            }
        }
        #is-filter {
            position: absolute;
            top: 2px;
            right: 14px;
            font-size: 0.5rem;
            padding: 3px;
            background-color: rgb(235, 133, 0);
            border-radius: 4px;
            box-shadow: inset 0 0 4px 2px rgba(255, 255, 255, 0.5);
            color: rgb(255, 255, 255);
        }
        .material-icons {
            margin-left: 18px;
            margin-top: 8px;
            font-size: 38px;
        }
    }
}

#search-result {
    z-index: 10;
}
</style>
