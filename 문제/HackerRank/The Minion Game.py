'''
#The Minion Game
https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
'''
def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Stuart", stuart_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)