harmonic_number = '''5. Harmonic Number
a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
(http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
b. I/P -> The Harmonic Value N. Ensure N != 0
c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
d. O/P -> Print the Nth Harmonic Value.
'''
number = int(input("Please enter the number: "))
harmonic_number = 0
for i in range(1,number+1):
    harmonic_number = harmonic_number+1/i #0+1,1+1/2,1+1/2+1/3....
print(float(harmonic_number))
