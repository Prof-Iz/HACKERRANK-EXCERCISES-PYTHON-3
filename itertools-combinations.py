'''
Task

You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string  and integer value  separated by a space.

Constraints 0 < k <= len(S)


The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string S on separate lines.
Sample Input

HACK 2

Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK

'''
from itertools import combinations
Input = input("Enter Word followed by Max number of Combinations Ex: DOGGY 3:")
S, k = Input.split(" ") #Takes user input and splits it into list based on delimiter
k = int(k) # make integer as it is defaluting to string
S = S.upper() #capitalise input in case user enters simple chars
newComb=[] #initialise temporary intermediate list
final=[] #initialise final list
if k in range(1,len(S)+1): #only does so if k is less than max and is positive int
    S = sorted(S) # sorts S
    while k > 0:
        combination = list(combinations(S,k)) #to generate list of combinations of k length
        for comb in combination:
            comb = "".join(comb) #each combination is combined into a word
            newComb.append(comb) #append each one to intermediate list
            
        k -= 1 #reduce k to get other combinations
        # newComb.sort() not required if S is sorted before passing to combinations
        newComb = reversed(newComb) #reversing new Comb as we want ouput to be lenght wise
        final += newComb #add reversed list to final
        newComb=[] #reset intermediate list


for i in reversed(final): 
    #reverse the final list one more time to make it lexographically ordered by length
    print (i)