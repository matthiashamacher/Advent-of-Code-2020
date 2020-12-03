import dayX.part1
import dayX.part2
import dayX.data
import dayX.example_data


def main():
    result_part1 = dayX.part1.main(dayX.data)
    test_result_part1 = dayX.part1.test(dayX.example_data)
    result_part2 = dayX.part2.main(dayX.data)
    test_result_part2 = dayX.part2.test(dayX.example_data)

    print('Day X: XXXXXXXXXXXXX')
    print('--------------------')

    if result_part1 is None and result_part2 is None:
        print('Not participated')

    if result_part1 is not None:
        if result_part1 == dayX.data.result_part1:
            print('Part 1 finished successfully')
        else:
            print('Test Part 1')
            print('')

            if test_result_part1 == dayX.example_data.result_part1:
                print('Test successful')
            else:
                print('Test unsuccessful')
                print('Answer: ' + str(test_result_part1))

            print('Part 1')
            print('Answer: ' + str(result_part1))
            print('')

    if result_part2 is not None:
        print('--------------------')

        if result_part2 == dayX.data.result_part2:
            print('Part 2 finished successfully')
        else:
            print('Test Part 2')

            if test_result_part2 == dayX.example_data.result_part2:
                print('Test successful')
            else:
                print('Test unsuccessful')
                print('Answer: ' + str(test_result_part2))

            print('')
            print('Part 2')
            print('Answer: ' + str(result_part2))


if __name__ == '__main__':
    main()
