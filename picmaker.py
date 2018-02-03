width = 500
height = 500

def draw(file):
    b = 255
    for y in range(height):
        line = ""
        r = g = 255 * y / height
        for x in range(width):
            line += "%d %d %d " % (r,g,b)
        file.write(line + "\n")

def main():
    file = open("image.ppm","w+")
    file.write("P3\n")
    file.write("%d %d\n" % (width, height))
    file.write("255\n")
    draw(file)

main()
