from pygame import image, transform, display, Surface, font
import os

def Error(message):
    raise ValueError(message)

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
    
def CreateTextElement(font: font, text: str, anti_aliasing: bool, color: tuple[int, int, int]):
    """Creates a text element"""
    return font.render(text, anti_aliasing, color)

def CreatImageElement(path: str, width: int, height: int):
    """Creates an image element"""
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, path)
    _image = image.load(full_path)
    _image = transform.scale(_image, (width, height))
    return _image

def GetCenterOfObject(object1W, object1H, object2W, object2H):
    return (object2W / 2 - object1W / 2, object2H / 2 - object1H / 2)

def PlaceSurfaceObject(screen: Surface,
                        x: int | None,
                        y: int | None,
                        childobject: Surface,
                        parentObject: tuple[int, int, int, int],
                        absolute: bool):
    """
    Places a surface (text, image) on given screen
    
    Logic:
        If x/y is provided and absolute=False → start on given Axis position
        If x/y is provided and absolute=True → use parent Axis as start point + given Axis position
        If x/y is not provided and absolute=True → use parentX/Y + centerX/Y
        If both x/y and absolute are not provided this will result in an ERROR
    
    """
    
    (pX, pY, pWidth, pHeight) = parentObject
    (cX, cY) = GetCenterOfObject(childobject.get_width(), childobject.get_height(), pWidth, pHeight)

    if x is not None:
        startX = x if not absolute else pX + x
    else:
        if not absolute:
            Error("Requirements not met! Please give required params: x or absolute")
        startX = pX + cX

    if y is not None:
        startY = y if not absolute else pY + y
    else:
        if not absolute:
            Error("Requirements not met! Please give required params: y or absolute")
        startY = pY + cY

    screen.blit(childobject, (startX, startY))
