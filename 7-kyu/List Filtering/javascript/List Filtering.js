/* My Solution */
function filter_list(l) {
    var res = []
    
    for (const value of l) {
      if (typeof value === 'number') {
        res.push(value)
      }
    }
    
    return res
}


/* Best Paratice & Clever */
function filter_list(l) {
    return l.filter(v => typeof v == "number")
}