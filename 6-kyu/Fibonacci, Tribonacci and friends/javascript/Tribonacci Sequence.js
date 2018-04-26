/* My Soultion */
function tribonacci(signature,n){
    let res = signature.slice(), sum;
    let len = signature.length;
    
    for (let i = 0; i < n - len; i++) {
      sum = 0;
      for (let j = i; j < i + len; j++) {
        sum += res[j];
      }
      res.push(sum)
    }
    return res.slice(0,n);
}

/* Best Pratices & Clever */
const Xbonacci = (sig, n) => {
  let len = sig.length;
  for (let i = len; i < n; i++) 
    sig[i] = sig.slice(i - len).reduce((a, b) => a + b);
  return sig.slice(0, n);
}