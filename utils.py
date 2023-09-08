class utils:
    def resversed(self, number):
        if type(number) is int:
            return int(str(number)[::-1])
        return None

    def formatter(self, number):
        if type(number) is int: 
            return bin(number), oct(number)
        return None
