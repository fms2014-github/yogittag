<template>
    <div id="menu-list" class="menu-open menu-close">
        <div id="close-button">
            <span class="material-icons" @click="closeMenu">
                arrow_back
            </span>
        </div>
        <div class="list-button">Menu 1</div>
        <div class="list-button">Menu 2</div>
        <div class="list-button">Menu 3</div>
        <div class="list-button">Menu 4</div>
        <div class="list-button">Menu 5</div>
    </div>
</template>

<script>
export default {
    methods: {
        closeMenu() {
            this.$emit('closeCheckChange')
        },
    },
}
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
