width = 500
height = 500

def main():
    file = open("image.ppm","w+")
    file.write("P3\n")
    file.write(str(width) + " " + str(height) + "\n")
    file.write("255\n")
    draw(file)

def draw(file):
    b = 225
    for y in range(height):
        line = ""
        r = g = 255 * y / height
        for x in range(width):
            line += str(r) + " " + str(g) + " " + str(b) + "  "
        file.write(line + "\n")

main()
