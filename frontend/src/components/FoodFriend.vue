<template>
    <div class="foodFriend">
        <food-friend-btn @toggle="toggle" />
        <v-expand-transition>
            <food-friend-tag v-show="isHidden" />
        </v-expand-transition>
    </div>
</template>

<script>
import FoodFriendBtn from '../components/FoodFriendBtn'
import FoodFriendTag from '../components/FoodFriendTag'
export default {
    name: 'FoodFriend',
    components: {
        FoodFriendBtn,
        FoodFriendTag,
    },
    data() {
        return {
            isHidden: false,
            test: false,
        }
    },
    methods: {
        toggle() {
            this.isHidden = !this.isHidden
        },
    },
}
</script>

<style>
</style>
