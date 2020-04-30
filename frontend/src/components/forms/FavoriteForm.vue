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
                <b-table
                    hover
                    @row-clicked="listClick"
                    :items="items"
                    :fields="fields"
                ></b-table>
            </div>
            <template v-slot:modal-footer>
                <div class="w-100">
                   <b-link href="#" disabled>Create 🍽</b-link>
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
    listClick(e){
      console.log(e['My Favorite List']);
      
    },
    cancleClick() {
      this.$emit('cancle')
      this.show = false
    }
  },
  mounted () {
    axios.getAllFavoriteList(
      {
        id : sessionStorage.getItem("userid")
      },
      res=>{
        this.items = res.data
      }
    )
  },
    data() {
        return {
            res:null,
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
            fields:['title'],
            items: []
        }
    },
}
</script>
