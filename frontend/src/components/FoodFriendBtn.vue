<template>
    <div>
        <v-btn class="ma-2 group_add_btn" icon @click="$emit('toggle')"
            ><v-icon large>group_add</v-icon></v-btn
        >
    </div>
</template>
<script>
export default {
    name: 'FoodFriendBtn',
    components: {},
    props: {
        isHidden: Boolean,
    },
    data() {
        return {}
    },
    methods: {},
}
</script>

<style>
.group_add_btn:focus {
    outline: none;
}
</style>
