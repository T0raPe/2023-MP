import queue as q

def dijkstra():
    coor = coor_queue.get()[1]
    x, y = coor[0], coor[1]
    
    if y<len_y-1 and maze[y+1][x]!='#' and (maze[y+1][x]==0 or maze[y+1][x]>maze[y][x]+1) and (x,y+1) not in path:
        path[(x,y+1)] = [x,y]
        maze[y+1][x] = maze[y][x]+1
        prior = maze[y+1][x]
        coor_queue.put((prior, [x, y+1]))
    if y>0 and maze[y-1][x]!='#' and (x,y-1) not in path and (maze[y-1][x]==0 or maze[y-1][x]>maze[y][x]+1):
        path[(x,y-1)] = [x,y]
        maze[y-1][x] = maze[y][x]+1
        prior = maze[y-1][x]
        coor_queue.put((prior, [x, y-1]))
    if x<len_x-1 and maze[y][x+1]!='#' and (x+1,y) not in path and (maze[y][x+1]==0 or maze[y][x+1]>maze[y][x]+1):
        path[(x+1,y)] = [x,y]
        maze[y][x+1] = maze[y][x]+1
        prior = maze[y][x+1]
        coor_queue.put((prior, [x+1, y]))
    if x>0 and maze[y][x-1]!='#' and (x-1,y) not in path and (maze[y][x-1]==0 or maze[y][x-1]>maze[y][x]+1):
        path[(x-1,y)] = [x,y]
        maze[y][x-1] = maze[y][x]+1
        prior = maze[y][x-1]
        coor_queue.put((prior, [x-1, y]))
        
    return (x, y)

def a():
    coor = coor_q.get()[1]
    x, y = coor[0], coor[1]
    if y<len_y-1 and maze[y+1][x]!='#' and (maze[y+1][x]==0 or maze[y+1][x]>maze[y][x]+1) and (x,y+1) not in path:
        path[(x,y+1)] = [x,y]
        maze[y+1][x] = maze[y][x]+1
        prior = maze[y+1][x]+(abs(end_x-x)+abs(end_y-(y+1)))
        coor_q.put((prior, [x, y+1]))
    if y>0 and maze[y-1][x]!='#' and (x,y-1) not in path and (maze[y-1][x]==0 or maze[y-1][x]>maze[y][x]+1):
        path[(x,y-1)] = [x,y]
        maze[y-1][x] = maze[y][x]+1
        prior = maze[y-1][x]+(abs(end_x-x)+abs(end_y-(y-1)))
        coor_q.put((prior, [x, y-1]))
    if x<len_x-1 and maze[y][x+1]!='#' and (x+1,y) not in path and (maze[y][x+1]==0 or maze[y][x+1]>maze[y][x]+1):
        path[(x+1,y)] = [x,y]
        maze[y][x+1] = maze[y][x]+1
        prior = maze[y][x+1]+(abs(end_x-(x+1))+abs(end_y-y))
        coor_q.put((prior, [x+1, y]))
    if x>0 and maze[y][x-1]!='#' and (x-1,y) not in path and (maze[y][x-1]==0 or maze[y][x-1]>maze[y][x]+1):
        path[(x-1,y)] = [x,y]
        maze[y][x-1] = maze[y][x]+1
        prior = maze[y][x-1]+(abs(end_x-(x-1))+abs(end_y-y))
        coor_q.put((prior, [x-1, y]))
        
    return (x, y)

with open ("maze-for-u.txt") as file:
    maze_read = file.read().splitlines()
len_x = len(maze_read[0])
len_y = len(maze_read)
maze = [['#' if line[i]=='#' else 0 for i in range (len_x)] for line in maze_read]
maze_w = [['#' if line[i]=='#' else ' ' for i in range (len_x)] for line in maze_read]
start_x, start_y = 1, 0
path = {(start_x,start_y): None}
coor_queue = q.PriorityQueue()
coor_queue.put((0, [start_x,start_y]))
key = [620,360]

x, y = start_x, start_y
while x!=key[0] or y!=key[1]:
    x, y = dijkstra()

x_p, y_p = key[0], key[1]
while x_p!=start_x or y_p!=start_y:
    x_p, y_p = path[(x_p,y_p)][0], path[(x_p,y_p)][1]
    maze_w[y_p][x_p] = '.'
    
maze = [['#' if line[i]=='#' else 0 for i in range (len_x)] for line in maze_read]
start_x, start_y = key[0], key[1]
path = {(start_x,start_y): None}
coor_q = q.PriorityQueue()
coor_q.put((0, [start_x, start_y]))
end_x, end_y = 797, 599

x, y = start_x, start_y
while x!=end_x or y!=end_y:
    x, y = a()

x_p, y_p = end_x, end_y
while x_p!=start_x or y_p!=start_y:
    x_p, y_p = path[(x_p,y_p)][0], path[(x_p,y_p)][1]
    maze_w[y_p][x_p] = ','
maze_w[key[1]][key[0]] = '*'
maze_w[end_y][end_x] = ','

with open('maze-for-me-done.txt', 'w') as file:
    for line in maze_w:
        for i in range (len_x):
            file.write(line[i])
        file.write('\n')
        