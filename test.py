   def draw_image(self, path, x=0, y=0, w=240, h=320, draw_speed=26375):
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
        with open(path, 'rb') as f:
            chunk_height = draw_speed // w  # 153600 total bytes of an image
            #chunk_count, remainder = divmod(h, chunk_height)
            chunk_size = chunk_height * w * 2
            chunk_y = y
            #buf = bytes(0)
      #      if chunk_count:
   #             for _ in range(0, chunk_count):
   #                 gc.collect()
            buf = f.read(chunk_size)
                    #self.block(x, chunk_y, x2, chunk_y + chunk_height - 1, buf)
   #                 chunk_y += chunk_height
            #if remainder:
             #   gc.collect()
            #    buf += f.read(remainder * w * 2)
                #self.block(x, chunk_y, x2, chunk_y + remainder - 1, buf)
            buf = framebuf.FrameBuffer(bytearray(buf), w, h, framebuf.RGB565)
            self.block(x, chunk_y, x2, chunk_y + chunk_height - 1, buf)

            
            
            
            
 
def write_bin(f, pixel_list):
    """
    Method to save image in RGB565 format
    
    Params:
        f: object
        pixel_list: list
    """
    for pix in pixel_list:
        r = (pix[0] >> 3) & 0x1F
        g = (pix[1] >> 2) & 0x3F
        b = (pix[2] >> 3) & 0x1F
        f.write(pack('>H', (r << 11) + (g << 5) + b))
