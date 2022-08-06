from picographics import PicoGraphics, DISPLAY_INKY_PACK

class Screen:
    def __init__(self, center_circle_x, line_length):
        self.center_circle_x = center_circle_x
        self.line_length = line_length
        self.display = PicoGraphics(display=DISPLAY_INKY_PACK)
        self.display.set_update_speed(2)
        self.erase()
    
    # draw all static items (TODO: Add more dynamic features to some items)
    def draw(self):
        # Draw shapes for bus routes
        line_start = self.center_circle_x - int(self.line_length / 2)
        self.display.circle(self.center_circle_x, 32, 10)
        self.display.rectangle(line_start, 30, 148, 4)
        self.display.circle(self.center_circle_x, 96, 10)
        self.display.rectangle(line_start, 94, 148, 4)
        
        # Write bus names
        self.display.set_font("bitmap14_outline")
        string1 = "343"
        string2 = "302"
        string_width = int(self.display.measure_text(string1, 1)) + 1
        x = line_start - string_width
        self.display.text(string1, x, 24, scale=1)
        string_width = int(self.display.measure_text(string2, 1)) + 1
        x = line_start - string_width
        self.display.text(string2, x, 89, scale=1)
        x = line_start + self.line_length + 1
        self.display.text(string1, x, 24, scale=1)
        self.display.text(string2, x, 89, scale=1)
        
        # Write bus stop names
        self.display.set_font("bitmap8")
        string = "Jetland"
        x = self.center_circle_x - int(self.display.measure_text(string, 2) / 2)
        self.display.text(string, x, 5, scale=2)
        string = "Derravaragh Road"
        x = self.center_circle_x - int(self.display.measure_text(string, 2) / 2)
        self.display.text(string, x, 69, scale=2)
        
        # Write button prompts
        self.display.set_font("bitmap8")
        self.display.text("Next Bus >", 250, 15, scale=1)
        self.display.text("Next Bus +1 >", 239, 57, scale=1)
        self.display.text("Next Bus +2 >", 239, 98, scale=1)
        self.display.update()
    
    # Clear screen
    def erase(self):
        self.display.set_pen(15)
        self.display.clear()
        self.display.set_pen(0)
    
    # Update bus times
    def update_time(self, stop1, stop2):
        self.erase()
        self.display.set_font("bitmap6")
        string = stop1
        x = self.center_circle_x - int(self.display.measure_text(string, 2) / 2)
        self.display.text(string, x, 45, scale=2)
        string = stop2
        x = self.center_circle_x - int(self.display.measure_text(string, 2) / 2)
        self.display.text(string, x, 110, scale=2)
        self.draw()
      
    
