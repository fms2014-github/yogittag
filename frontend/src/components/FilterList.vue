<template>
    <div id="filter-list">
        <h2 id="filter-title">
            검색 조건 설정
        </h2>
        <label for="filter-1"
            ><input v-model="selecterFilter" id="filter-1" type="radio" value="filter 1" />filter
            1</label
        >
        <label for="filter-2"
            ><input v-model="selecterFilter" id="filter-2" type="radio" value="filter 2" />filter
            2</label
        >
        <label for="filter-3"
            ><input v-model="selecterFilter" id="filter-3" type="radio" value="filter 3" />filter
            3</label
        >
        <label for="filter-4"
            ><input v-model="selecterFilter" id="filter-4" type="radio" value="filter 4" />filter
            4</label
        >
        <label for="filter-5"
            ><input v-model="selecterFilter" id="filter-5" type="radio" value="filter 5" />filter
            5</label
        >
    </div>
</template>

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

<script>
export default {
    data() {
        return {
            selecterFilter: '',
        }
    },
}
</script>
