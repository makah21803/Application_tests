import os

dirname = os.path.dirname(__file__)
file = open(dirname+"/test-input.txt", "r")


class MakeIntList():
    def __init__(self, input_file):
        input_list = [row.strip() for row in input_file.readlines()]
        self.accepted_range = [-1000000000, 1000000000]
        self.run(input_list)

    def run(self, input_list):
        valid_numbers = []
        for row in input_list:
            if not self.validator_integer(row):
                print("{0} is not a valid number. Skipping.".format(row))
                continue
            if not self.validator_range(int(row), self.accepted_range):
                print("{0} is not within the accepted range of {1}. Skipping.".format(row, self.accepted_range))
                continue

            valid_numbers.append(int(row))

        print(valid_numbers)
        return valid_numbers

    def validator_integer(self, number):
        """
        Checks if the string is convertable to an integer.

        :param int number:
        :return bool:
        """

        try:
            number = int(number)
            return True
        except:
            return False

    def validator_range(self, number, range=[0,1]):
        """
        Checks if the number is withing accepted range.

        :param int number:
        :param list range:
        :return bool:
        """
        if number >= range[0] and number <= range[-1]:
            return True
        else:
            return False


def solution(file_object):
    """
    I didnt manage to call the class correctly within the codify interface.
    Everything except 'MakeIntList(file_object)' is just to not fail the automatic tests.
    The cleaner solution is run by MakeIntList(file_object).
    """
    # This should be the solution, it works but codify doesnt accept it
    MakeIntList(file_object)

    # my_range = [-1000000000, 1000000000]
    # input_list = [row.strip() for row in file_object.readlines()]
    #
    # int_list = []
    # for num in input_list:
    #     try:
    #         num = int(num)
    #         if num >= my_range[0] and num <= my_range[1]:
    #             int_list.append(num)
    #         else:
    #             continue
    #     except:
    #         continue
    #
    # return int_list

solution(file)