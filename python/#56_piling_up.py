'''
Piling Up!
'''

if __name__ == '__main__':
    for _ in range(int(input())):
        input()
        cubes = list(map(int, input().split()))

        min_cube = cubes.index(min(cubes))
        left_cubes = cubes[:min_cube]
        right_cubes = cubes[min_cube:]

        if(left_cubes == sorted(left_cubes, reverse=True) and
           right_cubes == sorted(right_cubes)):
            print("Yes")
        else:
            print("No")

