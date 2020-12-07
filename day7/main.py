import day7.part1
import day7.part2
import day7.data
import day7.example_data


def main():
    result_part1 = day7.part1.main(day7.data)
    test_result_part1 = day7.part1.test(day7.example_data)
    result_part2 = day7.part2.main(day7.data)
    test_result_part2 = day7.part2.test(day7.example_data)
    test_result_part2_second_data = day7.part2.test_second_data(day7.example_data)

    print('Day 7: Handy Haversacks')
    print('--------------------')

    if result_part1 is None and result_part2 is None:
        print('Not participated')

    if result_part1 is not None:
        if result_part1 == day7.data.result_part1:
            print('Part 1 finished successfully')
        else:
            print('Test Part 1')
            print('')

            if test_result_part1 == day7.example_data.result_part1:
                print('Test successful')
            else:
                print('Test unsuccessful')
                print('Answer: ' + str(test_result_part1))

            print('Part 1')
            print('Answer: ' + str(result_part1))
            print('')

    if result_part2 is not None:
        print('--------------------')

        if result_part2 == day7.data.result_part2:
            print('Part 2 finished successfully')
        else:
            print('Test Part 2')

            if test_result_part2 == day7.example_data.result_part2:
                print('Test successful')
            else:
                print('Test unsuccessful')
                print('Answer: ' + str(test_result_part2))

            if test_result_part2_second_data == day7.example_data.result_part2_second_data:
                print('Test successful')
            else:
                print('Test unsuccessful')
                print('Answer: ' + str(test_result_part2_second_data))


            print('')
            print('Part 2')
            print('Answer: ' + str(result_part2))


if __name__ == '__main__':
    main()
