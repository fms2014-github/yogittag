<template>
    <div style="display: flex; align-item: center; justify-content: center;">
        <vue-tags-input
            v-model="tag"
            :tags="tags"
            placeholder="같이 밥먹을 친구를 추가하세요"
            :autocomplete-items="filteredItems"
            :autocomplete-min-length="0"
            :add-only-from-autocomplete="true"
            @tags-changed="
                (newTags) => {
                    tags = newTags
                    emittags()
                }
            "
        />
        <!-- <v-btn @click="goRecommand">
            <v-icon>search</v-icon>
        </v-btn>-->
    </div>
</template>

<script>
import axiosApi from '@/api/axiosScript.js'
import VueTagsInput from '@johmun/vue-tags-input'
export default {
    name: 'FoodFriendTag',
    components: {
        VueTagsInput,
    },
    data() {
        return {
            tag: '',
            tags: [],
            autocompleteItems: [],
        }
    },
    computed: {
        filteredItems() {
            return this.autocompleteItems.filter((i) => {
                return i.text.toLowerCase().indexOf(this.tag.toLowerCase()) !== -1
            })
        },
    },
    mounted() {
        axiosApi.getAllFollowers(
            68632,
            (res) => {
                console.log(res)

                this.autocompleteItems = []
                res.data.followers.forEach((element) => {
                    this.autocompleteItems.push({ text: element.nick_name, key: element.id })
                })
            },
            (err) => {
                console.log(err)
            },
        )
    },
    methods: {
        emittags() {
            console.log('first emit')
            this.$emit('emittags', this.tags)
        },
    },
}
</script>

<style></style>
