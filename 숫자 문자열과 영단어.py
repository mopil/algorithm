def solution(s):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for n in range(0, len(nums)):
        s = s.replace(nums[n], str(n))
    return int(s)