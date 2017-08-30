/*
* @Author: Rubén Couoh
* @Date:   2017-08-28 16:53:26
* @Last Modified by:   Rubén Couoh
* @Last Modified time: 2017-08-28 19:43:29
*/

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  prompt: '$ '
});

exports.read = function(cb) {
	
	rl.prompt();

	rl.on('line', (line)=> {
	  rl.close()
	  
	  if (cb) return cb(line.trim());
	});
};