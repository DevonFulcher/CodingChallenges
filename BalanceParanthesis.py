'''
You are given a string with alphanumeric characters and parentheses. Your goal is to return a string with balanced parentheses by removing the fewest characters possible. Note that you cannot add anything to the string.
 
Examples
 
"()"  -> "()"
"b(a)r)"  -> "b(a)r"
")("  -> ""
"((((("  -> ""
")(())("  -> "(())"
  
Note that there can be multiple correct results per input. You just have to return one of the correct results.
 
"(()()("  -> "()()" OR "(())"
"(())())"  -> "(()())" OR "(())()"
-------------------------------------------------------------

start: 9:01
test cases:

()(((())()
)))))))))())

nope - count left parantheses, if count of right parantheses is greater than left parantheses,
delete right paranthesis, at end delete number of left paranthesis equal to difference of left count and right count

O(n) space solution with queue

alternate solution, traverse in forward order then backward order O(1) space

optimization: use mutable data structure like list

code: 9:12
'''

def balance_parantheses(aString):
    left_parantheses_count = 0
    right_parantheses_count = 0
    for i, char in enumerate(aString):
        if char == "(":
            left_parantheses_count += 1
        if char == ")":
            right_parantheses_count += 1
        if right_parantheses_count > left_parantheses_count:
            aString = aString[:i] + aString[i+1:]
            right_parantheses_count -= 1
    
    left_parantheses_count = 0
    right_parantheses_count = 0
    aString = aString[::-1]
    for i, char in enumerate(aString):
        if char == "(":
            left_parantheses_count += 1
        if char == ")":
            right_parantheses_count += 1
        if right_parantheses_count < left_parantheses_count:
            aString = aString[:i] + aString[i+1:]
            left_parantheses_count -= 1
    return aString[::-1]


'''
"((())"
"()))" ->
")(()())(" -> "(()())(" -> "((()())" -> "(()())"

L=1
R=2

'''