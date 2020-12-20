def jump(argument, index):
    if argument[0] == '+':
        index += int(argument[1:])
    if argument[0] == '-':
        index -= int(argument[1:])
    return index


def accumulate(argument, accumulator):
    if argument[0] == '+':
        accumulator += int(argument[1:])
    if argument[0] == '-':
        accumulator -= int(argument[1:])
    return accumulator 


def find_start_of_infinite_loop(instructions, index, instruction_list, accumulator):
    instruction = instructions[index]
    operation = instruction.split(" ")[0]
    argument = instruction.split(" ")[1]

    if (index, instruction) in instruction_list:
        return accumulator
    
    instruction_list.append((index, instruction))

    if operation == 'nop':
        index += 1
    if operation == 'acc':
        accumulator = accumulate(argument, accumulator)
        index += 1
    if operation == 'jmp':
        index = jump(argument, index)

    return find_start_of_infinite_loop(instructions, index, instruction_list, accumulator)


def read_lines_in_file_to_list(filename: str):
    with open(filename, "r") as f:
        return [line.strip("\n") for line in f]


def main():
    instructions = read_lines_in_file_to_list("input8.txt")
    index = 0
    instruction_list = list()
    accumulator = 0
    accumulator = find_start_of_infinite_loop(instructions, index, instruction_list, accumulator)
    print(accumulator)


if __name__ == "__main__":
    main()
