'''
Find a string
'''

def count_substring(string, sub_strig):
    count = 0
    for i in range(len(string)-len(sub_strig)+1):
        for j in range(len(sub_strig)):
            if string[i+j] != sub_strig[j]:
                break
            if j == len(sub_strig)-1:
                count += 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_strig = input().strip()

    count = count_substring(string, sub_strig)
    print(count)

