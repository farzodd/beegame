import numpy

rotate_x = numpy.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
rotate_y = numpy.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
rotate_z = numpy.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
zero_matrix = numpy.zeros((3, 3), int)
ones_matrix = numpy.ones((3, 3), int)
value_r = 1
value_u = 1
value_y = 2


def main():
    tiles = [
        ('R', 'RR'),
        ('R', 'U'),
        ('U', 'UU'),
        ('U', 'R'),
        ('RR', 'RUU'),
        ('RR', 'Y'),
        ('RR', 'RRR'),
        ('UU', 'RRU'),
        ('UU', 'Y'),
        ('UU', 'UUU'),
        ('RU', 'YY'),
        ('Y', 'RRU'),
        ('Y', 'RUU'),
        ('Y', 'RRR'),
        ('Y', 'UUU'),
        ('YY', 'RRRUUU'),
        ('RRR', 'YYU'),
        ('RRR', 'YYRR'),
        ('UUU', 'YYR'),
        ('UUU', 'YYUU'),
        ('RRU', 'YUU'),
        ('RRU', 'YRU'),
        ('RUU', 'YRR'),
        ('RUU', 'YRU'),
        ('YRU', 'YYYY'),
        ('RRUU', 'YYYY')
    ]
    tile_values = []
    num_each_value = [0, 0, 0, 0, 0]
    counter = 0

    print('Value Calculations')
    print('Input\tOutput\tValue Added')
    for tile in tiles:
        value_before = (tile[0].count('R') * value_r) + (tile[0].count('U') * value_u) + (tile[0].count('Y') * value_y)
        value_after = (tile[1].count('R') * value_r) + (tile[1].count('U') * value_u) + (tile[1].count('Y') * value_y)
        value_added = value_after-value_before
        print('{:<5}'.format(tile[0]) + '\t' + '{:<5}'.format(tile[1]) + '\t' + str(value_added))
        tile_values.append((tile, value_added))
        num_each_value[value_added] += 1

    print('\nOverall Stats')
    print('Value' + '\t' + 'Count')
    for value in num_each_value:
        print('{:<5}'.format(str(counter)) + '\t' + str(value))
        counter += 1
    percent_0 = 15
    percent_1 = 35
    percent_2 = 30
    percent_3 = 15
    percent_4 = 5



if __name__ == "__main__":
    main()
