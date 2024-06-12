export const addToCart = async (idProd) => {
	
	const URL_ENDPOINT = `http://127.0.0.1:8000/store/add/${idProd}`
	
	const response = await fetch(URL_ENDPOINT, {
		method: 'POST',
		headers: {
			'Accept': 'application/json',
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({id_producto: idProd})
	});
	
	const content = await response.text()
	console.log(content)

}

