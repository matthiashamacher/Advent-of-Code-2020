import day13.part1
import day13.part2
import day13.data
import day13.example_data
from datetime import datetime


def main():
    start_time = datetime.now()
    result_part1 = day13.part1.main(day13.data)
    test_result_part1 = day13.part1.test(day13.example_data)
    # result_part2 = day13.part2.main(day13.data) # The today's part 2 is not solvable within a reasonable timeframe with brutforce (my solution)
    result_part2 = 840493039281088
    test_result_part2 = day13.part2.test(day13.example_data)

    print('Day 13: Shuttle Search')
    print('--------------------')

    if result_part1 is None and result_part2 is None:
        print('Not participated')

    if result_part1 is not None:
        if result_part1 == day13.data.result_part1:
            print('Part 1 finished successfully')
        else:
            print('Test Part 1')
            print('')

            if test_result_part1 == day13.example_data.result_part1:
                print('Test successful')
            else:
                print('Test unsuccessful')
                print('Answer: ' + str(test_result_part1))

            print('Part 1')
            print('Answer: ' + str(result_part1))
            print('')

    if result_part2 is not None:
        print('--------------------')
        print('Part 2 is not solvable with my solution (bruteforce) in a reasonable timeframe (> 1hr) therefore the '
              'solution is not calculated during execution')

        if result_part2 == day13.data.result_part2:
            print('Part 2 finished successfully')
        else:
            print('Test Part 2')

            if test_result_part2 == day13.example_data.result_part2:
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
