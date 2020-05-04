<template>
    <div id="filter-list">
        <h4 id="filter-title">필터</h4>
        <label for="filter-1">
            <input v-model="bob" id="filter-1" type="checkbox" value="filter 1" />
            <img src="@/assets/icons/bob.svg" style="width: 1.5em;" />
        </label>
        <label for="filter-2">
            <input v-model="cafe" id="filter-2" type="checkbox" value="filter 2" />
            <img src="@/assets/icons/cafe.svg" style="width: 1.5em;" />
        </label>
        <label for="filter-3">
            <input v-model="sul" id="filter-3" type="checkbox" value="filter 3" />
            <img src="@/assets/icons/soju.svg" style="width: 1.5em;" />
        </label>
    </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
    data() {
        return {
            filter: 'filter 1',
            bob: '',
            cafe: '',
            sul: '',
        }
    },
    watch: {
        filter: function (v) {
            console.log(v)
            this.setSelecterFilter(v)
        },
    },
    methods: {
        ...mapMutations('app', ['setSelecterFilter']),
    },
}
</script>

<style lang="scss" scoped>
#filter-list {
    margin: 18px 0;
    #filter-title {
        text-align: center;
    }
    input {
        font-size: 1.5rem;
    }
    label {
        margin: 8px 16px;
        font-size: 1.5rem;
    }
}
</style>
