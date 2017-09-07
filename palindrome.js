/*
* @Author: Rubén Couoh
* @Date:   2017-09-04 09:43:57
* @Last Modified by:   Rubén Couoh
* @Last Modified time: 2017-09-06 20:03:22
*/

const readline = require('./readline');

let palindrome = (string, begin=0, end=string.length-1) => {
	if (begin >= end) {
		return true;
	} else {
		return  string[begin] === string[end] && palindrome(string, begin+1, end-1);
	}
}

readline.read((line) => {
	let isPalindrome = palindrome(line.toLowerCase());
	console.log(`${line} ${isPalindrome ? 'es palindromo':'no es palindromo'}`);
});
