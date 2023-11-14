# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def day1(file_name):
    # Use a breakpoint in the code line below to debug your script.
    max_Calories = 0
    Elf_with_max_Calories = ""
    suma = 0
    cnt = 1
    elfs_dict = {}
    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()

    for line in all_lines:
        # Still on current Elf  information
        if line != "\n":
            suma += int(line.rstrip())
        else:
            # Switch to new Elf information
            elfs_dict[cnt] = suma
            if suma > max_Calories:
                max_Calories = suma
                Elf_with_max_Calories = 'Elf' + str(cnt)
            elif suma == max_Calories:
                Elf_with_max_Calories = Elf_with_max_Calories + ', ' + 'Elf' + str(cnt)
            suma = 0
            cnt += 1

    print("Max number of Calories carried by an Elf is: ", max_Calories)
    print("The Elf or Elfs carrying that number of Calories is/are: ", Elf_with_max_Calories)
    sorted_elfs_by_Calories = sorted(elfs_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = dict(sorted_elfs_by_Calories)
    l_keys = list(sorted_dict.keys())
    print("Top 3 max calories sum is: ", (sorted_dict[l_keys[0]] + sorted_dict[l_keys[1]] + sorted_dict[l_keys[2]]))


def day2(file_name):
    scores = {}
    scores_v2 = {}
    # A and X = Rock => value 1
    # B and Y = Paper => value 2
    # C and Z = Scissors => value 3
    scores["A X"] = 3 + 1
    scores["A Y"] = 6 + 2
    scores["A Z"] = 0 + 3
    scores["B X"] = 0 + 1
    scores["B Y"] = 3 + 2
    scores["B Z"] = 6 + 3
    scores["C X"] = 6 + 1
    scores["C Y"] = 0 + 2
    scores["C Z"] = 3 + 3

    # X means loose => value 0 Rock => value 1
    # Y means draw => value 3 Paper => value 2
    # Z means win => value 6 Scissors => value 3
    scores_v2["A X"] = 0 + 3
    scores_v2["A Y"] = 3 + 1
    scores_v2["A Z"] = 6 + 2
    scores_v2["B X"] = 0 + 1
    scores_v2["B Y"] = 3 + 2
    scores_v2["B Z"] = 6 + 3
    scores_v2["C X"] = 0 + 2
    scores_v2["C Y"] = 3 + 3
    scores_v2["C Z"] = 6 + 1

    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()

    total_score = 0
    total_score_v2 = 0
    for line in all_lines:
        total_score += int(scores[line.rstrip()])
        total_score_v2 += int(scores_v2[line.rstrip()])

    print("Total score is: ", total_score)
    print("Total score v2 is: ", total_score_v2)


def day3(file_name):
    prioValues = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()
    sum_prio = 0

    for line in all_lines:
        woEOL_line = line.rstrip('\n')
        half_line = int(len(line)/2)
        unique_char_line = {}
        for c in woEOL_line[:half_line]:
            unique_char_line[c] = prioValues.find(c)
        for c in unique_char_line.keys():
            if c in woEOL_line[half_line:]:
                sum_prio += prioValues.find(c)
                #print("Double character found: " + c + " with prio " + str(prioValues.find(c)))

    print("Total sum of priorities for repeating items is: ", sum_prio)


def day3_part2(file_name):
    prioValues = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()
    sum_prio = 0

    for grpCnt in range(0, len(all_lines), 3):
        line = all_lines[grpCnt].rstrip('\n')
        #print(line)
        #print(all_lines[grpCnt+1].rstrip('\n'))
        #print(all_lines[grpCnt+2].rstrip('\n'))
        unique_char_line = {}
        for c in line:
            unique_char_line[c] = prioValues.find(c)
        for c in unique_char_line.keys():
            if (c in all_lines[grpCnt+1]) and (c in all_lines[grpCnt+2]):
                sum_prio += prioValues.find(c)
                #print("Group badge found: " + c + " with prio " + str(prioValues.find(c)))
                break

    print("Total sum of priorities for each group badge is: ", sum_prio)


def day4_part1(file_name):
    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()
    count = 0

    for line in all_lines:
        line = line.strip('\n')
        #print(line)
        ranges = line.split(',')
        borders = ranges[0].split('-') + ranges[1].split('-')
        if ((int(borders[0]) >= int(borders[2])) and (int(borders[1]) <= int(borders[3]))) \
                or ((int(borders[0]) <= int(borders[2])) and (int(borders[1]) >= int(borders[3]))):
            count += 1
            #print(borders)

    print("There is a total of " + str(count) + " assignment pairs where one range fully contain the other")


def day4_part2(file_name):
    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()
    count = 0

    for line in all_lines:
        line = line.strip('\n')
        #print(line)
        ranges = line.split(',')
        borders = ranges[0].split('-') + ranges[1].split('-')
        if ((int(borders[0]) >= int(borders[2])) and (int(borders[0]) <= int(borders[3]))) \
                or ((int(borders[1]) >= int(borders[2])) and (int(borders[1]) <= int(borders[3]))) \
                or ((int(borders[2]) >= int(borders[0])) and (int(borders[2]) <= int(borders[1]))) \
                or ((int(borders[3]) >= int(borders[0])) and (int(borders[3]) <= int(borders[1]))):
            count += 1
            #print(borders)

    print("There is a total of " + str(count) + " assignment pairs where the two ranges overlap")


def day5_part1(file_name):
    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()
    stacks = {}
    count = 0

    for line in all_lines:
        if line != "\n":
            count += 1
        else:
            break
    #print(count)

    for i in range(count-1, -1, -1):
        #print(all_lines[i])
        for c in range(0, len(all_lines[i]), 4):
            if i == (count-1):
                stacks[all_lines[i][c+1]] = []
            else:
                if all_lines[i][c+1] != " ":
                    stacks[all_lines[count-1][c+1]].append(all_lines[i][c+1])

    #print(stacks)
    for i in range(count+1, len(all_lines), 1):
        line = all_lines[i].strip('\n')
        #print(line)
        list_of_moves = line.split(' ')     # move x from y to z
        for j in range(int(list_of_moves[1])):
            stacks[list_of_moves[5]].append(stacks[list_of_moves[3]][-1])
            stacks[list_of_moves[3]].pop()
        #print(stacks)

    last_crates = ""
    for k in stacks.keys():
        last_crates += stacks[k][-1]
    print("Last crates list for CrateMover 9000 is: ", last_crates)


def day5_part2(file_name):
    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()
    stacks = {}
    count = 0

    for line in all_lines:
        if line != "\n":
            count += 1
        else:
            break
    #print(count)

    for i in range(count-1, -1, -1):
        #print(all_lines[i])
        for c in range(0, len(all_lines[i]), 4):
            if i == (count-1):
                stacks[all_lines[i][c+1]] = []
            else:
                if all_lines[i][c+1] != " ":
                    stacks[all_lines[count-1][c+1]].append(all_lines[i][c+1])

    #print(stacks)
    for i in range(count+1, len(all_lines), 1):
        line = all_lines[i].strip('\n')
        #print(line)
        list_of_moves = line.split(' ')     # move x from y to z
        nr_of_moves = int(list_of_moves[1])
        stacks[list_of_moves[5]] += stacks[list_of_moves[3]][-nr_of_moves:]
        rem_items = len(stacks[list_of_moves[3]]) - nr_of_moves
        stacks[list_of_moves[3]] = stacks[list_of_moves[3]][:rem_items]
        #print(stacks)

    last_crates = ""
    for k in stacks.keys():
        last_crates += stacks[k][-1]
    print("Last crates list for CrateMover 9001 is: ", last_crates)


def day6_part1(file_name):
    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()

    for line in all_lines:
        line = line.strip('\n')
        for i in range(len(line)-4):
            four = line[i:i+4]
            #print(four)
            four_dict = dict.fromkeys(four, 1)
            #print(four_dict)
            if len(four_dict.keys()) == 4:
                break
    print("The first start-of-packet marker is after character: ", i+4)


def day6_part2(file_name):
    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()

    for line in all_lines:
        line = line.strip('\n')
        for i in range(len(line)-14):
            fourteen = line[i:i+14]
            #print(fourteen)
            fourteen_dict = dict.fromkeys(fourteen, 1)
            #print(fourteen_dict)
            if len(fourteen_dict.keys()) == 14:
                break
    print("The first start-of-message marker is after character: ", i+14)


def day7_part1(file_name):
    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()


def day7_part2(file_name):
    file1 = open(file_name, 'r')
    all_lines = file1.readlines()
    file1.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #elfs = day1("D:\\AdventOfCode2022\\day1_input.txt")
    #day2("D:\\AdventOfCode2022\\day2_input.txt")
    #day3("D:\\AdventOfCode2022\\day3_input.txt")
    #day3_part2("D:\\AdventOfCode2022\\day3_input.txt")
    #day4_part1("D:\\AdventOfCode2022\\day4_input.txt")
    #day4_part2("D:\\AdventOfCode2022\\day4_input.txt")
    #day5_part1("D:\\AdventOfCode2022\\day5_input.txt")
    #day5_part2("D:\\AdventOfCode2022\\day5_input.txt")
    #day6_part1("D:\\AdventOfCode2022\\day6_input.txt")
    #day6_part2("D:\\AdventOfCode2022\\day6_input.txt")
    day7_part1("D:\\AdventOfCode2022\\day7_input.txt")
    day7_part2("D:\\AdventOfCode2022\\day7_input.txt")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
