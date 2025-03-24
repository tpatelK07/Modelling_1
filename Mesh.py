from Config import *

def stan_vao_comfig(vertex_data):
    vao = gl.glGenVertexArrays(1)
    gl.glBindVertexArray(vao)

    vbo = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vbo)
    gl.glBufferData(gl.GL_ARRAY_BUFFER, vertex_data.nbytes,
                    vertex_data, gl.GL_STATIC_DRAW)

    gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, data_type_vertex.itemsize, ctypes.c_void_p(0))
    gl.glEnableVertexAttribArray(0)

    gl.glVertexAttribIPointer(1, 1, gl.GL_UNSIGNED_INT, data_type_vertex.itemsize, ctypes.c_void_p(12))
    gl.glEnableVertexAttribArray(1)
    return (vbo, vao)

def triangle():

    vertex_data = np.zeros(3,dtype= data_type_vertex)
    vertex_data[0] = (-0.75, -0.75, 0.0, 0)
    vertex_data[1] = (0.75, -0.75, 0.0, 1)
    vertex_data[2] = (0.0, 0.75, 0.0, 2)

    vbo, vao = stan_vao_comfig(vertex_data)

    return (vbo, vao)

def quad():

    vertex_data = np.zeros(4,dtype= data_type_vertex)
    vertex_data[0] = (-0.75, -0.75, -0.1, 2)
    vertex_data[1] = (0.75, -0.75, -0.1, 0)
    vertex_data[2] = (0.75, 0.75, -0.1, 1)
    vertex_data[3] = (-0.75, 0.75, -0.1, 2)

    index_data = np.array([0,1,2,3,2,0],dtype=np.ubyte)

    vbo, vao = stan_vao_comfig(vertex_data)

    ebo = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, ebo)
    gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, index_data.nbytes, index_data, gl.GL_STATIC_DRAW)

    return (ebo, vbo, vao)

def pyramid():
    vertex_data = np.zeros(4, dtype=data_type_vertex)
    vertex_data[0] = (-1, -1, 0, 0)
    vertex_data[1] = (1, -1, 0, 2)
    vertex_data[2] = (0, -1, 1.5, 4)
    vertex_data[3] = (0, 0.41, 0.67, 6)

    index_data = np.array([0,1,2,
                           0,1,2,
                           0,2,3,
                           1,2,3
                           ], dtype=np.ubyte)

    vbo, vao = stan_vao_comfig(vertex_data)

    ebo = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, ebo)
    gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, index_data.nbytes, index_data, gl.GL_STATIC_DRAW)

    return (ebo, vbo, vao)

def cube():
    vertex_data = np.zeros(8,dtype= data_type_vertex)
    vertex_data[0] = (-1, -1, -1, 0)
    vertex_data[1] = (1, -1, -1, 1)
    vertex_data[2] = (1, 1, -1, 2)
    vertex_data[3] = (-1, 1, -1, 3)
    vertex_data[4] = (-1, -1, 1, 4)
    vertex_data[5] = (1, -1, 1, 5)
    vertex_data[6] = (1, 1, 1, 6)
    vertex_data[7] = (-1, 1, 1, 7)

    index_data = np.array([ 0,1,2,2,3,0,
                            4,5,6,6,7,4,
                            1,5,6,6,2,1,
                            0,4,7,7,3,0,
                            0,1,5,5,4,0,
                            3,2,6,6,7,3,
                           ], dtype=np.ubyte)

    vbo, vao = stan_vao_comfig(vertex_data)

    ebo = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, ebo)
    gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, index_data.nbytes, index_data, gl.GL_STATIC_DRAW)

    return (ebo, vbo, vao)


def sphere():

    pass
