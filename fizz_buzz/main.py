def fizz_buzz(num):

    string=""

    if num % 3 == 0:
        string += "Fizz"
    if num % 5 == 0:
        string += "Buzz"
    if string == "":
        return num

    return string


if __name__ == "__main__":

    [ print(fizz_buzz(num=i)) for i in range(1,101) ]
