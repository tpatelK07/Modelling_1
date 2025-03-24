from Mesh import *
from Objects import Object
from Toolbars import Toolbar
class App:

    def __init__(self):
        self.numFrames = 0
        self.lastTime = 0
        self.init_glfw()
        self.initOpengl()
        self.Ui= Toolbar(self.window)
        self.cube = Object([0,0,0],cube())
        self.pyramid = Object([5,5,5],pyramid())
        self.mainloop()


    def initOpengl(self):
        gl.glClearColor(0.3, 0.3, 0.3, 1)
        gl.glEnable(gl.GL_DEPTH_TEST)
        # self.triangle_vbo, self.triangle_vao = triangle()
        # self.quad_ebo, self.quad_vbo, self.quad_vao  = quad()
        self.shader = shader_program("shaders/Vertex", "shaders/fragment")
        gl.glUseProgram(self.shader)

        #Allow transformations
        projection_transformations = pyrr.matrix44.create_perspective_projection(
            fovy=60, aspect=640 / 480,
            near=0.1, far=100, dtype=np.float32)
        gl.glUniformMatrix4fv(
            gl.glGetUniformLocation(self.shader, "projection"),
            1, gl.GL_FALSE, projection_transformations)
        self.modelMatrixLocation = gl.glGetUniformLocation(self.shader, "model")

    def init_glfw(self):
        glfw.init()
        # core_profile sets modern openGL
        glfw.window_hint(GLFW_CONSTANT.GLFW_OPENGL_PROFILE, GLFW_CONSTANT.GLFW_OPENGL_CORE_PROFILE)
        # Choose modern OpenGL version 3.3
        glfw.window_hint(GLFW_CONSTANT.GLFW_CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(GLFW_CONSTANT.GLFW_CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(GLFW_CONSTANT.GLFW_RESIZABLE, gl.GL_FALSE)
        # ONLY NEEDED TO RUN ON MAC_OS
        glfw.window_hint(GLFW_CONSTANT.GLFW_OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

        self.window = glfw.create_window(WIN_SIZEX,WIN_SIZEY, "Prototype", None, None)
        glfw.make_context_current(self.window)

    def mainloop(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()

            gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
            gl.glUseProgram(self.shader)

            self.cube.rotationKEYS(self.window)
            self.cube.movementKEYS(self.window)
            gl.glUniformMatrix4fv(self.modelMatrixLocation, 1, gl.GL_FALSE, self.cube.transform())

            gl.glBindVertexArray(self.cube.vao)
            gl.glDrawElements(gl.GL_TRIANGLES, 36, gl.GL_UNSIGNED_BYTE, ctypes.c_void_p(0))
            self.Ui.toolbar1(self.cube)

            # gl.glBindVertexArray()
            # gl.glDrawElements(gl.GL_SPHERE_MAP,1,gl.GL_UNSIGNED_BYTE,ctypes.c_void_p(0))

            # self.pyramid.rotationKEYS(self.window)
            # self.pyramid.movementKEYS(self.window)
            # gl.glUniformMatrix4fv(self.modelMatrixLocation, 1, gl.GL_FALSE, self.pyramid.transform())

            gl.glBindVertexArray(self.pyramid.vao)
            gl.glDrawElements(gl.GL_TRIANGLES, 12, gl.GL_UNSIGNED_BYTE, ctypes.c_void_p(0))
            # self.Ui.toolbar1(self.pyramid)


            self.framerate()

            glfw.swap_buffers(self.window)
            glfw.swap_interval(1)

        self.quit()

    def quit(self):
        gl.glDeleteBuffers(2, (self.cube.vbo,self.cube.ebo,self.pyramid.vbo,self.pyramid.ebo))
        gl.glDeleteVertexArrays(1, (self.cube.vao,self.pyramid.vao,))
        gl.glDeleteProgram(self.shader)
        glfw.destroy_window(self.window)
        glfw.terminate()

    def framerate(self):
        self.numFrames += 1
        self.currentTime = glfw.get_time()
        delta = self.currentTime - self.lastTime
        if self.numFrames == 5:
            frameRate = int(5 /delta)
            glfw.set_window_title(self.window, "Prototype - " + str(frameRate) + " fps")
            self.lastTime = self.currentTime
            self.numFrames = 0

class Material:
    def __init__(self):
        pass

if __name__ == "__main__":
    app = App()