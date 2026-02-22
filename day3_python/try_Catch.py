# prompt = "Enter a string"
# speed = input(prompt)
# int(speed)
# print(speed)
inp = input()
try:
    fahr = float(inp)
    cel = (fahr - 32) * 5/9
    print(fahr)
    print(cel)
except:
    print("Please enter a number")
