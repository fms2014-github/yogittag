<template>
    <v-btn
        v-show="fab"
        v-scroll="onScroll"
        fab
        dark
        fixed
        bottom
        right
        color="blue --lighten1"
        @click="toTop"
    >
        <v-icon>keyboard_arrow_up</v-icon>
    </v-btn>
</template>

<script>
export default {
    data: () => ({
        fab: false,
    }),

    methods: {
        onScroll(e) {
            if (typeof window === 'undefined') return
            const top = window.pageYOffset || e.target.scrollTop || 0
            this.fab = top > 20
        },
        toTop() {
            this.$vuetify.goTo(0)
        },
    },
}
</script>
