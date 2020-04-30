<template>
    <div>
        <b-modal
            v-model="show"
            title="Select Your 🥄 Or Create 🍴"
            :header-bg-variant="headerBgVariant"
            :header-text-variant="headerTextVariant"
            :body-bg-variant="bodyBgVariant"
            :body-text-variant="bodyTextVariant"
            :footer-bg-variant="footerBgVariant"
            :footer-text-variant="footerTextVariant"
            scrollable
        >
            <div>
                <b-table hover @row-clicked="listClick" :items="items" :fields="fields"></b-table>
            </div>
            <template v-slot:modal-footer>
                <div class="w-100">
                    <b-link @click="createListClick">Create 🍽</b-link>
                    <div v-if="createButtonFlag">
                        <b-input-group class="mt-3">
                            <b-form-input
                                v-model="createListName"
                                placeholder="Input List Name..."
                            ></b-form-input>
                            <b-input-group-append>
                                <b-button @click="createList" variant="outline-success"
                                    >Button</b-button
                                >
                            </b-input-group-append>
                        </b-input-group>
                    </div>
                    <br />
                    <b-button variant="primary" size="sm" class="float-right" @click="cancleClick">
                        Close
                    </b-button>
                </div>
            </template>
        </b-modal>
    </div>
</template>

<script>
import axios from '@/api/axiosScript.js'
export default {
    methods: {
        createList() {
          axios.createFavoriteList(
            {
              id:JSON.parse(sessionStorage.getItem('session')).userid,
              title: this.createListName
            },
            res=>{
              this.items.push(res.data)
            }
          )
        },
        createListClick(e) {
            console.log(e)

            console.log('in create list method')
            this.createButtonFlag = true
        },
        listClick(e) {
            axios.updateFavoriteListStore(
                {
                    user: JSON.parse(sessionStorage.getItem('session')).userid,
                    list_id: e['id'],
                    store: this.$route.params.id,
                },
                (res) => {
                    this.show = false
                    alert('추가 성공 🍕')
                },
            )
        },
        cancleClick() {
            this.$emit('cancle')
            this.show = false
        },
    },
    mounted() {
        axios.getAllFavoriteList(
            {
                id: JSON.parse(sessionStorage.getItem('session')).userid,
            },
            (res) => {
                this.items = res.data
            },
        )
    },
    data() {
        return {
            res: null,
            createButtonFlag: false,
            createListName: '',
            addTargetList: null,
            show: true,
            headerBgVariant: 'success',
            headerTextVariant: 'light',
            bodyBgVariant: 'light',
            bodyTextVariant: 'dark',
            footerBgVariant: 'warning',
            footerTextVariant: 'secondary',
            fields: ['title'],
            items: [],
        }
    },
}
</script>
