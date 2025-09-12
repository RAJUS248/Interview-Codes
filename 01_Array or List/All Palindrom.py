def palindrom(string):

    palindm = string[::-1]

    if string == palindm:
        print(True)

    else:
        print(False)

def palindrom_v2(string):
    text = "".join(reversed(string))
    print(text)

def palindrome_v3(string):

   for letr in range (len(string)-1,-1,-1):
       print(string[letr], end ="")

def v3(string):
    i,j = 0, len(string)-1

    while i < j:
        if string[i] != string[j]:
            return False
        
        i += 1
        j -= 1

    return True


if __name__ == "__main__":
    string = "gadaag"
    palindrom(string)
    palindrom_v2(string)
    palindrome_v3(string)
    print("\n",v3(string))

