<template>
    <div style="display: flex; align-item: center; justify-content: center;">
        <vue-tags-input
            v-model="tag"
            :tags="tags"
            placeholder="같이 밥먹을 친구를 추가하세요"
            :autocomplete-items="filteredItems"
            :add-only-from-autocomplete="true"
            @tags-changed="(newTags) => (tags = newTags)"
        />
        <v-btn @click="goRecommand">
            <v-icon>search</v-icon>
        </v-btn>
    </div>
</template>

<script>
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
            autocompleteItems: [
                {
                    text: 'Spain',
                    key: 123,
                },
                {
                    text: 'France',
                    key: 234,
                },
                {
                    text: 'USA',
                    key: 345,
                },
                {
                    text: 'Germany',
                    key: 456,
                },
                {
                    text: 'China',
                    key: 567,
                },
                {
                    text: '가나다라',
                    key: 123,
                },
            ],
        }
    },
    computed: {
        filteredItems() {
            return this.autocompleteItems.filter((i) => {
                return i.text.toLowerCase().indexOf(this.tag.toLowerCase()) !== -1
            })
        },
    },
    methods: {
        goRecommand() {
            console.log('goRecommand')
        },
    },
}
</script>

<style></style>
