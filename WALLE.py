import time
from tkinter import *
from tkinter.ttk import Progressbar

class HighBorn:
    def __init__(self, direction_label, status_label):
        self.direction = 'NORTH'  # Initial direction
        self.status = 'STOPPED'
        self.direction_label = direction_label
        self.status_label = status_label

    def update_labels(self):
        self.direction_label['text'] = f"Current Direction: {self.direction}"
        self.status_label['text'] = f"Status: {self.status}"

    def move_forward(self):
        print(f"Moving forward...")
        self.status = 'MOVING FORWARD'
        self.update_labels()

    def move_backward(self):
        print(f"Moving backward...")
        self.status = 'MOVING BACKWARD'
        self.update_labels()

    def turn_left(self):
        print(f"Turning left...")
        self.direction = {
            'NORTH': 'WEST',
            'WEST': 'SOUTH',
            'SOUTH': 'EAST',
            'EAST': 'NORTH',
        }[self.direction]
        self.update_labels()

    def turn_right(self):
        print(f"Turning right...")
        self.direction = {
            'NORTH': 'EAST',
            'EAST': 'SOUTH',
            'SOUTH': 'WEST',
            'WEST': 'NORTH',
        }[self.direction]
        self.update_labels()

    def stop(self):
        print(f"Stopping...")
        self.status = 'STOPPED'
        self.update_labels()

    def roll(self):
        print(f"Rolling...")
        self.status = 'ROLLING'
        self.update_labels()

def update_loading(window, label, progress, percentage):
    label['text'] = f'Loading: {percentage}% complete'
    progress['value'] = percentage
    window.update()
    time.sleep(0.05)  # wait for a bit

def start_robot(window, label, progress):
    label['text'] = 'Project Highborn Controls'
    progress.pack_forget()  # Hide progress bar

    # Display the current direction
    direction_label = Label(window, text=f"Current Direction: NORTH", bg='black', fg='green', font=('Fixedsys', 24))
    direction_label.pack()

    # Display the current status
    status_label = Label(window, text=f"Status: STOPPED", bg='black', fg='green', font=('Fixedsys', 24))
    status_label.pack()

    # Instantiate robot with labels
    robot = HighBorn(direction_label, status_label)

    # Define controls
    controls = {
        'Move Forward': robot.move_forward,
        'Move Backward': robot.move_backward,
        'Turn Left': robot.turn_left,
        'Turn Right': robot.turn_right,
        'Roll': robot.roll,  # Added roll here
        'Stop': robot.stop
        
    }

    button_font = ('Fixedsys', 24)
    for button_text, button_command in controls.items():
        button = Button(window, text=button_text, command=button_command)
        button.configure(bg='black', fg='green', activebackground='dark green', font=button_font)
        button.pack(pady=10)  # Added padding here

# Create tkinter window
window = Tk()
window.title("Project Highborn")
window.geometry("1920x1080")  # set window size
window.configure(bg='black')  # Set background color to black

# Create a retro-style font
retro_font = ('Fixedsys', 48)

# Initial title
label = Label(window, text='Project Highborn', bg='black', fg='green', font=retro_font)
label.pack(pady=200)

progress = Progressbar(window, length=1000)
progress.pack()

def start_loading():
    label['text'] = ''
    # Show a loading screen
    for i in range(101):
        update_loading(window, label, progress, i)
    label['text'] = 'Loading Complete'
    time.sleep(1)

    # Start robot control
    start_robot(window, label, progress)

# Start loading after a delay
window.after(2000, start_loading)

# Run the tkinter window
window.mainloop()
