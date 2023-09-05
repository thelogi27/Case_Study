import json

result = []

for i in range(1, 101):
    output = ""

    if i % 3 == 0:
        output += "BIG"
    if i % 5 == 0:
        output += "BANG"
    if output == "":
        output = str(i)

    result.append(output)

with open('output.json', 'w') as output_file:
    json.dump(result, output_file)

print("Result has been saved to 'output.json' file.")
