/*
* @Author: Rubén Couoh
* @Date:   2017-08-28 19:25:03
* @Last Modified by:   Rubén Couoh
* @Last Modified time: 2017-08-29 21:36:04
*/

var readline = require('./readline');

readline.read((input) => {
  const [i, j] = input.split(' ').map((item)=>Number.parseInt(item,10));

  let maximunCycle = 1;
  const memory = {'1':1, '2':2};

  const cycle = (n, memory) => {

    if (!memory[n]) {

      const k = n%2===0 ? n>>>1 : n*3+1; // +1 paso
      const steps = k%2 === 0 ? 2 : 3; // +1 Si es par, +2 Si es impar
      const k1 = steps == 2 ? k>>>1 : (k*3+1)>>>1;

      memory[n] = steps + cycle(k1, memory);
    }
    
    return memory[n];
  }

  console.time('elapse');

  for (let n=i; n<=j; n++) {
    let newCycle = cycle(n, memory);
    if(newCycle > maximunCycle) {
      maximunCycle = newCycle;
    }
  }

  console.timeEnd('elapse')
  console.log(`${i} ${j} ${maximunCycle}`);
});