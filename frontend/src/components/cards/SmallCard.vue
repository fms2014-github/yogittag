<template>
    <div class="col-lg-4 col-md-6 mb-4">
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
                <p class="card-text">{{ content }}</p>
                <p style="float: right;">{{ reg_time | dateFilter }}</p>
            </div>
            <div class="card-footer">
                <small v-for="item in score" :key="item.id">&#9733;</small>
                <small v-for="item in remainScore" :key="item.id">&#9734;</small>
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
            default: 'http://placehold.it/700x400',
        },
        gender: {
            type: String,
            default: null,
        },
        title: {
            type: String,
            default: 'Reivew Title',
        },
        reg_time: {
            type: String,
            default: null,
        },
        content: {
            type: String,
            default:
                'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Amet numquam aspernatur!',
        },
        score: {
            type: Number,
            default: 0,
        },
    },
    data() {
        return {
            maxScore: 5,
            remainScore: 0,
        }
    },
    filters: {
        dateFilter: dateFilter,
    },
    methods: {
        calRemainScore(score) {
            return this.maxScore - score
        },
    },
    created() {
        this.remainScore = this.calRemainScore(this.score)
    },
}
</script>

<style></style>
