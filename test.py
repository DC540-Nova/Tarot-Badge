    def block(self, x0, y0, x1, y1, data):
        """
        Method to write a block of data to display.

        Params:
            x0: int
            y0: int
            x1: int
            y1: int
            data: bytes
        """
        self.write_cmd(self.SET_COLUMN, *ustruct.pack('>HH', x0, x1))
        self.write_cmd(self.SET_PAGE, *ustruct.pack('>HH', y0, y1))
        self.write_cmd(self.WRITE_RAM)
        self.write_data(data)
         
         
    def draw_image(self, path, x=0, y=0, w=240, h=320):
        """
        Method to draw image on screen from flash or sd card

        Params:
            path: str
            x: int, optional
            y: int, optional
            w: int, optional
            h: int, optional
            draw_speed: int, optional
        """
        import framebuf
        x2 = x + w - 1
        y2 = y + h - 1
        if self.is_off_grid(x, y, x2, y2):
            return
        buf = bytearray(240*320*2)  # 153600 total byte array of an image
        with open(path, 'rb') as f:
            bytes_read = f.readinto(buf)
            #gc.collect()
        fb = framebuf.FrameBuffer(buf, 240, 320, framebuf.RGB565)
        self.block(x, y, x2, y2, fb)
   
   
0 File "ili9341.py", line 356, in draw_image
MemoryError: memory allocation failed, allocating 153600 bytes
