import day2.part1
import day2.part2
import day2.data
import day2.example_data


def main():
    result_part1 = day2.part1.main(day2.data)
    test_result_part1 = day2.part1.test(day2.example_data)
    result_part2 = day2.part2.main(day2.data)
    test_result_part2 = day2.part2.test(day2.example_data)

    print('Day 2: Password Philosophy')
    print('--------------------')

    if result_part1 == day2.data.result_part1:
        print('Part 1 finished successfully')
    else:
        print('Test Part 1')
        print('')

        if test_result_part1 == day2.example_data.result_part1:
            print('Test successful')
        else:
            print('Test unsuccessful')
            print('Answer: ' + str(test_result_part1))

        print('Part 1')
        print('Answer: ' + str(result_part1))
        print('')

    if result_part2 != 0:
        print('--------------------')

        if result_part2 == day2.data.result_part2:
            print('Part 2 finished successfully')
        else:
            print('Test Part 2')

            if test_result_part2 == day2.example_data.result_part2:
                print('Test successful')
            else:
                print('Test unsuccessful')
                print('Answer: ' + str(test_result_part2))

            print('')
            print('Part 2')
            print('Answer: ' + str(result_part2))


if __name__ == '__main__':
    main()
