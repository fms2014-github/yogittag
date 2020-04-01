<template>
	<div id="search">
		<div id="search-bar">
			<input id="search-bar-input" placeholder="음식점 이름을 입력하세요" type="text" />
			<button id="search-button">
				<span class="material-icons">
					search
				</span>
			</button>
			<br />
			<button id="filter-button">
				<span class="material-icons">
					filter_list
				</span>
			</button>
		</div>
	</div>
</template>

<style lang="scss" scoped>
#search {
	position: absolute;
	left: 50vw;
	top: 36px;
	transform: translateX(-50%);
	background-color: white;
	width: 50vw;
	max-width: 700px;
	z-index: 10;
	#search-bar {
		display: flex;
		justify-content: center;
		align-items: flex-start;
		padding: 0 1vw;
		width: 100%;
		height: 74px;
		border-radius: 7px;
		box-shadow: 0px 0px 4px 2px rgba(128, 128, 128, 0.7);
		#search-bar-input {
			width: 100%;
			margin-top: 10px;
			height: 48px;
			font-size: 18pt;
		}
		.material-icons {
			margin-left: 8px;
			margin-top: 10px;
			font-size: 48px;
		}
	}
}
</style>
