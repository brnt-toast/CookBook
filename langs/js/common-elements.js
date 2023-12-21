let array1 = ['corn', 'hotdog', 'lettuce', 'tomato', 'peanut']
let array2 = ['cucumber', 'blueberry', 'peanut', 'cake', 'hotdog']

let result = []

for (let i = 0; i < array1.length; i++){

	if( array2.indexOf(array1[i]) !== -1) {     // if value of array1 in array2
		let idxPos = array2.indexOf(array1[i])  // the index_position(idxPos) will equal a number not -1
		result.push(array2[idxPos])             // push content to result
	}
}

console.log(result)