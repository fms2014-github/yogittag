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
            userid : -1
        }
    },
    computed: {
        filteredItems() {
            return this.autocompleteItems.filter((i) => {
                return i.text.toLowerCase().indexOf(this.tag.toLowerCase()) !== -1
            })
        },
    },
    async mounted() {
        //let userid = JSON.parse(sessionStorage.getItem('session')).userid

        if(sessionStorage.getItem('session') != null){
            this.userid = JSON.parse(sessionStorage.getItem('session')).userid

            if(this.userid != 0){
                let followDataObj = (await axiosApi.getAllFollowers(this.userid)).data.followers

               followDataObj.forEach((element) => {
                        if(element.nick_name == null){
                            this.autocompleteItems.push({ text: '익명 '+element.id, key: element.id })
                        }
                        else{
                            this.autocompleteItems.push({ text: element.nick_name, key: element.id })
                        }
                        // this.autocompleteItems.push({ text: element.nick_name, key: element.id })
                        //this.autocompleteItems.push({ text: '익명 '+element.id, key: element.id })
                    })
                }
        }
        else{
            console.log('no')
        }
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
