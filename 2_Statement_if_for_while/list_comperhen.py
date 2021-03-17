
#4. Using list comprehension to creat a list of the first letters of every word in the string ( insert by input())
print("Using list comprehension to creat a list of the first letters of every word in the string ( insert by input())\n")
IP_Str = input("Insert the String you want: ")
Proc_Str = IP_Str.split()

result_list =[word[0] for word in Proc_Str]

print("The string result is: ")
print(*result_list, sep = "; ")
