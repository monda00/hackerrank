'''
Designer Door Mat
'''

def show_designer_mat(n, m):
    pattern_top = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
    print('\n'.join(pattern_top))
    pattern_center = ['WELCOME'.center(m, '-')]
    print('\n'.join(pattern_center))
    pattern_bottom = reversed(pattern_top)
    print('\n'.join(pattern_bottom))

if __name__ == '__main__':
    n, m = map(int, input().split())

    show_designer_mat(n, m)

