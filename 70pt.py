#########################################
#
#    70pt - Basic collision detection
#
#########################################

# When the player moves the ball into the rectangle, turn the rectangle red
# You will need to code the movement of the player and the collision detection.

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
tx1 = 200
ty1 = 20
tx2 = 280
ty2 = 80
target = drawpad.create_rectangle(tx1,ty1,tx2,ty2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")



class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.Upbutton = Button(self.myContainer1)
		self.Upbutton.configure(text="Up", background= "green")
		self.Upbutton.grid(row=0,column=0)
		self.Upbutton.bind("<Button-1>", self.UpClicked)

		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		

		
        def UpClicked(self, event):   
	       global oval
	       global player
	       drawpad.move(player,0,-20)
               global tx1, tx2, ty1, ty2
               x1, y1, x2, y2 = drawpad.coords(player) 
               if (tx1 < x1 and tx2 > x2) and (ty1 < y1 and ty2 > y2):
	            drawpad.itemconfig(target, fill = "red")
	       
	            
	       
		
	
	
		
myapp = MyApp(root)

root.mainloop()