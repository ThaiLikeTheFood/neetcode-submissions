class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        for p in s:         
            if p == '(' or p == '{' or p == '[':
                opened.append(p)
                continue
            if opened == []:
                return False
            else:
                top = opened[-1]
            

            print('current top is: ',top)
            print('we\'re looking at', p)
            if top == '(' and p == ')':
                print('popped ()!')
                opened.pop()
            elif top == '[' and p == ']':
                print('popped []!')
                opened.pop()
            elif top == '{' and p == '}':
                print('popped {}!')
                opened.pop()
            else:
                opened.append(p)

            print(p)
            print(opened)
            

        if opened == []:
            return True
        else:
            return False