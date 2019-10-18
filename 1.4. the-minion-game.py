# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.
#
# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


def minion_game(string):
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0

    # following did not work due to performance :(

    # for i, l in enumerate(string):
    #     sub = string[i:]
    #     for j in range(len(sub)):
    #         ssub = sub[:j + 1]
    #         if len(ssub) > 0:
    #             if ssub[0] in vowels:
    #                 kevin += 1
    #                 print(ssub)
    #             else:
    #                 print(ssub)
    #                 stuart += 1

    for i, l in enumerate(string):
        if l in vowels:
            kevin += (len(string) - i)
        else:
            stuart += (len(string) - i)

    # print(kevin, stuart)
    if kevin > stuart:
        print('Kevin', kevin)
    elif kevin == stuart:
        print('Draw')
    else:
        print('Stuart', stuart)


if __name__ == '__main__':
    # s = input()
    minion_game('BANANA')
