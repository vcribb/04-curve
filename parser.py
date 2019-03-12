from display import *
from matrix import *
from draw import *

ARG_COMMANDS = [ 'line', 'scale', 'move', 'rotate', 'save', 'circle', 'hermite', 'bezier' ]

def parse_file( fname, edges, transform, screen, color ):

    f = open(fname)
    lines = f.readlines()

    c = 0
    while c < len(lines):
        line = lines[c].strip()
        #print ':' + line + ':'

        if line in ARG_COMMANDS:
            c+= 1
            args = lines[c].strip().split(' ')

        if line == 'line':            
            #print 'LINE\t' + str(args)

            add_edge( edges,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), float(args[5]) )

        elif line == 'scale':
            #print 'SCALE\t' + str(args)
            t = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(t, transform)

        elif line == 'move':
            #print 'MOVE\t' + str(args)
            t = make_translate(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(t, transform)

        elif line == 'rotate':
            #print 'ROTATE\t' + str(args)
            theta = float(args[1]) * (math.pi / 180)
            
            if args[0] == 'x':
                t = make_rotX(theta)
            elif args[0] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult(t, transform)
                
        elif line == 'ident':
            ident(transform)

        elif line == 'apply':
            matrix_mult( transform, edges )

        elif line == 'display' or line == 'save':
            clear_screen(screen)
            draw_lines(edges, screen, color)

            if line == 'display':
                display(screen)
            else:
                save_extension(screen, args[0])

        elif line == 'circle':
            add_circle(edges, float(args[0]), float(args[1]), float(args[2]),
                   float(args[3]), 100)
            
        elif line == 'hermite':
            add_curve(edges, float(args[0]), float(args[1]), float(args[2]),
                  float(args[3]), float(args[4]), float(args[5]),
                  float(args[6]), float(args[7]), float(100), 'hermite')
            
        elif line == 'bezier':
            add_curve(edges, float(args[0]), float(args[1]), float(args[2]),
                  float(args[3]), float(args[4]), float(args[5]),
                  float(args[6]), float(args[7]), float(100), 'bezier')
            
        c+= 1
