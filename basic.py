

bricks = []

# for row in range(10):
#     for col in range(10):
#         brick = [col * 10, row * 10]
#         bricks.append(brick)


# print(bricks)
# print(' ')
# print(len(bricks))

for b in range(50, 800, 200):
    for row in range(10):
        for col in range(10):
            brick = [col*10+b, row * 10, col * 10, row * 10]
            bricks.append(brick)

for brick in range(len(bricks)):
    print(bricks[brick], '\n')

print(len(bricks))