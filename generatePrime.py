import sys
import math
def isfoo(num, prime):
        sqt =int(math.sqrt(num))+1
        for i in prime:
            if(i<=sqt):
                if (num // i * i == num): return 0
        return 1
def answer(n):
        LEN = 5
        minion = "23";
        i = 5;
        nn = int(n)
        prime = [3]
        while ( 1 ):
                if ( isfoo(i,prime) == 1):
                        prime.append(i)
                        minion += str(i)
                        if (len(minion)>nn+LEN):
                                return minion[nn:nn+LEN]
                                break
                i+=2
def main():
        print("minion["+sys.argv[1]+"]="+answer(sys.argv[1]))
if __name__ == "__main__":
    main()