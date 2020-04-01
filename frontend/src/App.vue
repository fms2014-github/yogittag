<template>
	<div id="app">
		<menu-button />
		<profile-button />
		<menu-list @closeCheckChange="menuOpenClose" />
		<main-view />
	</div>
</template>

<script>
import mainView from './components/View.vue'
import menuButton from './components/MenuButton.vue'
import profileButton from './components/ProfileButton.vue'
import MenuList from './components/MenuList.vue'
import { mapState, mapMutations, mapGetters } from 'vuex'

export default {
	components: {
		mainView,
		menuButton,
		MenuList,
		profileButton,
	},
	computed: {
		...mapState('app', ['menuOpenCheck']),
		...mapGetters('app', ['menuOpenState']),
	},
	methods: {
		...mapMutations('app', ['menuOpenClose']),
	},
}
</script>
