#priority_list = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import string
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
priority_list = [None] + lowercase + uppercase
priority_dict = {}
priority_sum = 0
for index, data in enumerate(priority_list):
    priority_dict[data] = index
print(priority_dict)

sets_of_three = []
raw_lines = []
with open('input.txt') as f:
    #current_set = 0
    line_to_append = []
    increment = 0
    for line in f:
        print('line before set: ', line.strip())
        raw_lines.append(line.strip())
        if len(line_to_append) < 3:
            #line_to_append.append(set(line.strip()))
            line_to_append.append(line.strip())
            print('line turned into set: ', set(line.strip()))
            increment = increment + 1
        else:
            #line_to_append += line.strip()
            #print('amended line: ', set(list(line_to_append)))
            print('3 LINES: ', line_to_append)
            sets_of_three.append(line_to_append)
            line_to_append = []
            #line_to_append.append(set(line.strip()))
            line_to_append.append(line.strip())
            increment = increment + 1
            #current_set = 0
#print(sets_of_three)
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
raw_chunks = list(chunks(raw_lines, 3))
#print('RAW CHUNKS:', list(raw_chunks))

for chunk in raw_chunks:
    for index, line in enumerate(chunk):
        chunk[index] = set(line)
print('RAW CHUNKS:', raw_chunks)
print("INCREMENT: ", increment)
print(len(raw_chunks))
#assert len(raw_chunks) == 100
for set_col in raw_chunks:
    assert len(set_col) == 3
   # print('dict reset')
    set_dict = {}
    for line in set_col:
       # print('line before set: ', line)
        #print('line turned into set: ', line)
        for item in line:
            if item in set_dict:
                set_dict[item] += 1
            else:
                set_dict[item] = 1
    print('dict: ', set_dict)
    set_dict_is_valid = False
    for letter in set_dict:
        if set_dict[letter] == 3:
            priority_sum += priority_dict[letter]
            #print('letter: ', letter)
            #print("priority: ", priority_dict[letter])
            set_dict_is_valid = True
            #print('priority sum: ', priority_sum)
    assert set_dict_is_valid == True
            



        # pure_line = line.strip()
        # print("half of line: ", len(pure_line) // 2)
        # first_sack = pure_line[0:(len(pure_line) // 2)]
        # second_sack = pure_line[(len(pure_line) // 2):(len(pure_line))]
        # sack_dict = {}
        # for index, data in enumerate(first_sack):
        #     sack_dict[data] = True
        # for i in second_sack:
        #     if i in sack_dict:
        #         print("dupe item: ", i, priority_dict[i])
        #         priority_sum = priority_sum + priority_dict[i]
        #         break
        #print(first_sack)
        #print(second_sack)
print(priority_sum)