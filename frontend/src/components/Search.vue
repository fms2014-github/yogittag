<template>
    <div id="search">
        <div id="search-bar" class="search-bar">
            <input
                id="search-bar-input"
                @keyup.enter="findData"
                placeholder="음식점 이름을 입력하세요"
                type="text"
            />
            <button id="search-button" @click="findData">
                <span class="material-icons">
                    search
                </span>
            </button>
            <button id="filter-button">
                <span class="material-icons" @click="openFilter">
                    filter_list
                </span>
                <span id="is-filter" v-show="useFilter">필터 사용</span>
            </button>
            <hr />
            <filter-list />
        </div>
    </div>
</template>

<script>
import filterList from '../components/FilterList.vue'
import axiosApi from '../api/axiosScript.js'
import { mapMutations, mapState, mapGetters } from 'vuex'
export default {
    components: {
        filterList,
    },
    computed: {
        ...mapGetters('app', ['useFilter']),
    },
    methods: {
        ...mapMutations('app', ['loadingSpinner', 'initState']),
        openFilter() {
            document.getElementById('search-bar').classList.toggle('open-filter')
        },
        findData() {
            this.initState()
            this.loadingSpinner()
            axiosApi.searchAxios(
                '',
                (res) => {
                    this.loadingSpinner()
                    console.log(res.data)
                },
                (err) => {
                    this.loadingSpinner()
                    console.log(err.data)
                },
            )
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
    max-width: 700px;
    z-index: 10;
    .search-bar {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        flex-wrap: wrap;
        padding: 0 1vw;
        width: 100%;
        height: 68px;
        border-radius: 7px;
        overflow: hidden;
        box-shadow: 0px 0px 4px 2px rgba(128, 128, 128, 0.7);
        #search-bar-input {
            width: calc(100% - 112px);
            margin-top: 10px;
            height: 48px;
            font-size: 18pt;
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
            margin-left: 8px;
            margin-top: 10px;
            font-size: 48px;
        }
    }
    .open-filter {
        height: auto;
    }
}
</style>
