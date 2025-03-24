from Config import glfw,pyrr,np

class Object:
    def __init__(self, pos,mesh_func = None):
        self.position = pos
        self.eulers = [0, 0, 0]
        self.ebo, self.vbo, self.vao = mesh_func
        self.SCALE = 0.5

    def transform(self):
        model_transform = pyrr.matrix44.create_identity(dtype=np.float32)
        model_transform = pyrr.matrix44.multiply(
            m1=model_transform,
            m2=pyrr.matrix44.create_from_eulers(
                eulers=np.radians(self.eulers),
                dtype=np.float32))

        model_transform = pyrr.matrix44.multiply(
            m1=model_transform,
            m2=pyrr.matrix44.create_from_translation(
                vec=self.position,
                dtype=np.float32))

        return model_transform

    def rotationKEYS(self,window,SPEED = 1.5):
        if (glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS):
            self.rotationUP(SPEED)
        if (glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS):
            self.rotationDOWN(SPEED)
        if (glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS):
            self.rotationRIGHT(SPEED)
        if (glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS):
            self.rotationLEFT(SPEED)

    def rotation(self,SPEED):
        self.rotationUP(SPEED)
        self.rotationLEFT(SPEED)
        self.rotationDOWN(SPEED)
        self.rotationRIGHT(SPEED)

    def rotationUP(self,SPEED):
        self.eulers[0] += SPEED
        if self.eulers[0] > 360:
            self.eulers[0] -= 360
    def rotationDOWN(self,SPEED):
        self.eulers[0] -= SPEED
        if self.eulers[0] < 0:
            self.eulers[0] += 360
    def rotationRIGHT(self,SPEED):
        self.eulers[2] -= SPEED
        if self.eulers[2] < 0:
            self.eulers[2] += 360
    def rotationLEFT(self,SPEED):
        self.eulers[2] += SPEED
        if self.eulers[2] > 360:
            self.eulers[2] -= 360

    def rotationACW(self,SPEED):
        self.eulers[1] -= SPEED
        if self.eulers[1] > 360:
            self.eulers[1] -= 360

    def rotationCW(self,SPEED):
        self.eulers[1] += SPEED
        if self.eulers[1] > 360:
            self.eulers[1] -= 360

    def movementKEYS(self,window):
        if (glfw.get_key(window, glfw.KEY_W) == glfw.PRESS):
            self.moveforwards()
        if (glfw.get_key(window, glfw.KEY_S) == glfw.PRESS):
            self.movebackwards()
        if (glfw.get_key(window, glfw.KEY_A) == glfw.PRESS):
            self.moveleft()
        if (glfw.get_key(window, glfw.KEY_D) == glfw.PRESS):
            self.moveright()
        if (glfw.get_key(window, glfw.KEY_E) == glfw.PRESS):
            self.moveup()
        if (glfw.get_key(window, glfw.KEY_Q) == glfw.PRESS):
            self.movedown()
    def moveforwards(self):
        self.position[2] += 0.03
        # if self.position[2] >= 0:
        #     self.position[2] = 0
    def movebackwards(self):
        self.position[2] -= 0.03
        # if self.position[2] <= -8:
        #     self.position[2] = -8
    def moveleft(self):
        self.position[0] -= 0.03
        # if self.position[0] <= -3:
        #     self.position[0] = -3
    def moveright(self):
        self.position[0] += 0.03
        # if self.position[0] >= 3:
        #     self.position[0] = 3
    def moveup(self):
        self.position[1] += 0.03
        # if self.position[1] >= 3:
        #     self.position[1] = 3
    def movedown(self):
        self.position[1] -= 0.03
        # if self.position[1] <= -3:
        #     self.position[1] = -3