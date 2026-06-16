int getSum(int a, int b) {
   int mask = 0xffffffff;
   int max_int = 0x7fffffff;
    while (b){
        unsigned carry = ((unsigned)(a & b)) << 1;
        a = (a ^ b);
        b = carry;

    }
    return (a <= max_int) ? a : ~(a ^ mask);
}