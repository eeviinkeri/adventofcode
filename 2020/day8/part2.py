from part1 import (
    read_lines_in_file_to_list,
    parse_instruction,
    run_instruction
)

def is_program_finite(instructions, index, index_list, accumulator):
    if index == len(instructions):
        return True, accumulator
    instruction = instructions[index]
    if index in index_list:
        return False, accumulator
    index_list.append(index)
    index, accumulator = run_instruction(instruction, index, accumulator)
    return is_program_finite(instructions, index, index_list, accumulator)


def change_instruction(operation, argument):
    if operation == "nop":
        return f"jmp {argument}"
    if operation == "jmp":
        return f"nop {argument}"


def fix_program(instructions):
    for i in range(len(instructions)):
        instructions_temp = instructions.copy()
        operation, argument = parse_instruction(instructions[i])
        if operation in ("nop", "jmp"):
            instructions_temp[i] = change_instruction(operation, argument)
            is_finite, acc = is_program_finite(
                instructions=instructions_temp,
                index=0,
                index_list=list(),
                accumulator=0)
            if is_finite:
                return acc
    return None


def main():
    instructions = read_lines_in_file_to_list("input8.txt")
    acc = fix_program(instructions)
    print(acc)


if __name__ == "__main__":
    main()
