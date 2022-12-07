original_arrangement = {
    1: ["D", "M", "S", "Z", "R", "F", "W", "N"],
    2: ["W","P", "Q", "G", "S"],
    3: ["W", "R", "V", "Q", "F", "N", "J", "C"],
    4: ["F", "Z", "P", "C", "G", "D", "L"],
    5: ["T", "P", "S"],
    6: ["H", "D", "F", "W", "R", "L"],
    7: ["Z", "N", "D", "C"],
    8: ["W", "N", "R", "F", "V", "S", "J", "Q"],
    9: ["R", "M", "S", "G", "Z", "W", "V"]
}
format_string = ""
with open('input.txt') as f:
    for line in f:
        split_line = line.split()
        print(split_line)
        if len(split_line) != 0 and split_line[0] == "move":
            amount = int(split_line[1])
            origin = int(split_line[3])
            destination = int(split_line[5])
            counter = 0
            print(amount)
            #get subset and push each to destination
            #while counter < amount:
            print(f'Moving {amount} from {origin} to {destination}')
            print('before move: ', original_arrangement[destination])
            moved_items = original_arrangement[origin][len(original_arrangement[origin]) - amount:]
            moved_items.reverse()
            print("moving items: ", moved_items)
            print("moving items from: ", original_arrangement[origin])
            for item in moved_items:
                original_arrangement[destination].append(item)
                original_arrangement[origin].remove(item)
                #counter += 1
            print('after move: ', original_arrangement[destination])

for item in original_arrangement:
    format_string += original_arrangement[item].pop()
print(format_string)