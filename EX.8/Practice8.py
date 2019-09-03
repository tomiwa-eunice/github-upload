# ex.8.1
# reading text files
f = open('myfile.txt', 'w')
lines = ['write something\n', 'write something else\n']
f.writelines(lines)
f.close()
print(f)

f = open('myfile.txt', 'a')
print(f)

f.write('I append this line of text')
f.close()

f = open('myfile.txt', 'r')
print(f)


text = f.read()
print(text)



f = open('points.txt', 'r')

new_points = []

for line in f:
    new_points.append(line.split())

print(new_points)


def count_char(filePath):
    f = open(filePath)
    story = f.read().upper().replace('\n', '').replace('\t', '').replace(' ', '')
    f.close()
    chars = {}  # dictionary in which (key:value) will be (character:count)
    for c in story:
        if c in chars:
            chars[c] = chars[c] + 1
        else:
            chars[c] = 1
    for c in chars:
        print(c, chars[c])

print(count_char('snark.txt'))