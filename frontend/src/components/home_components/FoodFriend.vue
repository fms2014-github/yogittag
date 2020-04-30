<template>
    <div class="foodFriend">
        <food-friend-btn @toggle="toggle" />
        <v-expand-transition>
            <food-friend-tag @emittags="emittags" v-show="isHidden" />
        </v-expand-transition>
    </div>
</template>

<script>
import FoodFriendBtn from '../../components/FoodFriendBtn'
import FoodFriendTag from '../../components/FoodFriendTag'
export default {
    name: 'FoodFriend',
    components: {
        FoodFriendBtn,
        FoodFriendTag,
    },
    data() {
        return {
            isHidden: false,
            test: false
        }
    },
    methods: {
        toggle() {
            this.isHidden = !this.isHidden
        },
        emittags(tags){
            console.log('second emit')
            console.log(tags)

            this.$emit("update:tags", tags)
        }
    },
}
</script>

<style>
</style>
