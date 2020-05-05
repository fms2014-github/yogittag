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

            <button id="search-button" @click="findData" style="float: left;">
                <span class="material-icons">search</span>
            </button>

            <button id="filter-button">
                <span class="material-icons" @click="useFilter = !useFilter">filter_list</span>
                <span id="is-filter" v-show="useFilter">필터 사용</span>
            </button>

            <v-chip-group
                multiple
                active-class="deep-purple--text text--accent-4"
                v-show="useFilter"
            >
                <v-chip color="white" v-for="tag in tags" :key="tag" @click="tagClick">
                    {{
                    tag
                    }}
                </v-chip>
            </v-chip-group>
            <div
                v-show="useFilter"
                style="
                    display: block;
                    margin-top: 10px;
                    width: 100%;
                    opacity: 0.7;
                    background: white;
                    max-height: 25em;
                    overflow-y: scroll;
                "
            >
                <div
                    id="search-result"
                    v-for="item in result"
                    v-bind:key="item.id"
                    v-on:mouseover="mouseOver(item.id)"
                    v-on:mouseout="mouseOut(item.id)"
                    @click="goToDetail(item.id)"
                >
                    <strong>{{ item.store_name }}</strong>
                    <br />
                    <small>{{ item.category }}</small>
                    <br />
                    <small>{{ item.address }}</small>
                    <hr />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axiosApi from '@/api/axiosScript.js'
import { mapMutations } from 'vuex'
export default {
    props: {
        latitude: {
            type: Number,
            require: true,
        },
        longitude: {
            type: Number,
            require: true,
        },
        area: {
            type : String,
            require : true
        }
    },
    data() {
        return {
            keyword: '',
            result: [],
            tags: ['음식점', '카페', '술집', '500m', '1km', '2km'],
            selectedTags: [],
            useFilter: false,
        }
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
            if(this.keyword !== ''){
                let distance = 500
                let category = []
                for (let i = 0; i < this.selectedTags.length; i++) {
                    if (this.selectedTags[i] == '500m' && distance <= 500) {
                        distance = 500
                    } else if (this.selectedTags[i] == '1km' && distance <= 1000) {
                        distance = 1000
                    } else if (this.selectedTags[i] == '2km' && distance <= 2000) {
                        // 2km 선택
                        distance = 2000
                    } else {
                        // 카테고리
                        category.push(this.selectedTags[i])
                    }
                }

                let data = {
                    keyword: this.keyword,
                    latitude: this.latitude,
                    longitude: this.longitude,
                    category: category,
                    distance: distance,
                    area: this.area
                }
                console.log(data)
                this.initState()
                this.loadingSpinner()
                await axiosApi.searchStore(
                    data,
                    (res) => {
                        this.loadingSpinner()
                        this.result = res.data.result

                        this.$emit('update:result', this.result)
                        this.useFilter = true
                        console.log(res.data.result)
                    },
                    (err) => {
                        this.loadingSpinner()
                        console.log(err.data)
                    },
                )
            }else{
                alert('검색어 입력은 필수입니다.')
            }
        },

        tagClick(event) {
            //console.log(event)
            let t = event.target.innerText
            //console.log(t)

            let idx = this.selectedTags.indexOf(t)
            if (idx > -1) {
                this.selectedTags.splice(idx, 1)
                console.log(this.selectedTags)
            } else {
                this.selectedTags.push(t)
                console.log(this.selectedTags)
            }

            //this.findData()  //이거 넣어야함. 통신없어서 주석 처리 해놓음
        },

        mouseOver(id) {
            this.$emit('mouseoverid', id)
        },
        mouseOut(id) {
            this.$emit('mouseoverid',-1)
        },

        goToDetail(id) {
            this.$router.push('/store/' + id)
        },
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
    //min-height: 15vh;
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
            //margin-left: 18px;
            margin-top: 8px;
            font-size: 38px;
        }
    }
}

#search-result {
    z-index: 10;
}
</style>