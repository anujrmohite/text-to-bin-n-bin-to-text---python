message="hello, i am anuj mohite "
#3->0011 | 5->1001
#this is to incode this 
binary=" ".join(format(ord(c),"b")for c in message)
print(binary)
#but to decode this
#The ord() function returns the number representing the unicode code of a specified character.
#give the solution of this to the new variable binary_text
binary_text="1101000 1100101 1101100 1101100 1101111 101100 100000 1101001 100000 1100001 1101101 100000 1100001 1101110 1110101 1101010 100000 1101101 1101111 1101000 1101001 1110100 1100101 100000"
#x = chr(97) -> print(x) -> it gives 'a'
normal="".join(chr(int(c,2))for c in binary_text.split(" "))
print("This is the binary provided to the binary_text: ",normal)