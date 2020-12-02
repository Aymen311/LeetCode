class Solution {
public:
    bool isValid(string s) {
        stack<char> pile;

        if ( s.length()==1) return false;
        if (s.length()==0) return true;

        for(int i = 0 ; i< s.length(); i++){
            char c = s[i];
            if (c == ')' || c == '}' || c == ']'){
                if (pile.size() == 0) return false;
                if(c== ')' && pile.top() != '(' ) return false;
                if(c== '}' && pile.top() != '{' ) return false;
                if(c== ']' && pile.top() != '[' ) return false;
                pile.pop();
            }
            else{pile.push(c);}
        }

        if (pile.size() == 0){ return true;}
        return false ;
    }
};
