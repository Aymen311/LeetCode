class Solution {
public: 
    bool isPalindrome(int x) {
          int pop =0;
          int rev = 0;
    if (x < 0 || (x % 10 == 0 && x!=0) ){return false;}
       while (x > rev) {
           pop = x % 10;
           x /= 10;
           rev = rev*10 + pop;
       }
        return rev == x || rev/10 == x;
    }
};
