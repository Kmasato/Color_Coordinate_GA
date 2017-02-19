import wx
import random
import cv2
import numpy as np
import ga as GA
import hsv_eval as ev


class Mywin(wx.Frame):
    def __init__(self,parent,title):
        super(Mywin,self).__init__(parent,title=title,size = (850,600))

        self.root_panel = wx.Panel(self, wx.ID_ANY)
        self.button_panel = Button(self.root_panel)
        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(self.button_panel, 0, wx.GROW | wx.LEFT | wx.RIGHT | wx.ALIGN_BOTTOM, border = 20)
        self.root_panel.SetSizer(root_layout)
        
        self.C = list()
        self.P1 = Chara(0,0,0)
        self.P2 = Chara(0,0,0)
        self.p1_list = list()
        self.p2_list = list()

        self.start_flag = 0
        self.gene = 0
        self.ave = 0
        self.InitUI()
        self.createTimer()
        #self.InitUI()
    
    def InitBuffer(self):
        size = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(max(1,size.width), max(1,size.height))
        dc = wx.BufferedDC(None, self.buffer)
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))

    def InitUI(self):
        self.Center()

        self.Bind(wx.EVT_BUTTON, self.startbutton, self.button_panel.start_button)
        self.Bind(wx.EVT_BUTTON, self.stopbutton, self.button_panel.stop_button)
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        self.Show(True)
     
    def createTimer(self):
        self.timer=wx.Timer(self)
        self.timer.Start(20)
        self.Bind(wx.EVT_TIMER, self.onTimer, self.timer)

    def onTimer(self, event):
        self.InitBuffer()
        self.Refresh()
        #dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        #dc.BeginDrawing()


        #dc.EndDrawing()



    def startbutton(self, event):
        self.start_flag = 1
        #self.InitBuffer()
        #dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        #dc.Clear()
        self.Refresh()
    def stopbutton(self, event):
        self.start_flag = 0
        self.Refresh()

    def show_result(self):
        result_index, second_index = GA.elite_chose(self.C)
        self.result = Chara(380,200,0)  
        for i in range(3):
                self.result.body[i] = self.C[result_index].body[i]
        for i in range(3):
                self.result.bottom[i] = self.C[result_index].bottom[i]
        for i in range(3):
                self.result.shoes[i] = self.C[result_index].shoes[i]







        




    def OnPaint(self,e):
        
        dc = wx.PaintDC(self)
        self.gene = self.gene + 1
        #dc = wx.BufferedDC(dc)
        self.count = -1

        if self.start_flag == 0:
            for i in range(3):
                for j in range(10):
                    self.count += 1
                    self.C.append(Chara(j*80+15,i*150+50,self.count))
                    self.C[self.count].draw(dc)
        elif self.start_flag == 1:

            print("Generation:", self.gene)
            for i in range(30):
                #print self.C[i].id
                self.C[i].score = 0
                self.C[i].score = self.C[i].score + ev.hue_eval(self.C[i].body[0],self.C[i].bottom[0])
                self.C[i].score = self.C[i].score + ev.hue_eval(self.C[i].bottom[0],self.C[i].shoes[0])
                self.C[i].score = self.C[i].score + ev.sat_val_eval(self.C[i].body[1],self.C[i].bottom[1],self.C[i].body[2],self.C[i].bottom[2])
                self.C[i].score = self.C[i].score + ev.sat_val_eval(self.C[i].bottom[1],self.C[i].shoes[1],self.C[i].bottom[2],self.C[i].shoes[2])
                print self.C[i].score
       
            self.P1 = GA.roulette_chose(self.C)
            while True:
                self.P2 = GA.roulette_chose(self.C)
                self.p1_list = [self.P1.body[0], self.P1.body[1], self.P1.body[2], self.P1.bottom[0], self.P1.bottom[1], self.P1.bottom[2], self.P1.shoes[0], self.P1.shoes[1], self.P1.shoes[2]]
                self.p2_lit = [self.P2.body[0], self.P2.body[1], self.P2.body[2], self.P2.bottom[0], self.P2.bottom[1], self.P2.bottom[2], self.P2.shoes[0], self.P2.shoes[1], self.P2.shoes[2]]
                self
                if self.p1_list != self.p2_list:
                    break
                else:
                    continue
          # print self.P2.id
          # print self.P1.id
            

            e1, e2 = GA.elite_chose(self.C)
            for i in range(3):
                 self.C[0].body[i] = self.C[e1].body[i]
            for i in range(3):
                self.C[0].bottom[i] = self.C[e1].bottom[i]
            for i in range(3):
                self.C[0].shoes[i] = self.C[e1].shoes[i]

            for i in range(3):
                 self.C[1].body[i] = self.C[e2].body[i]
            for i in range(3):
                self.C[1].bottom[i] = self.C[e2].bottom[i]
            for i in range(3):
                self.C[1].shoes[i] = self.C[e2].shoes[i]





            count_n = 2
            p1 = [self.P1.body[0], self.P1.body[1], self.P1.body[2], self.P1.bottom[0], self.P1.bottom[1], self.P1.bottom[2], self.P1.shoes[0], self.P1.shoes[1], self.P1.shoes[2]]
            p2 = [self.P2.body[0], self.P2.body[1], self.P2.body[2], self.P2.bottom[0], self.P2.bottom[1], self.P2.bottom[2], self.P2.shoes[0], self.P2.shoes[1], self.P2.shoes[2]]
            #print p1
            #print p2

            while True:
                c1, c2 = GA.cross(p1,p2)
                for i in range(3):
                    self.C[count_n].body[i] = c1[i]
                for i in range(3):
                    self.C[count_n].bottom[i] = c1[i+3]
                for i in range(3):
                    self.C[count_n].shoes[i] = c1[i+6]
                
                count_n = count_n + 1

                for i in range(3):
                    self.C[count_n].body[i] = c2[i]
                for i in range(3):
                    self.C[count_n].bottom[i] = c2[i+3]
                for i in range(3):
                    self.C[count_n].shoes[i] = c2[i+6]

                count_n = count_n + 1

                if count_n == 30:
                    break



            self.count = 0
            for i in range(3):
                for j in range(10):
                    self.C[self.count].draw(dc)
                    self.count += 1

            if ev.judge(self.C) == True:
                self.show_result()
                self.result.draw(dc)
                self.start_flag = 2
                print "Generation:", self.gene
                print "BODY",(self.result.body[0], self.result.body[1], self.result.body[2])
                print "BOTTOM",(self.result.bottom[0], self.result.bottom[1], self.result.bottom[2])
                print "SHOES",(self.result.shoes[0], self.result.shoes[1], self.result.shoes[2])


        
        elif self.start_flag == 2:
            self.result.draw(dc)
           

