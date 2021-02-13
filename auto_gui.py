#! python3

import pyautogui, os

class Auto_gui ():
    """
    Automate kyboard and mouse, reading specific pixles of the screen
    """

    def __init__ (self): 
        """
        Constructor of class
        """

        x_initial = 832
        y_initial = 752

        x_final = 833
        y_final = 792

        h_min = 47
        h_max = 51
        
        skip_pixels = 2

        print ('Waiting "e" button')

        # Infinite llop for found pixel
        while True: 

            # Loop for "Y" range of pixels
            for y in range(int(y_initial), int(y_final), skip_pixels): 

                # Loop for "X" range of pixels
                for x in range (int(x_initial), int(x_final), skip_pixels):
                    im = pyautogui.screenshot()
                    pixel = im.getpixel((x, y))
                    pixel_r = pixel[0]
                    pixel_g = pixel[1]
                    pixel_b = pixel[2]
                    pixel_hsv = self.__rgb_to_hsv(pixel_r, pixel_g, pixel_b)
                    print (pixel_hsv[0]) 
                    if h_min < pixel_hsv[0] < h_max: 
                        print ("Element found.")
                        print (x, y)

        

        # self.current_dir = os.path.dirname (__file__)
        # self.__delete_last_ss()

        # yellow_bar_pos = self.__get_yellow_bar()
        # # e_button = self.__get_button_e (yellow_bar_pos)

        # e_button = [yellow_bar_pos[0] + 50, yellow_bar_pos[1]]
        
        # print (e_button[0], e_button[1])
        

    def __get_button_e (self, yellow_bar_pos):
        """
        Get the position and color of button E
        """

        print ('Searching "e" button...')

        x_initial = yellow_bar_pos[0]
        x_final = yellow_bar_pos[0] + 1000
        y_initial = yellow_bar_pos[1]
        y_final = yellow_bar_pos[1] + 1

        match_pixel = self.__compare_pixel_hsv (x_initial, x_final, y_initial, y_final, skip_pixels=2, h_min=226, h_max=230)
        return match_pixel

    def __get_yellow_bar (self): 
        """
        Search the control yellow bar in the screen
        """

        print ("Searching yellow bar...")

        width = pyautogui.size().width
        height = pyautogui.size().height
    
        y_initial = height*.8
        y_final = height
        x_initial = width*.3
        x_final = width*.7

        match_pixel = self.__compare_pixel_hsv (x_initial, x_final, y_initial, y_final, skip_pixels=10, h_min=47, h_max=51)
        return match_pixel

    def __delete_last_ss (self): 
        """
        Delete the last screenshorts in the current work directory
        """

        for file in os.listdir (self.current_dir): 
            if file.endswith (".png"): 
                file_path = os.path.join (self.current_dir, file)
                os.remove (file_path)
    
    def __compare_pixel_hsv (self, x_initial, x_final, y_initial, y_final, skip_pixels, h_min, h_max):
        """
        Compare a specific range of pixels with range of "h" in the color hsv. 
        Return the cordenate of the match pixel
        """

        # Infinite llop for found pixel
        while True: 

            # Loop for "Y" range of pixels
            for y in range(int(y_final), int(y_initial), skip_pixels): 

                # Loop for "X" range of pixels
                for x in range (int(x_initial), int(x_final), skip_pixels):
                    im = pyautogui.screenshot()
                    pixel = im.getpixel((x, y))
                    pixel_r = pixel[0]
                    pixel_g = pixel[1]
                    pixel_b = pixel[2]
                    pixel_hsv = self.__rgb_to_hsv(pixel_r, pixel_g, pixel_b)
                    if h_min < pixel_hsv[0] < h_max: 
                        print ("Element found.")
                        return x, y


    def __rgb_to_hsv(self, r, g, b):
        r, g, b = r/255.0, g/255.0, b/255.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx-mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g-b)/df) + 360) % 360
        elif mx == g:
            h = (60 * ((b-r)/df) + 120) % 360
        elif mx == b:
            h = (60 * ((r-g)/df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = (df/mx)*100
        v = mx*100
        return h, s, v
        


my_auto_gui = Auto_gui()

