import day3.part1 as part1
    

def filter_report(diagnostic_report, bit, i):
    report_list = []
    for report in diagnostic_report:
        if report[i] == str(bit):
            report_list.append(report)
    return report_list


def get_co2_scrubber_rating(diagnostic_report):
    least_common_bit = part1.find_least_common_bit(0, diagnostic_report)
    filtered_diagnostic_report = filter_report(diagnostic_report, least_common_bit, 0)
    for i in range(1, 12):
        least_common_bit = part1.find_least_common_bit(i, filtered_diagnostic_report)
        filtered_diagnostic_report = filter_report(filtered_diagnostic_report, least_common_bit, i)
        if len(filtered_diagnostic_report) == 1:
            return filtered_diagnostic_report[0]
            

def get_oxygen_generator_rating(diagnostic_report):
    most_common_bit = part1.find_most_common_bit(0, diagnostic_report)
    filtered_diagnostic_report = filter_report(diagnostic_report, most_common_bit, 0)
    for i in range(1, 12):
        most_common_bit = part1.find_most_common_bit(i, filtered_diagnostic_report)
        filtered_diagnostic_report = filter_report(filtered_diagnostic_report, most_common_bit, i)
        if len(filtered_diagnostic_report) == 1:
            return filtered_diagnostic_report[0]



def main():
    diagnostic_report = part1.read_lines_in_file_to_list('day3/input.txt')

    oxygen_generator_rating = get_oxygen_generator_rating(diagnostic_report)
    co2_scrubber_rating = get_co2_scrubber_rating(diagnostic_report)

    life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
    print(f'life support rating of the submarine is {life_support_rating}') 


if __name__ == "__main__":
    main()