import day4.part1
import day4.part2
import day4.data
import day4.example_data
from datetime import datetime


def main():
    start_time = datetime.now()
    result_part1 = day4.part1.main(day4.data)
    test_result_part1 = day4.part1.test(day4.example_data)
    result_part2 = day4.part2.main(day4.data)
    test_result_part2 = day4.part2.test(day4.example_data)

    print('Day 4: Passport Processing')
    print('--------------------')

    if result_part1 is None and result_part2 is None:
        print('Not participated')

    if result_part1 is not None:
        if result_part1 == day4.data.result_part1:
            print('Part 1 finished successfully')
        else:
            print('Test Part 1')
            print('')

            if test_result_part1 == day4.example_data.result_part1:
                print('Test successful')
            else:
                print('Test unsuccessful')
                print('Answer: ' + str(test_result_part1))

            print('Part 1')
            print('Answer: ' + str(result_part1))
            print('')

    if result_part2 is not None:
        print('--------------------')

        if result_part2 == day4.data.result_part2:
            print('Part 2 finished successfully')
        else:
            print('Test Part 2')

            if test_result_part2 == day4.example_data.result_part2:
                print('Test successful')
            else:
                print('Test unsuccessful')
                print('Answer: ' + str(test_result_part2))

            print('')
            print('Part 2')
            print('Answer: ' + str(result_part2))

    end_time = datetime.now()
    print('')
    print('Duration: ', format(end_time - start_time))


if __name__ == '__main__':
    main()
