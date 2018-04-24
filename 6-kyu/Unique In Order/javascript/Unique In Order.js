/* My Soultion */
var uniqueInOrder=function(iterable){
    var res = [];
    var len = iterable.length;
    
    for (let i = 0; i < len - 1; i++) {
      if (iterable[i] !== iterable[i + 1]) {
        res.push(iterable[i]);
      }
    }
    if (iterable) {
      res.push(iterable[len-1]);
    }
    
    return res;
}

/* Best Pratices */
function uniqueInOrder(it) {
    var result = []
    var last
    
    for (var i = 0; i < it.length; i++) {
      if (it[i] !== last) {
        result.push(last = it[i])
      }
    }
    
    return result
}

/* Clever */
var uniqueInOrder = function (iterable) {
  return [].filter.call(iterable, (function (a, i) { return iterable[i - 1] !== a }));
}

/* Another Soultions */
var uniqueInOrder=function(iterable){
    return [...iterable].filter((a, i) => a !== iterable[i-1])
}

/* ---------- */
const reducer = (acc, x) =>
  acc[acc.length - 1] === x
    ? acc
    : [...acc, x]

const uniqueInOrder = x => [].reduce.call(x, reducer, [])

/* ---------- */
const uniqueInOrder = d => [...d].filter((x, i, a) => x != a[i + 1])

/* ---------- */
var uniqueInOrder=function(iterable){
    var result = [];
    for (var i = 0; i < iterable.length; i++) {
      if (iterable[i-1] === undefined || iterable[i-1] !== iterable[i]) {
        result.push(iterable[i]);
      }
    }
    return result;
}

/* ---------- */
var uniqueInOrder=function(iterable){
    var res = [];
    for (var i = 0; i < iterable.length; i++) {
      if (iterable[i] != iterable[i+1]) res.push(iterable[i]);
    }
    return res;
}

/* ---------- */
var uniqueInOrder=function(iterable){
    //your code here - remember iterable can be a string or an array
    var previous
    var newArray = []
    
    for (var v of iterable) {
      if(previous !== v) newArray.push(previous = v)
    }
    
    return newArray
}