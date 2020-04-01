<template>
	<div id="menu">
		<button class="menu-button" @click="menuOpenClose">
			<span class="material-icons">
				menu
			</span>
		</button>
	</div>
</template>

<style lang="scss" scoped>
#menu {
	position: absolute;
	display: inline-flex;
	justify-content: center;
	align-items: center;
	width: 48px;
	height: 48px;
	top: 18px;
	left: 18px;
	z-index: 10;
	border-radius: 48px;
	background-color: white;
	box-shadow: 0px 0px 4px 2px rgba(128, 128, 128, 0.7);
	.menu-button .material-icons {
		vertical-align: bottom;
		font-size: 32px;
		z-index: 1;
	}
}
</style>

<script>
import { mapMutations } from 'vuex'
export default {
	methods: {
		...mapMutations('app', ['menuOpenClose']),
	},
}
</script>
