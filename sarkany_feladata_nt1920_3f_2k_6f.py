with open('input_nt1920_3ford_2kat_6fel', 'r') as file:
    lines = file.readlines()

a1, b1, n1 = map(int, lines[0].split())
a2, b2, n2 = map(int, lines[1].split())
a3, b3, n3 = map(int, lines[2].split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a,b):
    return a*b//gcd(a,b)

def count_digits(n):
    return len(str(abs(n)))

def process_digits(d, n):
    digit_count = count_digits(d)

    if digit_count > n:
        return -1
    elif digit_count == n:
        return str(d)
    else:
        # Append (n - digit_count) zeros to d
        zeros_to_append = '0' * (n - digit_count)
        return str(d) + zeros_to_append

print(process_digits(lcm(a1,b1),n1))
print(process_digits(lcm(a2,b2),n2))
print(process_digits(lcm(a3,b3),n3))