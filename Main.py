from ID_Generator import id_generator_j1 as ID  #Importing the required id
from time import sleep
import pyautogui as py
import Color_check as color

error_id = []
while(True):
    for i in ID.id:
        j=0
        hello = str(i)  #Selecting an element from the list of id's available

        sleep(5)
        #Login Page
        py.click(1102 , 299)    #Username textbox selection
        py.hotkey("ctrl","a")
        py.typewrite(hello)     #Entering username
        py.move(1303 , 299)
        py.click(1303 , 299)    #Password textbox selection
        py.hotkey("ctrl","a")
        py.typewrite(hello)     #Entering password
        print(hello)
        py.moveRel(1412 , 299)
        py.click(1412 , 299)    #Clicking on login button
        
        while (True):
            White = color.checkColor(148 , 821)       #Setting the colour of left sidebar 
            Light_blue = color.checkColor(993 , 380)  #Setting colour at the point just below the username and password section
            print(White)
            print(Light_blue)
    
            if(White == [240 , 240 , 240]):     #Checks whether login has failed or not. If the left sidebar colour is white, then login is failed.
                j = j+1
                sleep(1)
                print("Not Login")
                print(j)
                if(j > 10): #To wait for 10s whether t
                    if(Light_blue == [207, 231, 253]):  #
                        error_id.append(i)
                        print("Error id collected")
                    break
    
            if(White == [48, 57, 70]):
                #Profile Download
                print("Login")
                print(hello)
                py.click(206 , 286)
                py.click(191 , 323)
                while (True):
                    yellow = color.checkColor(953 , 511)

                    if(yellow != [255 , 255 , 204]):
                        print("No Print")
                        sleep(3)
                        continue
                        
                    elif(yellow == [255 , 255 , 204]):
                        print("Print")
                        py.hotkey("ctrlleft","p")
                        sleep(3)
                        py.click(1561 , 980)
                        sleep(2)
                        py.typewrite(hello)
                        py.hotkey("enter")
                        sleep(2)
                        py.click(1806 , 178)
                        
                        while(True):
                            blue = color.checkColor(1134 , 563)
                            
                            if (blue != [33, 64, 91]):
                                print("Not Login Page")
                                sleep(3)
                                continue
                            elif(blue == [33, 64, 91]):
                                print("Login Page")
                                break
                        break
                break
    break

if(len(error_id) > 0):
    print("These id's couldn't be resolved:")
    for i in range(len(error_id)):
        print(error_id[i])