'''
Zipped!
'''

if __name__ == '__main__':
    num_student, num_sub = map(int, input().split())

    exam_list = []
    for _ in range(num_sub):
        exam_list.append(list(map(float, input().split())))

    for exam_result in zip(*exam_list):
        print(sum(exam_result) / num_sub)

