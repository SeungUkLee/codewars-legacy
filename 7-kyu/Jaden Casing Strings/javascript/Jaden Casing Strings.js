/* My Soultion */
String.prototype.toJadenCase = function () {
    return this.toLowerCase().split(' ').map((word) => {
      return word.charAt(0).toUpperCase() + word.substr( 1 );
    }).join(' ')
};

/* Best Practices */
String.prototype.toJadenCase = function () { 
    return this.split(" ").map(function(word){
      return word.charAt(0).toUpperCase() + word.slice(1);
    }).join(" ");
}

/* Clever */
String.prototype.toJadenCase = function () {
    return this.replace(/(^|\s)[a-z]/g, function(x){ return x.toUpperCase(); });
};