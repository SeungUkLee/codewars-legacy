/* My Soultion */
const digPow = (n, p) => {
  let num = n.toString().split('').reduce((sum, x) => {
    return sum + Math.pow(x, p++)
  }, 0)
  return num % n === 0 ? num / n : -1;
}

/* Best Pratices & Clever */
function digPow(n, p) {
  var x = String(n).split("").reduce((s, d, i) => s + Math.pow(d, p + i), 0)
  return x % n ? -1 : x / n
}

/* ********************** */
function digPow(n, p){
  var ans = (''+n).split('')
    .map(function(d,i){return Math.pow(+d,i+p) })
    .reduce(function(s,v){return s+v}) / n
  return ans%1 ? -1 : ans    
}//z.

/* ********************** */
function digPow(n, p){
  var ans = n.toString().split('')
             .map((v,i) => Math.pow(parseInt(v), i+p))
             .reduce((a,b) => a+b) / n;
  return ans%1 == 0 ? ans : -1;
}