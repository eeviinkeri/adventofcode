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


def parse_instruction(instruction):
    instruction_split = instruction.split(" ")
    return instruction_split[0], instruction_split[1]


def run_instruction(instruction, index, accumulator):
    operation, argument = parse_instruction(instruction)
    if operation == 'nop':
        index += 1
    if operation == 'acc':
        accumulator = accumulate(argument, accumulator)
        index += 1
    if operation == 'jmp':
        index = jump(argument, index)
    return index, accumulator


def find_start_of_infinite_loop(instructions, index, index_list, accumulator):
    instruction = instructions[index]
    if index in index_list:
        return accumulator

    index_list.append(index)
    index, accumulator = run_instruction(instruction, index, accumulator)
    return find_start_of_infinite_loop(instructions, index, index_list, accumulator)


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
