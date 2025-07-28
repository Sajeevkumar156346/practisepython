print( (2 + 6) * 12 / 6)
print( (2 + 6) * 12 // 6)
print(12 * 8)
age=21
print("age:" ,int(age))
age=21
print("age:",float(age))
print(bin(6))
print(int(0b110))
print(float(0b110))
#here bin() converts decimal → binary (as a string).
class Number:
    value = 7
    
    def __int__(self):
        return self.value

data = Number()
print("number =", int(data))

