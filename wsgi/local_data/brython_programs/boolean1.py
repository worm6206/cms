'''
program: boolean1.py
'''
print(None == None)
print(None is None)

print(True is True)

print([] == [])
print([] is [])

print("Python" is "Python")

'''
not 關鍵字使用
'''

grades = ["A", "B", "C", "D", "E", "F"]

grade = "L"

if grade not in grades:
    print("unknown grade")

'''
and 關鍵字使用
'''

sex = "M"
age = 26

if age < 55 and sex == "M":
    print("a young male")
   
name = "Jack"

if ( name == "Robert" or name == "Frank" or name == "Jack" 
      or name == "George" or name == "Luke"):
    print("This is a male")