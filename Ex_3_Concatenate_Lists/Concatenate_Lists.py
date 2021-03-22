"""
I had a transit accident and I don't remember my mane help me, please!!
"""
memory_1 = ["M", "na", "i", "Jo", "Bla"]
memory_2 = ["y", "me", "s", "e", "ck"]

result = []
for men_1, men_2 in zip(memory_1, memory_2):
    word = men_1+men_2
    result.append(word)

print(result)
