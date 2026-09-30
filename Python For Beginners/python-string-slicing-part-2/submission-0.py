def first_n_characters(s: str, n: int) -> str:
    pass

    return s[:n]

def last_n_characters(s: str, n: int) -> str:
    pass

    lastchar = len(s) - n 

    return s[lastchar:]

# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3)) #print tcode need ode
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8)) #print blank need Neetcode
