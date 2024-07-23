class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        concatenated_string = ''.join(map(str, digits))
        result_number = int(concatenated_string) + 1
        number_str = str(result_number)
        digit_list = [int(digit) for digit in number_str]
        return digit_list
