const readline = require('readline');

var r = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
});

const left = [];
const right = [];

r.on('line', line => {
	let [a, b] = line.split('   ').map(x => Number(x));

	left.push(a);
	right.push(b);
});

//const counter: { [key: Number]: Number } = {};

r.on('close', _ => {
	let sum = 0;

	for(let i=0; i<left.length; i++) {
		const left_item = left[i];

		let occurrences = 0;
		for(let j=0; j<right.length; j++) {
			if ( right[j] == left_item ) {
				occurrences += 1;
			}
		}

		sum += left_item * occurrences;
	}
	console.log(sum);
});
