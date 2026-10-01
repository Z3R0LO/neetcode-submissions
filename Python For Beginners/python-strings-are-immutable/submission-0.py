def remove_fourth_character(word: str) -> str:
    pass

    #length of word > 4
    #remove 4 character and return new string

    p1 = word[0:3]
    p2 = word[4:]

    new_string = p1 + p2 

    return new_string











# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
