import sys,random,time
from PyQt4 import QtGui, QtCore,QtTest

i=0
a=120
b=10
c=180
k=[1,1,1,1,1]
q=[0,0,0,0,0]
#y=[10,0]
arx=[50,100,390,300,215,275]
y=[0,-20,-30,-50,-70]
class Example(QtGui.QMainWindow):
    def __init__(self):
      super(Example, self).__init__()
      self.initUI()
    def initUI(self):
      self.setGeometry(100,100, 400,300)
      self.setWindowTitle('Game')
      self.tboard = Board(self)
      self.setCentralWidget(self.tboard)
      self.statusbar = self.statusBar()        
      self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        
      self.tboard.start()
      self.show() 

class Board(QtGui.QFrame):
    
    msg2Statusbar = QtCore.pyqtSignal(str)

    Speed = 300

    def __init__(self, parent):
        super(Board, self).__init__(parent)
        
        self.initBoard()
    def initBoard(self):     

        self.timer = QtCore.QBasicTimer()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)


    def start(self):
        self.score=0
        self.msg2Statusbar.emit(str(self.score))
       # self.timer.start(Board.Speed, self)

    def loop(self):
        #rint "loopkali"
        self.timer.start(Board.Speed, self)
        #self.msg2Statusbar.emit(str(self.score))

        #self.update()
    def paintEvent(self, event):
        qp = QtGui.QPainter()
        #global i
        #i=i+1
        #Sprint i
        qp.begin(self)
        #self.loop()
        self.drawLines(qp)
        
        
        self.drawdot1(qp,arx[0])
        self.drawdot2(qp,arx[1]) 
        self.drawdot3(qp,arx[2]) 
        self.drawdot4(qp,arx[3])
        self.reddot1(qp,arx[4])
        #qp.end()
        self.update()
        qp.end()

    def drawLines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 4, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        global a,b,c
        c=c+b*2
        a=a+b*2
        b=0
        qp.drawLine(a,275, c, 275)
        

    

    def drawdot1(self,qp,x):
     global k,q,y
     size = self.size()
     if k[0]==1:
          k[0]=0 
          q[0]=time.clock()
     
     if (time.clock()-q[0]) < 1 and k[0]==0:
        dpen = QtGui.QPen(QtCore.Qt.blue, 7, QtCore.Qt.SolidLine)
        qp.setPen(dpen)
        qp.drawPoint(x, y[0])
     elif (time.clock()-q[0]) > 1 and k[0]==0:
        #k[0]=1
        y[0]+=40
        
        if (y[0]>=275):
          if(x>=a)and(x<=c):
               self.score+=1
       
          y[0]=0
          arx[0]=random.randint(1, size.width()-1)
          self.msg2Statusbar.emit(str(self.score))
          print self.score
        k[0]=1
    
    def drawdot2(self,qp,x):
     global k,q,y
     size = self.size()
     if k[1]==1:
          k[1]=0
          q[1]=time.clock()
     
     if (time.clock()-q[1]) < 1 and k[1]==0:
        dpen = QtGui.QPen(QtCore.Qt.blue, 7, QtCore.Qt.SolidLine)
        qp.setPen(dpen)
        qp.drawPoint(x, y[1])
     elif (time.clock()-q[1]) > 1 and k[1]==0:
        #k[1]=1
        y[1]+=30
        
        if (y[1]>=275):
          if(x>=a)and(x<=c):
               self.score+=1
       
          y[1]=0
          arx[1]=random.randint(1, size.width()-1)
          self.msg2Statusbar.emit(str(self.score))
          print self.score
        k[1]=1

    def drawdot3(self,qp,x):
     global k,q,y
     size = self.size()
     if k[2]==1:
          k[2]=0
          q[2]=time.clock()
     
     if (time.clock()-q[2]) < 1 and k[2]==0:
        dpen = QtGui.QPen(QtCore.Qt.blue, 7, QtCore.Qt.SolidLine)
        qp.setPen(dpen)
        qp.drawPoint(x, y[2])
     elif (time.clock()-q[2]) > 1 and k[2]==0:
        #k[2]=1
        y[2]+=20
       
        if (y[2]>=275):
          if(x>=a)and(x<=c):
               self.score+=1
       
          y[2]=0
          arx[2]=random.randint(1, size.width()-1)
          self.msg2Statusbar.emit(str(self.score))
          print self.score
        k[2]=1

    def drawdot4(self,qp,x):
     global k,q,y
     size = self.size()
     if k[3]==1:
          k[3]=0
          q[3]=time.clock()
     
     if (time.clock()-q[3]) < 1 and k[3]==0:
        dpen = QtGui.QPen(QtCore.Qt.blue, 7, QtCore.Qt.SolidLine)
        qp.setPen(dpen)
        qp.drawPoint(x, y[3])
     elif  (time.clock()-q[3]) > 1 and k[3]==0:
        #k[3]=1
        y[3]+=50
        
        if (y[3]>=275):
           if(x>=a)and(x<=c):
             self.score+=1
       
           y[3]=0
           arx[3]=random.randint(1, size.width()-1)
           self.msg2Statusbar.emit(str(self.score))
           
           print self.score
        k[3]=1

    def keyPressEvent(self, event):
        global b
        key = event.key()
        if key == QtCore.Qt.Key_Left:
            b=-1
            
        elif key == QtCore.Qt.Key_Right:
            b=1


    def reddot1(self,qp,x):
     global k,q,y
     size = self.size()
     if k[4]==1:
          k[4]=0
          q[4]=time.clock()
     
     if (time.clock()-q[4]) < 1 and k[4]==0:
        dpen = QtGui.QPen(QtCore.Qt.red, 7, QtCore.Qt.SolidLine)
        qp.setPen(dpen)
        qp.drawPoint(x, y[4])
     elif (time.clock()-q[4]) > 1 and (k[4]==0):
        #k[4]=1
        y[4]+=80
        
        if (y[4]>=275):
                 if(x>=a)and(x<=c):
                     print "Game over!"
            #string="-- Game Over!!!"+self.score
                     self.msg2Statusbar.emit("-- Game Over!!! Score =  "+str(self.score))
                     QtTest.QTest.qWait(2000)
                     sys.exit()            
       
                 y[4]=0
                 arx[4]=random.randint(1, size.width()-1)

                 print self.score
        k[4]=1
def main():
   app = QtGui.QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()









