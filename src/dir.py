class Dir:

    (right, down, left, top) = range(4)

    def opposite(dir):
        return (dir+2)%4

