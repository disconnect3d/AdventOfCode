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

r.on('close', _ => {
	left.sort( (x, y) => x-y );
	right.sort( (x, y) => x-y );

	let sum = 0;
	for(let i=0; i<left.length; i++) {
		sum += Math.abs(left[i] - right[i]);
	}

	//console.log(left);
	//console.log(right);
	console.log(sum);
});

// O(n) = 2n + n*log(n) = n* (2+log(n)) ~~ n*log(n)
