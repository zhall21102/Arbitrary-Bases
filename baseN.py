import math
possible='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
class BaseN:
    """A class to handle arithmetic between bases
       Returns properties of self for natural numbers, decimal values otherwise
       Value can be string representation for natural numbers, otherwise decimal"""
    def __init__(self, value, base, chrSet = possible):
        self.base = base
        self.chrSet = chrSet
        if type(value)== str:
            self.nVal = value
            self.decimal = baseNToDecimal(value, self.base, self.chrSet)
        else:
            self.nVal = decimalToBaseN(value, self.base, self.chrSet)
            self.decimal = value

    def __add__(self,other):
        if self.base == int(self.base) and self.base >= 1:
            if type(other) == BaseN:
                return decimalToBaseN(self.decimal+other.decimal, self.base, self.chrSet)
            elif type(other) == int or type(other) == float:
                return decimalToBaseN(self.decimal+other, self.base, self.chrSet)
        else:
            if type(other) == BaseN:
                return self.decimal+other.decimal
            elif type(other) == int or type(other) == float:
                return self.decimal+other
    def __sub__(self,other):
        if self.base == int(self.base) and self.base > 1:
            if type(other) == BaseN:
                return decimalToBaseN(self.decimal-other.decimal, self.base, self.chrSet)
            elif type(other) == int or type(other) == float:
                return decimalToBaseN(self.decimal-other, self.base, self.chrSet)
        else:
            if type(other) == BaseN:
                return self.decimal-other.decimal
            elif type(other) == int or type(other) == float:
                return self.decimal-other
    def __mul__(self, other):
        if self.base == int(self.base) and self.base > 1:
            if type(other) == BaseN:
                return decimalToBaseN(self.decimal*other.decimal, self.base, self.chrSet)
            elif type(other) == int or type(other) == float:
                return decimalToBaseN(self.decimal*other, self.base, self.chrSet)
        else:
            if type(other) == BaseN:
                return self.decimal*other.decimal
            elif type(other) == int or type(other) == float:
                return self.decimal*other
    def __floordiv__(self, other):
        if self.base == int(self.base) and self.base > 1:
            if type(other) == BaseN:
                return decimalToBaseN(self.decimal//other.decimal, self.base, self.chrSet)
            elif type(other) == int or type(other) == float:
                return decimalToBaseN(self.decimal//other, self.base, self.chrSet)
        else:
            if type(other) == BaseN:
                return self.decimal//other.decimal
            elif type(other) == int or type(other) == float:
                return self.decimal//other
    def __pow__(self, other):
        if self.base == int(self.base) and self.base > 1:
            if type(other) == BaseN:
                return decimalToBaseN(self.decimal**other.decimal, self.base, self.chrSet)
            elif type(other) == int or type(other) == float:
                return decimalToBaseN(self.decimal**other, self.base, self.chrSet)
        else:
            if type(other) == BaseN:
                return self.decimal**other.decimal
            elif type(other) == int or type(other) == float:
                return self.decimal**other
    def __truediv__(self, other):
        if self.base == int(self.base) and self.base > 1:
            if type(other) == BaseN:
                return decimalToBaseN(self.decimal/other.decimal, self.base, self.chrSet)
            elif type(other) == int or type(other) == float:
                return decimalToBaseN(self.decimal/other, self.base, self.chrSet)
        else:
            if type(other) == BaseN:
                return self.decimal/other.decimal
            elif type(other) == int or type(other) == float:
                return self.decimal/other
    def __mod__(self, other):
        if self.base == int(self.base) and self.base > 1:
            if type(other) == BaseN:
                return decimalToBaseN(self.decimal%other.decimal, self.base, self.chrSet)
            elif type(other) == int or type(other) == float:
                return decimalToBaseN(self.decimal%other, self.base, self.chrSet)
        else:
            if type(other) == BaseN:
                return self.decimal%other.decimal
            elif type(other) == int or type(other) == float:
                return self.decimal%other
    
    def fraction(self, other):
        integer=(self.decimal//other.decimal)
        denominator=(other.decimal)
        numerator=(self.decimal-(self.decimal//other.decimal)*denominator)
        gcd=math.gcd(numerator,denominator)
        if numerator != 0 and integer !=0 :
            return '{} {}/{}'.format(decimalToBaseN(integer),\
                                     decimalToBaseN(numerator//gcd, self.base, self.chrSet),\
                                     decimalToBaseN(denominator//gcd, self.base, self.chrSet))
        elif integer != 0:
            return decimalToBaseN(integer, self.base, self.chrSet)
        else:
            return '{}/{}'.format(decimalToBaseN(numerator//gcd, self.base, self.chrSet),\
                                     decimalToBaseN(denominator//gcd, self.base, self.chrSet))
    def factorial(self):
        
        return decimalToBaseN(math.gamma(self.decimal+1), self.base, self.chrSet)
    
    def __eq__(self, other):
        if type(other) == BaseN:
            return self.decimal == other.decimal
        elif type(other) == int or type(other) == float:
            return self.decimal == other
    def __ne__(self, other):
        if type(other) == BaseN:
            return self.decimal != other.decimal
        elif type(other) == int or type(other) == float:
            return self.decimal != other
    def __gt__(self, other):
        if type(other) == BaseN:
            return self.decimal > other.decimal
        elif type(other) == int or type(other) == float:
            return self.decimal > other
    def __ge__(self, other):
        if type(other) == BaseN:
            return self.decimal >= other.decimal
        elif type(other) == int or type(other) == float:
            return self.decimal >= other
    def __lt__(self, other):
        if type(other) == BaseN:
            return self.decimal < other.decimal
        elif type(other) == int or type(other) == float:
            return self.decimal < other
    def __le__(self, other):
        if type(other) == BaseN:
            return self.decimal <= other.decimal
        elif type(other) == int or type(other) == float:
            return self.decimal <= other
        
    def __repr__(self):
        return 'Base {} number {}\nDecimal interpretation: {}\nCharacter set: {}'\
               .format(self.base, self.nVal, self.decimal,self.chrSet)
    def __str__(self):
        return self.nVal


    
def decimalToBaseN(n, base, chrSet = possible):
    """Converts a number N into its equivalent in base BASE
       Only consistently works with Natural Bases"""
    if n<0:
        negative = True
        n=abs(n)
    else:
        negative = False
    
    if int(n) == n:
        n=int(n)
        outputL = []
        output=''
        while(n > 1):
            n,o=helper(n, base, chrSet)
            outputL.append(o)
        outputL.append(n%base)
        outputL=outputL[::-1]
        for e in outputL:
            output+=chrSet[e]
        while output[0] == chrSet[0] and len(output)>1:
            output=output[1:]
        if negative:
            return '-'+output
        else:
            return output
    else:
        precision=10
        integer = decimalToBaseN(int(n), base, chrSet)
        step=n-int(n)
        after=step
        decimal=''
        temp=0
        level=1
        for e in range(precision):
            while after-temp/(base**level)>0:
                after-=temp/(base**level)
                temp+=1
                after=step
            if after-temp/base**level!=0:
                temp-=1
            after-=temp/(base**level)
            step=after
            decimal+=chrSet[temp%base]
            if after == 0:
                if negative:
                    return '-'+integer+'.'+decimal
                else:
                    return integer+'.'+decimal
            temp=0
            level+=1
        while decimal[-1]==chrSet[0]:
                decimal=decimal[:-1]
        e=1
        yCount=0
        while decimal[-e]==chrSet[-1]:
            yCount+=1
            e+=1
        if yCount>3:
            while decimal[-1]==chrSet[-1]:
                decimal=decimal[:-1]
            decimal=decimal.replace(decimal[-1],chrSet[chrSet.index(decimal[-1])+1])
            
        if negative:
            return '-'+integer+'.'+decimal
        else:
            return integer+'.'+decimal

def helper(n, base, chrSet): #Helper for decimalToBaseN()
    return n//base,n%base


def baseNToDecimal(n, base, chrSet = possible):
    """Convert the value of N in base BASE into its decimal equivalent"""
    if '-' in n:
        negative = True
        n=n.replace('-','')
    else:
        negative = False
    if '.' not in n:
        n=n[::-1]
        output = 0
        for place in range(len(n)):
            output+=chrSet.index(n[place])*base**place
        if negative:
            return -output
        else:
            return output
    else:
        integer=baseNToDecimal(n[:n.index('.')], base, chrSet)
        decimal=0
        n = n[n.index('.')+1:]
        for place in range(len(n)):
            decimal+=chrSet.index(n[place])*base**(-place-1)
        if negative:
            return -(integer+decimal)
        else:
            return integer+decimal


def fractions(base, chrSet = possible):
    """Print all fractions in the form 1/x up to x = BASE"""
    for e in range(base):
        print(BaseN(1, base, chrSet)/BaseN((e+1), base, chrSet),\
              '1/{}'.format(e+1))
        
def fractionsTo(start, limit):
    """Execute fractions() for every base from START to LIMIT"""
    for e in range(start, limit+1):
        print('base',e)
        fractions(e, possible[:e])
        print()


def compareBases(largest, number):
    """Convert a NUMBER in every base up to LARGEST"""
    print(number, 'in every base up to base', largest)
    print('Base 1: ',end = '')
    if number%1 == 0:
        for e in range(int(number)):
            print('1', end = '')
        print()
    else:
        print('N/A')
    for e in range(largest-1):
        base = e+2
        chrSet=possible[:base]
        print('Base {}: {}'.format(base,decimalToBaseN(number, base, chrSet)))

def convertBases(value, base1, base2 = 10):
    """Convert a VALUE in BASE1 to the equivalant in BASE2"""
    value = str(value)
    print(value, 'in base', base1, 'is equal to', \
            decimalToBaseN(baseNToDecimal(value, base1, possible[:base1]),base2,possible[:base2]),\
            'in base',base2)
    return decimalToBaseN(baseNToDecimal(value, base1, possible[:base1]),base2,possible[:base2])


def findInt(base, number): #Helper for findPi()
    chrSet=possible[:math.ceil(base)]
    return decimalToBaseN(number, base, chrSet)
    
def findPi(base,accuracy = 'full'):
    """Approximate Pi in a given BASE"""
    chrSet=possible[:math.ceil(base)]
    pi = math.pi
    approx = str(findInt(base, 3)) + '.'
    if accuracy != 'full':
        for i in range(accuracy):
            approx+='0'
            for e in range(math.ceil(base)):
                approx = list(approx)
                approx[-1] = chrSet[-e-1]
                step = baseNToDecimal(approx,base,chrSet)
                if step <= math.pi:
                    break
    else:
        while baseNToDecimal(approx,base,chrSet) != math.pi:
            approx+='0'
            for e in range(math.ceil(base)):
                approx = list(approx)
                approx[-1] = chrSet[-e-1]
                step = baseNToDecimal(approx,base,chrSet)
                if step <= math.pi:
                    break
            
    return ''.join(approx)

def intPi(fro,to):
    for e in range(fro,to+1):    
        base = e
        chrSet=possible[:base]
        pi=''.join(findPi(base))
        print('{}: {}'.format(base, pi))


        
def findIntValueHelp(base, value): #Helper for findIntValue()
    chrSet=possible[:math.ceil(base)]
    length = 1
    approx = ['0']
    while baseNToDecimal(approx,base,chrSet) < value:
        approx = ['0'] * length
        for e in chrSet:
            approx[0] = e
            if baseNToDecimal(approx,base,chrSet) >= value:
                break
        approx.insert(0,'0')
        length += 1
    approx = approx[1:]
    if baseNToDecimal(approx,base,chrSet) > value and int(approx[0])>1:
        approx[0] = str(int(approx[0])-1)
    if baseNToDecimal(approx,base,chrSet) > value:
        newLength = len(approx)-1
        approx = ['0'] * newLength
        approx[0] = str(math.ceil(base)-1)
    return approx

def findIntValue(base, value): #Helper for findValue()
    chrSet=possible[:math.ceil(base)]
    initial = findIntValueHelp(base, value)
    if initial[0] == '0':
        initial[1] = str(math.ceil(base)-1)
        initial = initial[1:]
    remainder = value - baseNToDecimal(initial,base,chrSet)
    for e in initial:
        cur = initial
        if remainder != 0:
            test = list(initial)
            test[-1] = '1'
            if baseNToDecimal(test,base,chrSet) > value:
                return ''.join(initial)
            try:
                nex = (findIntValueHelp(base, remainder))
            except:
                nex=['0']
            if len(str(cur)) != len(str(nex)):
                test = cur
                if base == int(base):
                    test = BaseN(''.join(test),base)
                    test += 1
                else:
                    if int(test[-1])+1 > base:
                        it = -1
                        try:
                            while int(test[it])+1 > base:
                                it -= 1
                        except:
                            length = len(test)
                            test = ['1']
                            for e in range(length):
                                test.append('0')
                        
                        
                    else:
                        test[-1] = str(int(test[-1])+1)
                if baseNToDecimal(test,base,chrSet) > value:
                    if base == int(base):
                        test = BaseN(test,base)
                        test -= 1
                    else:
                        it = -1
                        while test[it] == '0':
                            it -=1
                        test[it] = str(int(test[it])-1)
                        for e in range(len(test)+it+1,len(test)):
                            test[e] = str(int(test[e])+math.ceil(base)-1)
                        it = 0
                        while test[it] == '0':
                            test = test[1:]                    
                    return ''.join(test)
                cur[-len(nex):]=nex
                initial = cur
            try:
                remainder = value - baseNToDecimal(initial,base,chrSet)
            except:
                return ''.join(initial)
    return ''.join(initial)
    
def findValue(base, value, accuracy = 'full'):
    '''Approximate VALUE in a given BASE for BASE > 1'''
    chrSet=possible[:math.ceil(base)]
    if base <= 1:
        return 'Invalid base'
    if value >= 1:
        approx = findIntValue(base, value)+'.'
    else:
        approx = '0.'
    if accuracy != 'full':
        for i in range(accuracy):
            approx+='0'
            for e in range(math.ceil(base)):
                approx = list(approx)
                approx[-1] = chrSet[-e-1]
                step = baseNToDecimal(approx,base,chrSet)
                if step <= value:
                    break
    else:
        while baseNToDecimal(approx,base,chrSet) != value:
            #print(''.join(approx))
            approx+='0'
            for e in range(math.ceil(base)):
                approx = list(approx)
                approx[-1] = chrSet[-e-1]
                step = baseNToDecimal(approx,base,chrSet)
                if step <= value:
                    break
            
    return ''.join(approx)



#forty2 = BaseN(1965, 62)
#sixty4 = BaseN(64, 62)
#10 approximated in base pi
#print(baseNToDecimal('23.2021120021000000300201212221',math.pi,possible))
#print(baseNToDecimal('100.01022122221121122001111210202',math.pi,possible))
