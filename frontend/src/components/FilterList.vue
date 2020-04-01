/* eslint-disable prettier/prettier */ /* eslint-disable prettier/prettier */
<template>
	<div id="filter-list">
		<div id="filter">
			<h2 id="filter-title">
				검색 조건 설정
			</h2>
			<label for="seleter-filter"><input id="selete-filter" type="radio" />filter 1</label>
			<label for="seleter-filter"><input id="selete-filter" type="radio" />filter 2</label>
			<label for="seleter-filter"><input id="selete-filter" type="radio" />filter 3</label>
			<label for="seleter-filter"><input id="selete-filter" type="radio" />filter 4</label>
			<label for="seleter-filter"><input id="selete-filter" type="radio" />filter 5</label>
		</div>
	</div>
</template>

<style lang="scss" scoped>
#filter-list {
	position: absolute;
	top: 0px;
	left: 0px;
	width: 100vw;
	height: 100vh;
	background-color: rgba(255, 255, 255, 0.3);
	z-index: 12;
	#filter {
		position: absolute;
		top: 50vh;
		left: 50vw;
		background-color: white;
		transform: translate(-50%, -50%);
		width: 40%;
		max-width: 700px;
		height: 200px;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 0 0 4px 2px rgba(128, 128, 128, 0.7);
		#filter-title {
			text-align: center;
		}
		// eslint-disable-next-line prettier/prettier
		label[for='selete-filter'] {
			display: block;
		}
	}
}
</style>
