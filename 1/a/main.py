import time

print("Amos Lastmann")
print("City of London School\n\n")



s1, s2 = input().split(" ")
start = time.time()
# Recursion

def reverse(string):
    return string[::-1]

def test(string, i):
    if len(string) > 2:     
        test1 = string[:i]
        test2 = string[i:]
        
        test1s = min(ord(i) for i in test1)
        test2s = max(ord(i) for i in test2)
        if test1s <= test2s:
            return False
        
        else:
            return testall(reverse(test1)) and testall(reverse(test2))
        
    else:
        if len(string) == 1:
            return True

        if ord(string[0]) > ord(string[1]):
            return True
        
        else:
            return False

def testall(string):
    if len(string) == 1:
        return True

    return any(test(string, i) for i in range(1, len(string)))

print("YES" if testall(s1) else "NO")
print("YES" if testall(s2) else "NO")
print("YES" if testall(s1 + s2) else "NO")

print(f"\nTime taken: {time.time() - start} seconds. ")

input("\n\nPress enter to exit. ")
exit()