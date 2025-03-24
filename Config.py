import glfw, ctypes , pyrr #, numba
import imgui as im
import OpenGL.GL as gl
import numpy as np
import glfw.GLFW as GLFW_CONSTANT
from OpenGL.GL.shaders import compileProgram, compileShader
from imgui.integrations.glfw import GlfwRenderer

SCALE = 0.75
WIN_SIZEX = int(1280 * SCALE)
WIN_SIZEY = int(1024 * SCALE)


data_type_vertex = np.dtype({
    "names" : ["x", "y", "z", "colour"],
    "formats" : [np.float32, np.float32, np.float32, np.uint32],
    "offsets" : [0, 4, 8, 12],
    "itemsize" : 16
}
                             )


def shader_program(v_filepath, f_filepath):
    return compileProgram(compileShader(open(v_filepath).read(),
                                        gl.GL_VERTEX_SHADER),
                          compileShader(open(f_filepath).read(),
                                        gl.GL_FRAGMENT_SHADER))