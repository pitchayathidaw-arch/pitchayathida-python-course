# รับชื่อจริง (หรือข้อความ)จากผู้ใช้
# นับจำนวนสระทังหมดในข้อความนั้นว่ามีกี่ตัว (a,e,i,o,u)

# ตัวอย่างหน้าจอ
# what is your name ?:Pitchayathida
# Your text have 4 vowels.
name = input("What is your name?:")

letters= list(name)
print(letters)


""
count = 0
for letter in name:
    if letter =='a' or letter =='A':
        count = count +1
    if letter == 'e' or letter == 'E':
        count = count +1
    if letter == 'i' or letter == 'I':
        count = count +1
    if letter == 'o' or letter == 'O':
        count = count +1
    if letter == 'u' or letter == 'U':
        count = count +1
    #print(f"ตัวอักษร:{letter}")

print("Your text have",count,"vowels")