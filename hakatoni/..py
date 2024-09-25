def manual_max(numbers):
    max = numbers[0]

    for num in numbers:
        if num > max:
            max = num
    return max

print(manual_max([42,6,22332,123,25,2]))
    
# შექმენით manual_min() ფუნქცია. ანუ უნდა შექმნათ ისეთი ფუნქცია რომელიც იპოვის მინიმალურ რიცხვს რაიმე list'ში, min() ფუნქციის გამოყენების გარეშე.												
def manual_min(numbers):
    min = numbers[0]

    for num in numbers:
        if num < min:
            min = num
    return min

print(manual_min([42,6,22332,123,25,2])) 