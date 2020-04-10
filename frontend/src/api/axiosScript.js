import axios from 'axios'

const searchAxios = async (data, success, error) => {
	await axios({
		url: 'http://192.168.0.46:8080/apiTest/3sec-return',
		method: 'post',
	})
		.then((res) => {
			success(res)
		})
		.catch((err) => {
			error(err)
		})
}

const axiosFunction = {
	searchAxios: (data, success, error) => searchAxios(data, success, error),
}

export default axiosFunction
