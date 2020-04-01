// import { set, toggle } from "@/utils/vuex";

const state = {
	menuOpenCheck: false,
}

//getters
const getters = {
	menuOpenState: (state) => {
		return state.menuOpenCheck
	},
}

// action
const action = {}

// mutations
const mutations = {
	menuOpenClose(state) {
		if (state.menuOpenCheck) {
			state.menuOpenCheck = !state.menuOpenCheck
			document.getElementById('menu-list').classList.toggle('menu-close')
		} else {
			state.menuOpenCheck = !state.menuOpenCheck
			document.getElementById('menu-list').classList.toggle('menu-close')
		}
	},
}

export default {
	namespaced: true,
	state,
	mutations,
	action,
	getters,
}
