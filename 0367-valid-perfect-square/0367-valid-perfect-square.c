bool isPerfectSquare(int num) {
    if (num == 1) {
        return true;
    }
    for (int i = 2; i < num; i++) {
        if (num / i < i) {
            return false;
        }
        if ((num % i == 0) && (num / i == i)) {
            return true;
        }
    }
    return false;
}