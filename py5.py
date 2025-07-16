#write a program to count words,lines and characters in a user-provided sentence.

a=input("Enter the sentence:")
count=0
words=len(a.split())
print("No.of words:",words)
print("No. of lines:",len(a.split(sep="."))-1)
for i in a.split():
   count=count+len(i)
print("No of characters:",count)




