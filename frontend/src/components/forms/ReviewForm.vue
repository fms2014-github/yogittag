<template>
    <div>
        <b-modal
            :no-close-on-backdrop="true"
            @ok="modalCilck()"
            id="modal"
            size="lg"
            title="Review"
            v-model="modal"
        >
            <div>
                <b-form @submit.stop.prevent>
                    <div>
                        <h5>Rating</h5>
                        <star-rating
                            v-model="rating"
                            :glow="6"
                            :increment="0.5"
                            :border-width="1"
                            border-color="#d8d8d8"
                            :rounded-corners="true"
                            :star-points="[
                                23,
                                2,
                                14,
                                17,
                                0,
                                19,
                                10,
                                34,
                                7,
                                50,
                                23,
                                43,
                                38,
                                50,
                                36,
                                34,
                                46,
                                19,
                                31,
                                17,
                            ]"
                        ></star-rating>
                    </div>
                    <br />
                    <div>
                        <h5>Content</h5>
                        <b-form-textarea
                            id="textarea-state"
                            v-model="content"
                            placeholder="Enter at least 10 characters"
                            rows="3"
                            max-rows="6"
                            :state="validation"
                        ></b-form-textarea>
                        <b-form-valid-feedback :state="validation">
                            Looks Good.
                        </b-form-valid-feedback>
                    </div>
                    <br />
                    <div>
                        <h5>Picture</h5>
                        <b-img
                            v-if="imageData.length > 0"
                            center
                            thumbnail
                            fluid
                            :src="imageData"
                            alt="preview image file"
                        ></b-img>
                        <b-form-file
                            id="preview"
                            v-model="file"
                            @change="previewImage"
                            accept="image/*"
                            placeholder="Choose a file or drop it here..."
                            drop-placeholder="Drop file here..."
                        ></b-form-file>
                    </div>
                    <br />
                </b-form>
            </div>
        </b-modal>
    </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import axios from '@/api/axiosScript.js'

export default {
    props:['storeName'],
    components: {
        StarRating,
    },
    data() {
        return {
            modal: null,
            file: null,
            content: '',
            rating: 0,
            img: null,
            imageData: '', // we will store base64 format of image in this string
            imageLink: null
        }
    },
    computed: {
        validation() {
            return this.content.length > 4
        },
    },
    methods: {

        modalCilck(e) {
            axios.createReview(
                {
                    store: this.$route.params.id,
                    user: JSON.parse(sessionStorage.getItem("session")).userid,
                    score: this.rating,
                    content: this.content,
                    img: this.file == null ? null : this.imageLink,
                },
                (res) => {
                    alert(`${this.storeName} 음식점에 리뷰를 등록하였습니다.\n감사합니다~`)
                    let local = localStorage
                    local.setItem("card_title",`익명 ${res.data.user}`)
                    local.setItem("card_routing",`/profile/${res.data.user}/review`)
                    local.setItem("card_score",res.data.score)
                    local.setItem("card_content",res.data.content)
                    local.setItem("card_reg_time",res.data.reg_time)
                    local.setItem("card_img",res.data.img)
                    this.$emit('registerReview')
                },
                (err) => {
                    alert(`리뷰 등록 실패하였습니다.`)
                },
            )
        },
        async previewImage(event) {
            // Reference to the DOM input element
            var input = event.target
            this.imageLink = await axios.imageUpload(event.target.files[0])
            // Ensure that you have a file before attempting to read it
            if (input.files && input.files[0]) {
                // create a new FileReader to read this image and convert to base64 format
                var reader = new FileReader()
                // Define a callback function to run, when FileReader finishes its job
                reader.onload = (e) => {
                    // Note: arrow function used here, so that "this.imageData" refers to the imageData of Vue component
                    // Read image as base64 and set to imageData
                    this.imageData = e.target.result
                }
                // Start the reader job - read file as a data url (base64 format)
                reader.readAsDataURL(input.files[0])
            }
        },
    },
}
</script>
<style scoped>
#preview {
    width: 700px;
    height: 400px;
}
</style>
