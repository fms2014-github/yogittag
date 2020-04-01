<template>
	<div class="vld-parent">
		<loading
			:active.sync="isLoading"
			:can-cancel="true"
			:on-cancel="onCancel"
			:is-full-page="fullPage"
		/>

		<label><input v-model="fullPage" type="checkbox" />Full page?</label>

		<button @click.prevent="doAjax">fetch Data</button>
	</div>
</template>

<script>
// Import component

import Loading from 'vue-loading-overlay'

// Import stylesheet

import 'vue-loading-overlay/dist/vue-loading.css'

export default {
	components: {
		Loading,
	},

	data() {
		return {
			isLoading: false,

			fullPage: true,
		}
	},

	methods: {
		doAjax() {
			this.isLoading = true

			// simulate AJAX

			window.console.log('123123123')

			setTimeout(() => {
				this.isLoading = false
			}, 5000)
		},

		onCancel() {
			window.console.log('User cancelled the loader.')
		},
	},
}
</script>
