'''
Mutations
'''

def mutate_string(string, position, character):
    mutate_str = string[:position] + character + string[position+1:]
    return mutate_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

