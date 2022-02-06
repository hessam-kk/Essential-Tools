import pyautogui
from time import sleep
import easygui
import mss

# Second Way Is MUCH BETTER ###########################################

# These are sizes for screen shot,
# and may vary on diffrent devices or diffrent bookreaders
# find what works best for you, my screen res is: 1920 * 1080
# and it precisely fits Taaghche-bookreader when it fully sticked
# to the left side of the screen
x = 80
y = 55
width = 750
height = 945

# This is First method, export all screens as a single shot 
# and then you need to import them in an app like ms-word
# and export as pdf, not really worth it, QUALITY IS SAME  
# pages_list = []
# sleep(1)
# with mss.mss() as sct:
#     for page in range(10):
#         # The screen part to capture
#         monitor = {"top": 55, "left": 80, "width": 910-155, "height": 1080-135}
#         output = ('img\\'+ str(87+page) + ".png").format(**monitor)
#         # Grab the data
#         sct_img = sct.grab(monitor)
#         # Save to the picture file
#         mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#         pyautogui.click(35, 1080/2)
#         sleep(2)

# # print(pages_list)
# # pages_list.save(r'C:\Users\Hessam\Desktop\tt.pdf', save_all=True, append_images=pages_list)

# easygui.msgbox("Recording Finished", title="Finished!!!!!")
# exit()
# end of first method

# second method 
sleep(1)
pages_list = []
# you need To change this number based your book
# if you are recording from Taaghche-Bookreader, you may
# need to set a higher int that what it shows you
# for example for a 330-page book, 400 is properly works.
number_of_pages = 640

for page in range(number_of_pages):
    # Taking Screen Shot
    myScreenshot = pyautogui.screenshot(region=(670, 90, 1250-670, 1050-90))
    pages_list.append(myScreenshot.convert('RGB'))
    # if you want to save every single pages in a file, uncomment this line
    # myScreenshot.save(r'C:\Users\Hessam\Desktop\'+ str(page) +'.png')
    print(page)
    # Click next
    pyautogui.click(1400, 540)
    # let the animation end, less value may cause taking bad photos
    sleep(0.1)
    # Stop When Mouse Triggered
    if pyautogui.position()[0] != 1400:
        break

# Save to PDF
pages_list[0].save(r'C:\Users\Hessam\Desktop\Ob.pdf', save_all=True, append_images=pages_list)

# alarm when task finished
easygui.msgbox("Recording Finished", title="Finished!!!!!")