<template>
    <div id="app-view">
        <router-view :key="$route.fullPath"/>
    </div>
</template>

<style lang="scss" scoped>
#app-view {
    width: 100vw;
    height: 100%;
}
</style>

<script>
export default {}
</script>
