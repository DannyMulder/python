from pygame import image, transform, display
import os

def ChangeScreen(width, height):
    return display.set_mode((width, height)), width, height

def Borders(transform, screenW, screenH):
    if transform.x < 0: transform.x = 0
    if transform.x + transform.width > screenW: transform.x = screenW - transform.width
    if transform.y < 0: transform.y = 0
    if transform.y + transform.height > screenH: transform.y = screenH - transform.height
    
def IsColliding(t1, t2):
    return (
        t1.x < t2.x + t2.width and
        t1.x + t1.width > t2.x and
        t1.y < t2.y + t2.height and
        t1.y + t1.height > t2.y
    )
    
def CreateTextElement(font, text, anti_aliasing, color):
    return font.render(text, anti_aliasing, color)

def CreatImageElement(path, width, height):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, path)
    _image = image.load(full_path)
    _image = transform.scale(_image, (width, height))
    return _image

def GetCenterOfObject(object1W, object1H, object2W, object2H):
    return (object2W / 2 - object1W / 2, object2H / 2 - object1H / 2)

def PlaceCenteredObject(screen, x, y, width, height, object):
    (X, Y) = GetCenterOfObject(object.get_width(), object.get_height(), width, height)
    x = X if x == None else x
    y = Y if x == None else y
    screen.blit(object, (x, y))