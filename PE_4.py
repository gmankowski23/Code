#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#This first line is defining that my list is empty
pallist = []

#I need the product of two 3-digit numbers, so i create a range for my 2 digits
for x in range(1,1000):
    for y in range(1,1000):

#This multiplies my two digits together
        num = x * y

#This line reverses my "num" and compares it to the original "num"
#If both of these values are equal to eachother it adds them to my list
        rev = int(str(num)[::-1])
        if num == rev:
            pallist.append(rev)

#This line takes all the numbers in my list and prints the largest of themff
print (max(pallist))
