def is_balance(parent):
    stack = []

    map = {")":"(" , "}":"{" , "]":"["}

    for ch in parent:
        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":

            if stack == []:
                return "Not Balance"
            
            top = stack.pop()
            if top != map[ch]:
                return "Not Balance"


    return "Balance"

        

parent = "({[]})"
print(is_balance(parent))
    


