import re

def getInput(path):
    with open(path) as f:
        return f.read().splitlines()

def decodePart1(lines):
    codes = []
    for text in lines:
        numbers = []
        for c in text:
            if c in [str(n) for n in range(1, 10)]:
                numbers.append(c)
        codes.append(numbers[0] + numbers[-1])
    return codes

def codeSum(codes):
    return sum([int(n) for n in codes])

### part 2 ###

def decodePart2(lines):
    translate = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    regularExpression = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    codes = []
    for line in lines:
        matches = re.finditer(regularExpression, line)
        code = [match.groups()[0] for match in matches]
        for i, val in enumerate(code):
            if val in translate.keys():
                code[i] = str(translate[val])
                
        codes.append(code[0]+code[-1])
    return codes
        
def main():
    path = "day1/"
    lines = getInput(path+"input.txt")
    print(codeSum(decodePart1(lines)))
    print(codeSum(decodePart2(lines)))

if __name__ == "__main__":
    main()