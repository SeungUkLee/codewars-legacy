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
function tribonacci(signature,n){  
    for (var i = 0; i < n-3; i++) { // iterate n times
      signature.push(signature[i] + signature[i+1] + signature[i+2]); // add last 3 array items and push to trib
    }
    return signature.slice(0, n); //return trib - length of n
}

/* Another Soultions */
function tribonacci(signature,n) {
    const result = signature.slice(0, n);
    while (result.length < n) {
      result[result.length] = result.slice(-3).reduce((p,c) => p + c, 0);
    }
    return result;
}

/* ----------- */
function tribonacci(signature,n){
    while (signature.length < n) {
      signature.push(signature.slice(-3).reduce((a, b) => a + b));
    }
    return signature.slice(0, n);
}