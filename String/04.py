# 4. Remove one string from another string, if present.

def remove_substring(main, remove):
    result = ""
    i = 0
    while i < len(main):
        if main[i:i+len(remove)] == remove:
            i += len(remove)
        else:
            result += main[i]
            i += 1
    return result

main_str = input("Enter the main string: ")
remove_str = input("Enter the string to remove: ")

final_str = remove_substring(main_str, remove_str)
print("Final string:", final_str)
