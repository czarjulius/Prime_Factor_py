class PrimeFactor:
    def of(number):
        factors=[]

        if type(number) == int:

            if number < 2:
                return []

            for factor in range(2,number+1):
                while number%factor==0:
                    factors.append(factor)
                    number =number/factor

        return factors