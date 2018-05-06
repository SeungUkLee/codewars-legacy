/* My Soultion */
const divisors = (integer) => {
  let divisors = [];
  for (let i = 2; i < integer; i++) {
    if (integer % i == 0) {
      divisors.push(i);
    }
  }
  return divisors.length ? divisors : `${integer} is prime`;
};


/* Best Pratices & Clever */
function divisors(integer) {
  var res = []
  for (var i = 2; i <= Math.floor(integer / 2); ++i) if (integer % i == 0) res.push(i);
  return res.length ? res : integer + ' is prime'
};
