class utils:
    def reversed(self, number):
        if type(number) is int:
            #result = int(str(number)[::-1])
            result = 0
            while (number > 0):
                last = number % 10
                result = (result * 10) + last 
                number = number // 10
            print("reversed int:",result)
            return result
        print("reversed: error not an int")
        return None

    def formatter(self, number):
        if type(number) is int: 
            binresult = bin(number)
            octresult = oct(number)
            print("binary:", binresult)
            print("octal:", octresult)
            return binresult, octresult
        print("format: error not an int")
        return None

