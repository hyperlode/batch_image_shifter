import wx

import os


class MyCanvas(wx.ScrolledWindow):
    def __init__(self, parent, id = -1, size = wx.DefaultSize, filepath = None):
        wx.ScrolledWindow.__init__(self, parent, id, (0, 0), size=size, style=wx.SUNKEN_BORDER)
        self.LoadImage(filepath)
        
    def LoadImage(self, path):
        self.image = wx.Image(filepath)
        self.w = self.image.GetWidth()
        self.h = self.image.GetHeight()
        self.bmp = wx.BitmapFromImage(self.image)

        self.SetVirtualSize((self.w, self.h))
        self.SetScrollRate(20,20)
        self.SetBackgroundColour(wx.Colour(0,0,0))

        self.buffer = wx.EmptyBitmap(self.w, self.h)
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        self.DoDrawing(dc)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_UP, self.OnClick)

    def OnClick(self, event):
        pos = self.CalcUnscrolledPosition(event.GetPosition())
        # print('%d, %d' %(pos.x, pos.y))
        s = "{},{},{},{},{}\n".format(filepath,self.w, self.h, pos.x, pos.y)
        with open(logfile, "a") as f:
            f.write(s)
        print(s)
        # self.LoadImage(r"C:\Data\Dropbox\Camera Uploads\2019-07-05 22.45.37.jpg")

    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self, self.buffer, wx.BUFFER_VIRTUAL_AREA)

    def DoDrawing(self, dc):
        dc.DrawBitmap(self.bmp, 0, 0)

class MyFrame(wx.Frame): 
    def __init__(self, parent=None, id=-1, filepath = None): 
        wx.Frame.__init__(self, parent, id, title=filepath)
        self.canvas = MyCanvas(self, -1, filepath = filepath)

        self.canvas.SetMinSize((self.canvas.w, self.canvas.h))
        self.canvas.SetMaxSize((self.canvas.w, self.canvas.h))
        self.canvas.SetBackgroundColour(wx.Colour(0, 0, 0))
        vert = wx.BoxSizer(wx.VERTICAL)
        horz = wx.BoxSizer(wx.HORIZONTAL)
        vert.Add(horz,0, wx.EXPAND,0)
        vert.Add(self.canvas,1,wx.EXPAND,0)
        self.SetSizer(vert)
        vert.Fit(self)
        self.Layout()

if __name__ == '__main__':

    app = wx.App()
    app.SetOutputWindowAttributes(title='stdout')  
    wx.InitAllImageHandlers()

    # SOURCE_DIR = r"C:\Temp\KVR\andi on bike selection 1\cycling\cycle towards"
    # SOURCE_DIR = r"C:\Temp\KVR\andi on bike selection 1\cycling\cycle away\1"
    # SOURCE_DIR = r"C:\Temp\KVR\andi on bike selection 1\cycling\cycle away\2"
    SOURCE_DIR = r"C:\Temp\KVR\andi on bike selection 1\cycling\cycle away\3"
    RESULTS = "coords.txt"
    logfile = "{}/{}".format(SOURCE_DIR, RESULTS)

    
    
    files = os.listdir(SOURCE_DIR)
    images = []
    print(files)
    for file in files:
        ext = file[-3:].lower()
        if ext in ["jpg","peg"]:
            images.append("{}/{}".format(SOURCE_DIR, file))
    print(images)
    
    for filepath in images:
        print(filepath)
        myframe = MyFrame(filepath=filepath)
        myframe.Center()
        myframe.Show()
        app.MainLoop()