<template>
    <div class="col-lg-3 col-md-4 col-sm-6 col-12">
        <div class="card h-100">
            <router-link :to="routing">
                <img class="card-img-top" :src="img" alt />
            </router-link>
            <div class="card-body">
                <h4 class="card-title">
                    <router-link :to="routing">
                        {{ title }}
                        {{ gender != null ? '(' + gender + ')' : '' }}
                    </router-link>
                </h4>
                <p class="card-text" v-if="content">{{ content }}</p>
                <p style="float: right;" v-if="reg_time">{{ reg_time | dateFilter }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import dateFilter from '@/components/filters/dateFilter.js'

export default {
    /*
        routing : "string",
        img : "string",
        gender : "string",
        title : "string",
        reg_time : "string",
        content : "string",
        score : number
    */
    props: {
        routing: {
            type: String,
            default: '#',
        },
        img: {
            type: String,
             default: require('../../assets/img/review_default_img.png'),
        },
        gender: {
            type: String,
            default: null,
        },
        title: {
            type: String,
        },
        reg_time: {
            type: String,
            default: null,
        },
        content: {
            type: String,
        },
        score: {
            type: Number,
        },
    },
    data() {
        return {
        }
    },
    filters: {
        dateFilter: dateFilter,
    },
}
</script>

<style></style>
