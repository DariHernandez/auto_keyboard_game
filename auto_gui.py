#! python3

import pyautogui, os, logging, sys

logging.basicConfig(filename='log.txt', level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s' )

class Auto_gui ():
    """
    Automate kyboard and mouse, reading specific pixles of the screen
    """

    def __init__ (self): 
        """
        Constructor of class
        """

        # Clean log file
        file = open("log.txt", 'w')
        file.write ("")
        file.close()

        print ('Running program. Press "Ctrl" + "C" to exit.')

        try: 

            self.current_dir = os.path.dirname (__file__)

            self.__delete_last_ss()

            self.screen_values = {
                "width": 1600, 
                "height": 900, 
                "x_initial": 832, 
                "y_initial": 752, 
                "x_final": 833, 
                "y_final": 753,
            }

            self.__update_screen_values()
            
            logging.info(self.screen_values)

            self.skip_pixels = 2
            self.h_min = 47 
            self.h_max = 51

            while True: 
                self.__search_e_button()

        except KeyboardInterrupt:
            print ("\b\bProgram finished.")
            sys.exit()



    def __search_e_button (self): 
        """
        Seach alert for press button "E" and send "E" with the keyboard
        """

        print ('\tWaiting "e" button')

        # Infinite llop for found pixel
        while True: 

            # Loop for "Y" range of pixels
            for y in range(int(self.screen_values["y_initial"]), int( self.screen_values["y_final"]), self.skip_pixels): 

                # Loop for "X" range of pixels
                for x in range (int(self.screen_values["x_initial"]), int( self.screen_values["x_final"]), self.skip_pixels):
                    im = pyautogui.screenshot()
                    pixel = im.getpixel((x, y))
                    pixel_r = pixel[0]
                    pixel_g = pixel[1]
                    pixel_b = pixel[2]
                    pixel_hsv = self.__rgb_to_hsv(pixel_r, pixel_g, pixel_b)
                    logging.info ("pixel_hsv: {}".format(pixel_hsv)) 
                    if self.h_min < pixel_hsv[0] < self.h_max: 
                        print ('\tElement found. Sending key "E"')
                        pyautogui.press ('E')
                        return None



    def __update_screen_values (self): 
        """
        Return a updated dictionary with the correct values of the program
        for the current screen size
        """

        for key, value in self.screen_values.items(): 

            current_width = pyautogui.size()[0]
            current_height = pyautogui.size()[1]

            if str(key).startswith("x"): 
                self.screen_values[key] = current_width * value / self.screen_values["width"]
            elif str(key).startswith("y"):
                self.screen_values[key] = current_height * value / self.screen_values["height"]
        
        

    def __delete_last_ss (self): 
        """
        Delete the last screenshorts in the current work directory
        """

        for file in os.listdir (self.current_dir): 
            if file.endswith (".png"): 
                file_path = os.path.join (self.current_dir, file)
                os.remove (file_path)
    

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

