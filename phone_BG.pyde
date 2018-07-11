def setup():
    size(600,800)
    background(random (0),random (0), random (0))
    img = loadImage ("yin_yang.png")
    x = 0
    while x < 600:
        y = 0
        while y < 800:
            image(img,x,y,100,100)
            y = y + 100
        x = x +100
