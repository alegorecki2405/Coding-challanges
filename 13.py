#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
#
def find_str(s,k):
    already_there = []
    len_of_the_longest = 0
    for i in range(0,len(s)):
        for j in range(i-1,len(s)):
            if len(set(already_there)) == k:
                if s[j] in already_there:
                    already_there.append(s[j])

                else:
                    if len_of_the_longest < len(already_there):
                        len_of_the_longest = len(already_there)

                    break
            else:
                already_there.append(s[j])
        already_there = []
    print(s)
    return len_of_the_longest






print(find_str("abcbcccccccca",2))

