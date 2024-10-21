"""
    allAddressList.add(
        Address_Search(
        first: '서울특별시',
        second: '강남구',
        ),
    );
    allAddressList.add(
        Address_Search(
        first: '서울특별시',
        second: '강동구',
        ),
    );
    allAddressList.add(
        Address_Search(
        first: '서울특별시',
        second: '...',
        ),
    );
"""

inputFile = open('input.txt', 'r')
lines = inputFile.readlines()
inputFile.close()

result = ''
first = ''

for i in range(len(lines)):
    line = lines[i].strip()

    if len(line) <= 1:
        continue

    if line[0] == '-':
        first = line[1 : len(line)]
        continue

    second = line
    result += f"allAddressList.add(\n            Address_Search(\n                first: '{first}',\n                second: '{second}',\n            ),\n        );\n\n"

outputFile = open('output.txt', 'w')
outputFile.write(result)
outputFile.close()

print('끝')