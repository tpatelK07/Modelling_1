from Config import im , WIN_SIZEY, WIN_SIZEX , GlfwRenderer
class Toolbar:
    def __init__(self,window):
        im.create_context()
        self.io = im.get_io()
        self.io.display_size = im.Vec2(WIN_SIZEX, WIN_SIZEY)
        self.renderer = GlfwRenderer(window)

    def toolbar1(self,object):
        self.renderer.process_inputs()
        im.new_frame()
        XSIZE = WIN_SIZEX/3
        xPos = 0
        # with im.begin("Transformaton UI", False,
        #               flags = im.WINDOW_NO_RESIZE|
        #                         im.WINDOW_NO_MOVE|
        #                         im.WINDOW_NO_COLLAPSE|
        #               im.WINDOW_NO_FOCUS_ON_APPEARING):
        #
        #     im.set_window_size(WIN_SIZEX,(WIN_SIZEY/6))
        #     YPOS = WIN_SIZEY - im.get_window_size().y - 20
        #     xPos = 0
        #     im.set_window_position(xPos,YPOS)
        #     xPos += im.get_window_size().x

        with im.begin("PITCH", False,
                      flags = im.WINDOW_NO_RESIZE|
                                im.WINDOW_NO_MOVE|
                                im.WINDOW_NO_COLLAPSE):
            im.set_window_size(XSIZE, WIN_SIZEY / 6)
            YPOS = WIN_SIZEY- im.get_window_size().y
            im.set_window_position(xPos, YPOS)
            xPos += im.get_window_size().x

            im.button("Rotate UP")
            if im.is_item_active():
                object.rotationUP(1.5)
            im.button("Rotate DOWN")
            if im.is_item_active():
                object.rotationDOWN(1.5)

        with im.begin("YAW", False,
                      flags = im.WINDOW_NO_RESIZE|
                                im.WINDOW_NO_MOVE|
                                im.WINDOW_NO_COLLAPSE):
            im.set_window_size(XSIZE, WIN_SIZEY / 6)
            im.set_window_position(xPos, YPOS)

            xPos += im.get_window_size().x

            im.button("Rotate RIGHT")
            if im.is_item_active():
                object.rotationRIGHT(1.5)
            im.button("Rotate LEFT")
            if im.is_item_active():
                object.rotationLEFT(1.5)

        with im.begin("ROLL", False,
                      flags = im.WINDOW_NO_RESIZE|
                                im.WINDOW_NO_MOVE|
                                im.WINDOW_NO_COLLAPSE):
            im.set_window_size(XSIZE, WIN_SIZEY / 6)

            im.set_window_position(xPos, YPOS)


            im.text("ROLL")
            im.button("Rotate Clockwise")
            if im.is_item_active():
                object.rotationCW(1.5)
            im.button("Rotate Anti-Clockwise")
            if im.is_item_active():
                object.rotationACW(1.5)

        im.render()
        if im.get_draw_data():
            self.renderer.render(im.get_draw_data())
        im.end_frame()