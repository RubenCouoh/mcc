/*
* @Author: Rubén Couoh
* @Date:   2017-08-31 09:02:41
* @Last Modified by:   Rubén Couoh
* @Last Modified time: 2017-08-31 09:20:56
*/

const readline = require('./readline');

readline.read((input) => {
  const [n, ...list] = input.split(/\s+/).map((item)=>Number.parseInt(item,10));
  
  let set = new Set();

  for (let i=1; i<n; i++) {
  	const diff = Math.abs(list[i-1] -list[i]);

  	if (diff < n && !set.has(diff)) {
  		set.add(diff);
  	} else {
  		break;
  	}
  }

  if(set.size === n-1) {
  	console.log('Jolly');
  } else {
  	console.log('No Jolly');

  }
});