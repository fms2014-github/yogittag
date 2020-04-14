<template>
    <v-app-bar id="app-toolbar" app flat color="blue lighten-1">
        <v-btn v-if="!drawer" dark icon @click.stop="onClickDrawer">
            <v-icon>view_list</v-icon>
        </v-btn>
        <v-spacer />
    </v-app-bar>
</template>

<script>
import { mapMutations, mapState } from 'vuex'

export default {
    data: () => ({}),
    computed: {
        ...mapState('app', ['drawer']),
    },
    mounted() {
        window.addEventListener('resize', this.onResponsiveInverted)
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.onResponsiveInverted)
    },

    methods: {
        ...mapMutations('app', ['setDrawer']),
        onClickDrawer() {
            this.setDrawer(!this.drawer)
        },
    },
}
</script>
