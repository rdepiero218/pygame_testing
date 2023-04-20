

bricks = []

# for row in range(10):
#     for col in range(10):
#         brick = [col * 10, row * 10]
#         bricks.append(brick)


# print(bricks)
# print(' ')
# print(len(bricks))

# for b in range(50, 800, 200):
#     for row in range(10):
#         for col in range(10):
#             brick = [col*10+b, row * 10, col * 10, row * 10]
#             bricks.append(brick)

# for brick in range(len(bricks)):
#     print(bricks[brick], '\n')

# print(len(bricks))


screen_list = [
    'STATUS',
    'ITEM',
    'DATA',
    'MAP',
    'RADIO'
]

direction = input('Enter a direction L or R: ')
position = input('enter a position: ')
position = int(position)
print('Screen chosen: ', screen_list[position])

new_position = 0

if position >= 0 and position < len(screen_list):
    if direction == 'L':
        if position == 0:
            new_position = 4
            # print('Next screen: ', screen_list[new_position])
        else:
            new_position = int(position - 1)
            # print('Next screen: ', screen_list[new_position])

    if direction == 'R':
        if position == 4:
            new_position = 0
            # print('New screen is: ', screen_list[new_position])
        else:
            new_position = int(position + 1)
            # print('New screen is: ', screen_list[new_position])

    print('Next screen: ', screen_list[new_position])