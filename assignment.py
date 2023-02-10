def sum (num_list):
    sum = 0
    for i in num_list:
        sum +=i
    return sum

def multiplication (num_list):
    result = 1
    for i in num_list:
        result *= i
    return result

def main ():
    input_list = list(input("Enter a list of numbers, separate each number by space: ").split())
    num_list = [int(i) for i in input_list]
    print("Sum of the list: " + str(sum(num_list)))
    print("Product of the list: " + str(multiplication(num_list)))
    
if __name__ == '__main__':
    main()
    