class Vector():
    """
    Klasa reprezentująca wektor.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def add(self,x,y,z):
        """
        Metoda add
        """
        self.x += x
        self.y += y
        self.z += z
