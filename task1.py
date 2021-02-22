"""
    Написать функцию, которая принимает список строк,
    и возвращает другой список, содержащий все самые длинные строки.
    Например:
    [in] ['a', 'asd', 'bd', 'q', 'dsq']
    [out] ['asd', 'dsq']
"""
import re

def main():
    list_in = input("Enter string: ")
    words = re.findall(r"\w+", list_in)
    longest_strings(words)


def longest_strings(words):
    longest_word = words[0]
    new_list = []
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    for word in words:
        if len(word) == len(longest_word):
            new_list.append(word)
    print(f"Longest words: {new_list}")
    return new_list

if __name__ == "__main__":
    main()



t_1 = ["x"]
assert longest_strings(t_1) == ["x"]

t_2 = ["abc", "eeee", "abcd", "dcd"]
assert longest_strings(t_2) == ["eeee", "abcd"]

t_3 = ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
assert longest_strings(t_3) == ["zzzzzz", "abcdef", "aaaaaa"]

t_4 = ["enyky", "benyky", "yely", "varennyky"]
assert longest_strings(t_4) == ["varennyky"]

t_5 = ["abacaba", "abacab", "abac", "xxxxxx"]
assert longest_strings(t_5) == ["abacaba"]

print("All tests passed successfully!")