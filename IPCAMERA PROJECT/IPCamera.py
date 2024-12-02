import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
from ptz_control import PTZController  


ip = "192.168.4.64" 
port = 80  
user = "admin"  
passwd = "Admin8503"  

mycam = PTZController(ip, port, user, passwd)  

# Global variables
theMove = ""
zoomX = 0.0
camX = 0.0
camY = 0.0
theX = 0.0
theEachMove = 0.0

class WEBCAMAPP:
    def __init__(self, window, frame_video):
        rtsp_url = 'rtsp://admin:Admin8503@192.168.4.64:554'
        self.window = window
        self.frame_video = frame_video
        self.video_capture = cv2.VideoCapture(rtsp_url)
        self.currentImage = None
        self.canvas = tk.Canvas(master=self.frame_video,bg="BLACK",width=1500, height=1500)
        self.canvas.pack()
        self.update_webcam()

    def update_webcam(self):
        ret, frame = self.video_capture.read()
        if ret:
            self.currentImage = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.photo = ImageTk.PhotoImage(image=self.currentImage)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(15, self.update_webcam)

    def __del__(self):
        # Release the webcam when the app is closed
        if self.video_capture.isOpened():
            self.video_capture.release()

def main():
    def moveStop():
        global mycam
        mycam.stop()
        
    def showStatus():
        global mycam
        global theMove
        if theMove == "":
            label.configure(text="You did not choose a move style")
        elif theMove == "Absolute Move":
            label.configure(text=f"XNOW: {mycam.xnow * 180}\nYNOW: {mycam.ynow * 180}\nZOOM: {mycam.zoomx * 180}")
        elif theMove == "Continuous Move":
            label.configure(text=f"You cannot get the status in {theMove}")
    
    def resetCamera():
        global mycam, camY, camX, zoomX
        mycam.myAbsoluteMove(mycam.settedX, mycam.settedY, mycam.settedZoom)
        label.configure(text="Position of camera reset")

    def zoomPositive():
        global mycam, theEachMove, zoomX, theMove
        if theMove == "Absolute Move":
            temp = zoomX + theEachMove
            if temp >= 1.0:
                mycam.myAbsoluteMove(camX, camY, 1.0)
                label.configure(text="Out of bounds. The bounds: -1.0 ~ 1.0", justify=tk.LEFT)
            else:
                zoomX += theEachMove
                mycam.myAbsoluteMove(camX, camY, zoomX)
        elif theMove == "Continuous Move":
            theEachMove = abs(theEachMove)
            mycam.myContinuousMove(0, 0, float(theEachMove))
    
    def zoomNegative():
        global mycam, theEachMove, zoomX, theMove
        if theMove == "Absolute Move":
            temp = zoomX - theEachMove
            if temp <= -1.0:
                mycam.myAbsoluteMove(camX, camY, -1.0)
                label.configure(text="Out of bounds. The bounds: -1.0 ~ 1.0", justify=tk.LEFT)
            else:
                zoomX -= theEachMove
                mycam.myAbsoluteMove(camX, camY, zoomX)
        elif theMove == "Continuous Move":
            theEachMove = -abs(theEachMove)
            mycam.myContinuousMove(0, 0, float(theEachMove))
    
    def setPreset():
        global mycam, camX, camY, zoomX
        mycam.settedX = camX
        mycam.settedY = camY
        mycam.settedZoom = zoomX
        label.configure(text="Preset is set for camera reset")
    
    def moveRight():
        global mycam, theEachMove, camX, theMove
        if theMove == "Absolute Move":
            temp = camX + theEachMove
            if temp >= 1.0:
                camX = 1.0
                mycam.myAbsoluteMove(1.0, camY, zoomX)
                label.configure(text="Out of bounds. The bounds: -1.0 ~ 1.0", justify=tk.LEFT)
            else:
                camX += theEachMove
                mycam.myAbsoluteMove(camX, camY)
        elif theMove == "Continuous Move":
            theEachMove = abs(theEachMove)
            mycam.myContinuousMove(float(theEachMove), 0, 0)
        elif theMove == "Relative Move":
            temp = camX + theEachMove
            if temp >= 1.0:
                camX = 0.1
                mycam.myRelativeMove(camX, camY)
            else:
                camX += theEachMove
                mycam.myRelativeMove(camX, camY)
    
    def moveLeft():
        global mycam, theEachMove, camX, theMove
        if theMove == "Absolute Move":
            temp = camX - theEachMove
            if camX <= -1.0:
                camX = -1.0
                mycam.myAbsoluteMove(-1.0, camY, zoomX)
                label.configure(text="Out of bounds. The bounds: -1.0 ~ 1.0", justify=tk.LEFT)
            else:
                camX -= theEachMove
                mycam.myAbsoluteMove(camX, camY)
        elif theMove == "Continuous Move":
            theEachMove = -abs(theEachMove)
            mycam.myContinuousMove(float(theEachMove), 0, 0)
        elif theMove == "Relative Move":
            temp = camX - theEachMove
            if temp <= -1.0:
                camX = -0.1
                mycam.myRelativeMove(camX, camY)
            else:
                camX -= theEachMove
                mycam.myRelativeMove(camX, camY)
    
    def moveUp():
        global mycam, theEachMove, camY, theMove
        if theMove == "Absolute Move":
            temp = camY + (theEachMove / 2)
            if camY >= 0.25:
                camY = 0.25
                mycam.myAbsoluteMove(camX, 0.25, zoomX)
                label.configure(text="Out of bounds. The bounds: -0.5 ~ 0.25", justify=tk.LEFT)
            else:
                camY += (theEachMove / 2)
                mycam.myAbsoluteMove(camX, camY)
        elif theMove == "Continuous Move":
            theEachMove = abs(theEachMove)
            mycam.myContinuousMove(0, float(theEachMove), 0)
        elif theMove == "Relative Move":
            temp = camX + theEachMove
            if temp >= 0.25:
                camY = 0.25
                mycam.myRelativeMove(camX, camY)
                label.configure(text="Out of bounds. The bounds: -0.5 ~ 0.25", justify=tk.LEFT)
            else:
                camY += theEachMove
                mycam.myRelativeMove(camX, camY)
    
    def moveDown():
        global mycam, theEachMove, camY, theMove
        if theMove == "Absolute Move":
            temp = camY - (theEachMove / 2)
            if camY <= -0.5:
                camY = -0.5
                mycam.myAbsoluteMove(camX, -0.5, zoomX)
                label.configure(text="Out of bounds. The bounds: -0.5 ~ 0.25", justify=tk.LEFT)
            else:
                camY -= (theEachMove / 2)
                mycam.myAbsoluteMove(camX, camY)
        elif theMove == "Continuous Move":
            theEachMove = -abs(theEachMove)
            mycam.myContinuousMove(0, theEachMove, 0)
        elif theMove == "Relative Move":
            temp = camY - theEachMove
            if temp <= -0.5:
                camY = -0.5
                mycam.myRelativeMove(camX, camY)
                label.configure(text="Out of bounds. The bounds: -0.5 ~ 0.25", justify=tk.LEFT)
            else:
                camY -= theEachMove
                mycam.myRelativeMove(camX, camY)
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    root.title("IPCAMERA APP")
    root.geometry("825x390")
    root.attributes("-fullscreen", "False")

    # Frames
    frame_buttons = ctk.CTkFrame(master=root, width=300, height=210)
    frame_buttons.grid(row=1, column=0)

    frame_label = ctk.CTkFrame(master=root, width=300, height=75)
    frame_label.grid(row=0, column=0)

    frame_combo = ctk.CTkFrame(master=root, width=300, height=125)
    frame_combo.grid(row=2, column=0)

    frame_video = ctk.CTkFrame(master=root, width=600, height=410)
    frame_video.place(relx=0.37,rely=0.0)

    # Webcam display
    webcam_app = WEBCAMAPP(root, frame_video)

    # Buttons and other controls
    left = ctk.CTkButton(master=frame_buttons, width=25, height=20, text="LEFT", command=moveLeft)
    left.place(relx=0.05, rely=0.35)

    right = ctk.CTkButton(master=frame_buttons, width=25, height=20, text="RIGHT", command=moveRight)
    right.place(relx=0.80, rely=0.35)
    
    up = ctk.CTkButton(master=frame_buttons, width=50, height=20, text="UP", command=moveUp)
    up.place(relx=0.4, rely=0.15)

    down = ctk.CTkButton(master=frame_buttons, width=25, height=20, text="DOWN", command=moveDown)
    down.place(relx=0.4, rely=0.55)
    
    stop = ctk.CTkButton(master=frame_buttons, width=30, height=30, text="STOP", command=moveStop)
    stop.place(relx=0.05, rely=0.8)

    show = ctk.CTkButton(master=frame_buttons, width=30, height=30, text="STATUS", command=showStatus)
    show.place(relx=0.27, rely=0.8)

    reset = ctk.CTkButton(master=frame_buttons, width=30, height=30, text="RESET", command=resetCamera)
    reset.place(relx=0.5, rely=0.8)

    setPreset1 = ctk.CTkButton(master=frame_buttons, width=30, height=30, text="SET PRESET", command=setPreset)
    setPreset1.place(relx=0.7, rely=0.8)

    zoompo = ctk.CTkButton(master=frame_buttons, width=30, height=30, text="ZOOM+", command=zoomPositive)
    zoompo.place(relx=0.3, rely=0.33)

    zoomne = ctk.CTkButton(master=frame_buttons, width=30, height=30, text="ZOOM-", command=zoomNegative)
    zoomne.place(relx=0.5, rely=0.33)

    my_font = ctk.CTkFont(family="Arial", size=15)
    label = ctk.CTkLabel(master=frame_label,
                        text="Please select your movement.\nFor continuous you cannot set a speed.",
                        width=130,
                        height=25,
                        font=my_font,
                        justify=tk.LEFT
                        )
    label.place(relx=0.0, rely=0.0)

    OptionMenu_var = ctk.StringVar(value="Choose your move")
    combobox1 = ctk.CTkComboBox(master=frame_combo,
                               values=["Relative Move", "Continuous Move", "Absolute Move"],
                               variable=OptionMenu_var)
    combobox1.place(relx=0.27, rely=0.07)

    OptionMenu_var2 = ctk.StringVar(value="1")
    combobox2 = ctk.CTkComboBox(master=frame_combo,
                               values=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                               variable=OptionMenu_var2)
    combobox2.place(relx=0.27, rely=0.3)

    def start():
        global theX, theMove, mycam, theEachMove
        if theMove == "Absolute Move":
            theX = float(theX)
            theEachMove = theX
            x = theEachMove * 180
            y = (theEachMove / 2) * 360
            label.configure(text=f"Movement Style: {theMove}\nThe move per x in degree: {x}\nThe move per y in degree: {y}")
        elif theMove == "Continuous Move":
            theX = float(theX)
            theEachMove = theX
            label.configure(text=f"Movement Style: {theMove}")
        elif theMove == "Relative Move":
            theX = float(theX)
            theEachMove = theX
            x = theEachMove * 360
            y = (theEachMove / 2) * 360
            label.configure(text=f"Movement Style: {theMove}\nThe move per x in degree: {x}\nThe move per y in degree: {y}")

    def comboGet():
        global theMove
        theMove = str(combobox1.get())
        comboGet2()

    def comboGet2():
        global theX
        theX = float(combobox2.get())
        theX = (theX / 100) * 10
        start()

    buttonForCombo = ctk.CTkButton(master=frame_combo, text="Apply Move", command=comboGet)
    buttonForCombo.place(relx=0.27, rely=0.53)

    root.mainloop()

if __name__ == "__main__":
    main()


