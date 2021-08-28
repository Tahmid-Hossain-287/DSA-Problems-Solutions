'''
Problem link: https://leetcode.com/problems/longest-common-prefix/submissions/

Problem name: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

'''
        

def solution(strs): 

    smallest_element = min(strs, key=len)
        

    if '' in strs:  # If the list contains empty string, it will return empty string.
        return ''
    elif len(strs) == 1:  # If the list has only one item, it will return only that.
        return strs[0]

    # base_word = strs[0]
    base_word = smallest_element
    word_len = len(base_word)
    letter_count = 1
    matched_letters = []
    # for words in strs[1:]:  # Starts the loop with skipping the first word, that is the base word.
    for words in strs:
        for letters in words:  # Starts iterating through the letters of each word.
            # print(words[:letter_count], base_word[:letter_count])

            if words == base_word:
                matched_letters.append(words)

            elif words[:letter_count] == base_word[:letter_count]:  # If the prefix of base word and current word matches.
                letter_count += 1  # Continue the checking while increasing the letter limit.
                continue
                
            elif words[:letter_count] != base_word[:letter_count]:  # If the letter of the current word does not match the base word, store the upto the position they did match.
                matched_letters.append(words[:(letter_count-1)])
                letter_count = 1
                continue

    
    answer = (min(matched_letters, key=len))
    answer_length = len(answer)
    if_answer_matches = 0
    for all in matched_letters:
        if answer in all[:answer_length]:
            if_answer_matches += 1
    if if_answer_matches == len(matched_letters):
        return answer
    else:
        return ''
            

# test_case = ["a","aca","accb","b"]

# print(solution(test_case))


# The program crashes because the word that is being tested gets finished while being still processed.
'''
Note: Don't pick up the first word but the smallest word.
'''




# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         print(strs)
#         smallest_element = min(strs, key=len)


#         if '' in strs:  # If the list contains empty string, it will return empty string.
#             return ''
#         elif len(strs) == 1:  # If the list has only one item, it will return only that.
#             return strs[0]

#         # base_word = strs[0]
#         base_word = smallest_element
#         word_len = len(base_word)
#         letter_count = 1
#         matched_letters = []
#         # for words in strs[1:]:  # Starts the loop with skipping the first word, that is the base word.
#         for words in strs:
#             for letters in words:  # Starts iterating through the letters of each word.
#                 # print(words[:letter_count], base_word[:letter_count])

#                 if words == base_word:
#                     matched_letters.append(words)

#                 elif words[:letter_count] == base_word[:letter_count]:  # If the prefix of base word and current word matches.
#                     letter_count += 1  # Continue the checking while increasing the letter limit.
#                     continue

#                 elif words[:letter_count] != base_word[:letter_count]:  # If the letter of the current word does not match the base word, store the upto the position they did match.
#                     matched_letters.append(words[:(letter_count-1)])
#                     letter_count = 1
#                     continue


#         answer = (min(matched_letters, key=len))
#         answer_length = len(answer)
#         if_answer_matches = 0
#         for all in matched_letters:
#             if answer in all[:answer_length]:
#                 if_answer_matches += 1
#         if if_answer_matches == len(matched_letters):
#             return answer
#         else:
#             return ''
