var arr = [
	1,2,3,4,5, 			6,7,8,9,10,
	11,12,13,14,15, 16,17,18,19,20,
	21,22,23,24,25, 26,27,28,29,30,
	31,32,33,34,35, 36,37,38,39,40,
	41,42,43,44,45
]

let temp=0;
for(let i=0;i<1000;i++){
	let rnd=parseInt(Math.random()*45);
	temp=arr[0];
	arr[0]=arr[rnd];
	arr[rnd]=temp;
}
for(let i=0; i<6;i++){
	console.log(arr[i]);
}