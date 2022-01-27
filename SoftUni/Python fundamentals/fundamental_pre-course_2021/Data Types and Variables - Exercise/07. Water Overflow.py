lines_num = int(input())
pipe_line = 0
for _ in range(lines_num):
    pipe_line1 = int(input())
    if pipe_line + pipe_line1 > 255:
        print('Insufficient capacity!')
    else:
        pipe_line += pipe_line1
print(pipe_line)
