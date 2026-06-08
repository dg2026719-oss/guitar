Web VPython 3.2

cylinder(pos = vec(0,0,0), opacity = 1, size = vec(10,25,29), color = vector(0.82, 0.68, 0.45))
cylinder(pos = vec(0,15.7,0), opacity = 1, size = vec(10,16,21), color = vector(0.82, 0.68, 0.45))
cylinder(pos = vec(-0.1,11,0), opacity = 1, size = vec(8.3,8.3,8.3), color = color.black)
box(pos = vec(0.5,29,0), opacity = 1, size = vec(2,29,5), color = vector(0.17,0.15,0.14))
box(pos = vec(0.2, 0.8, 0), opacity = 1, size = vec(1,0.3,5), color = vector(0.9,0.77,0.58))
box(pos = vec(0.3, 0.5, 0), opacity = 1, size = vec(1,2.1,9.5), color = vector(0.16,0.14,0.13))
sphere(pos = vec(-0.3, 0.1, -1.8), opacity = 1, size = vec(0.4,0.4,0.4), color = vector(0.99,0.96,0.9))
sphere(pos = vec(-0.3, 0.1, 1.8), opacity = 1, size = vec(0.4,0.4,0.4), color = vector(0.99,0.96,0.9))
sphere(pos = vec(-0.3, 0.1, 0.35), opacity = 1, size = vec(0.4,0.4,0.4), color = vector(0.99,0.96,0.9))
sphere(pos = vec(-0.3, 0.1, -0.35), opacity = 1, size = vec(0.4,0.4,0.4), color = vector(0.99,0.96,0.9))
sphere(pos = vec(-0.3, 0.1, 1.1), opacity = 1, size = vec(0.4,0.4,0.4), color = vector(0.99,0.96,0.9))
sphere(pos = vec(-0.3, 0.1, -1.1), opacity = 1, size = vec(0.4,0.4,0.4), color = vector(0.99,0.96,0.9))
b = cylinder(pos = vec(-0.5,0,1.8), opacity = 1, size = vec(42,0.1,0.15), axis = vec(0,30,0))
a = cylinder(pos = vec(-0.5,0,-1.8), opacity = 1, size = vec(42,0.1,0.15), axis = vec(0,30,0), color = vector(0.92,0.76,0.53))
c = cylinder(pos = vec(-0.5,0,0.35), opacity = 1, size = vec(42,0.1,0.15), axis = vec(0,30,0))
d = cylinder(pos = vec(-0.5,0,-0.35), opacity = 1, size = vec(42,0.1,0.15), color = vector(0.92,0.76,0.53), axis = vec(0,30,0))
e = cylinder(pos = vec(-0.5,0,1.1), opacity = 1, size = vec(42,0.1,0.15), color = vector(0.9,0.9,0.9), axis = vec(0,30,0))
f = cylinder(pos = vec(-0.5,0,-1.1), opacity = 1, size = vec(42,0.1,0.15), color = vector(0.92,0.76,0.53), axis = vec(0,30,0))
box(pos = vec(0.55,47.5,0), opacity = 1, size = vec(2,8,6), color = vector(0.34,0.22,0.14))
cylinder(pos = vec(-1.3,50,1.7), opacity = 1, size = vec(2,0.9,0.9), color = vector(0.74,0.76,0.78))
cylinder(pos = vec(-1.3,50,-1.7), opacity = 1, size = vec(2,0.9,0.9), color = vector(0.74,0.76,0.78))
cylinder(pos = vec(-1.3,47.65,1.7), opacity = 1, size = vec(2,0.9,0.9), color = vector(0.74,0.76,0.78))
cylinder(pos = vec(-1.3,47.65,-1.7), opacity = 1, size = vec(2,0.9,0.9), color = vector(0.74,0.76,0.78))
cylinder(pos = vec(-1.3,45.5,1.7), opacity = 1, size = vec(2,0.9,0.9), color = vector(0.74,0.76,0.78))
cylinder(pos = vec(-1.3,45.5,-1.7), opacity = 1, size = vec(2,0.9,0.9), color = vector(0.74,0.76,0.78))
strings = [a, f, d, c, e, b]
while True:
    rate(100)
    k = keysdown()

    if '1' in k:
        strings[0].color = color.red
    else:
        strings[0].color = vector(0.92,0.76,0.53)

    if '2' in k:
        strings[1].color = color.orange
    else:
        strings[1].color = vector(0.92,0.76,0.53)

    if '3' in k:
        strings[2].color = color.yellow
    else:
        strings[2].color = vector(0.92,0.76,0.53)

    if '4' in k:
        strings[3].color = color.green
    else:
        strings[3].color = vector(0.92,0.76,0.53)

    if '5' in k:
        strings[4].color = color.blue
    else:
        strings[4].color = vector(0.9,0.9,0.9)

    if '6' in k:
        strings[5].color = color.black
    else:
        strings[5].color = vector(0.9,0.9,0.9)
        
        
