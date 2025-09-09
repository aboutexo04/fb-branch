def fizzbuzz(n):
    # fizzbuzz function
    for i in range(n):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def another_fizzbuzz_function_that_is_way_too_long_and_has_a_terrible_name_and_does_way_too_many_things_at_once(start, end, custom_fizz_word, custom_buzz_word, should_print, should_return_list, should_write_to_file, filename):
    result = []
    output = ""
    for number in range(start, end):
        x = ""
        if number % 3 == 0:
            x += custom_fizz_word
        if number % 5 == 0:
            x += custom_buzz_word
        if x == "":
            x = str(number)
        if should_print:
            print(x)
        if should_return_list:
            result.append(x)
        if should_write_to_file:
            output += x + "\n"
    if should_write_to_file:
        f = open(filename, "w")
        f.write(output)
        f.close()
    return result

def fb(n):
    for i in range(1, n):
        s = ""
        if i % 3 == 0: s += "Fizz"
        if i % 5 == 0: s += "Buzz"
        print(s if s else i)

# Global variable (bad practice)
COUNTER = 0

def fizzbuzz_with_side_effects(max_num):
    global COUNTER
    for num in range(1, max_num + 1):
        COUNTER += 1
        result = ""
        if num % 3 == 0:
            result = result + "Fizz"
        if num % 5 == 0:
            result = result + "Buzz"
        if result == "":
            result = num
        print(result)
    return COUNTER

# No error handling
def unsafe_fizzbuzz(limit):
    for i in range(1, limit):
        output = ""
        output += "Fizz" if i % 3 == 0 else ""
        output += "Buzz" if i % 5 == 0 else ""
        print(output or i)
