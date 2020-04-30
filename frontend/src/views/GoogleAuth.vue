<template>
    <div id="profile-edit">
        <profile-edit :isFullSize="true" />
    </div>
</template>

<script>
import profileEdit from './profileEditPage.vue'
export default {
    components: {
        profileEdit,
    },
}
</script>

<style lang="scss" scoped>
#profile-edit {
    position: absolute;
    top: 0px;
    width: 100vw;
    height: 100vh;
    background-color: rgba(128, 128, 128);
}
</style>