class Button(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        self.start_button = wx.Button(self, wx.ID_ANY, u"START")
        self.stop_button  = wx.Button(self, wx.ID_ANY, u"STOP")
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(self.start_button, flag = wx.GROW | wx.ALIGN_BOTTOM)
        layout.Add(self.stop_button, flag = wx.GROW)
        self.SetSizer(layout)



class Chara:
    def __init__(self,X,Y,ID):
        self.body = self.RandColor()
        self.bottom = self.RandColor()
        self.shoes = self.RandColor()
        self.x = X
        self.y = Y
        self.id = ID
        self.score = 0
        self.p = 0
    
    #Set first status
    def RandColor(self):
        self.hue = random.randint(0,180)
        self.satu = random.randint(0,255)
        self.value = random.randint(0,255)
        return [self.hue, self.satu, self.value]


    def draw(self,dc):
        # draw body
        self.rgb = hsv_to_rgb(self.body[0], self.body[1], self.body[2])
        self.color = wx.Colour(self.rgb[0], self.rgb[1], self.rgb[2])
        dc.SetPen(wx.Pen(self.color))
        dc.SetBrush(wx.Brush(self.color))
        dc.DrawRectangle(self.x,self.y,70,50)
        
        #draw bottom
        self.rgb = hsv_to_rgb(self.bottom[0], self.bottom[1], self.bottom[2])
        self.color = wx.Colour(self.rgb[0],self.rgb[1],self.rgb[2])
        dc.SetPen(wx.Pen(self.color))
        dc.SetBrush(wx.Brush(self.color))
        dc.DrawRectangle(self.x,self.y+50,70,50)

        #draw shoes
        self.rgb = hsv_to_rgb(self.shoes[0], self.shoes[1], self.shoes[2])
        self.color = wx.Colour(self.rgb[0],self.rgb[1],self.rgb[2])
        dc.SetPen(wx.Pen(self.color))
        dc.SetBrush(wx.Brush(self.color))
        dc.DrawRectangle(self.x,self.y+100,70,20)

   
        



def hsv_to_rgb(h,s,v):
    bgr = cv2.cvtColor(np.array([[[h,s,v]]], dtype = np.uint8),cv2.COLOR_HSV2BGR)[0][0]
    return (bgr[2], bgr[1], bgr[0])

def rgb_to_hsv(r,g,b):
    hsv = cv2.cvtColor(np.array([[[b,g,r]]], dtype = np.uint8), cv2.COLOR_BGR2HSV)[0][0]
    return (hsv[0], hsv[1], hsv[0])
    

if __name__ == '__main__':
    ex = wx.App()
    Mywin(None,'Draw Character')
    ex.MainLoop()

