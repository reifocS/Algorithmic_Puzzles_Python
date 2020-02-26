#https://www.codingame.com/training/easy/brackets-extreme-edition

parenthese = {'{':'}', 
              '(':')',
              '[':']'}
              
def correct_brackets(expression):
    #cleaning
    n = [k for k in expression if k in parenthese.values() or k in parenthese]
    queue = []
    for p in n:
        if p in parenthese:
            queue.append(p)
        else:
            if not queue or parenthese[queue[-1]] != p:
                return False
            queue.pop()
    return not queue


print({True: "true", False: "false"} [correct_brackets(input())]) 
