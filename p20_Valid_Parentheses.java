import java.util.Stack;

public class Solution {
    public boolean isValid(String s){
        char[] sArray = s.toCharArray();
        Stack<Character> parenthesesStack = new Stack<Character>();
        for (char c : sArray){
            if (c == '[') parenthesesStack.push(']');
            else if (c == '(') parenthesesStack.push(')');
            else if (c == '{') parenthesesStack.push('}');
            else if (parenthesesStack.isEmpty() || parenthesesStack.pop() != c) return false;
        }
        return parenthesesStack.isEmpty();
    }
}