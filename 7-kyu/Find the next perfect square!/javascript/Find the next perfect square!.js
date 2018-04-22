function findNextSquare(sq) {
    return Math.sqrt(sq)%1 === 0 ? Math.pow(Math.sqrt(sq)+1, 2) : -1;
}