<template>
    <div id="menu-list">
        <b-sidebar id="sidebar-1" title="Sidebar" shadow>
            <div class="px-3 py-2">
                <div>
                    <router-link class="list-button" :to="{ name: 'Home' }">Home</router-link>
                </div>
                <div>
                    <router-link class="list-button" :to="{ name: 'Map' }">Map</router-link>
                </div>
                <div>
                    <router-link class="list-button" to="/store/145030">StoreDetail</router-link>
                </div>
                <div>
                    <router-link class="list-button" :to="{ name: 'Profile' }">Profile</router-link>
                </div>
            </div>
        </b-sidebar>
    </div>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped>
.menu-open {
    position: absolute;
    width: 15vw;
    min-width: 200px;
    top: 0px;
    height: 100%;
    background-color: rgb(250, 250, 250);
    padding: 6px 0 0 30px;
    font-size: 2rem;
    box-shadow: 0px 0px 4px 2px rgba(128, 128, 128, 0.7);
    z-index: 11;
    .list-button {
        padding: 12px 0px;
        cursor: pointer;
    }
    overflow: hidden;
    #close-button {
        width: 100%;
        padding-right: 8px;
        text-align: right;
        .material-icons {
            display: inline;
            cursor: pointer;
            font-size: 48px;
        }
    }
}
.menu-close {
    width: 0;
    min-width: 0;
    padding: 0;
}
</style>
