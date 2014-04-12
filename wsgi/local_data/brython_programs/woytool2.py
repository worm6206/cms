# -*- coding: cp1252 -*-
#
# Copyright Hans-Bernhard Woyand 
# Kirchstrasse 36a, D58456 Witten
# December 3, 2006 (3.12.2006)
#
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
#

from math import *
from Tkinter import *
from Canvas import *
#from numpy import *
import time

line = 80*"-"

class woyDraw:
    
    def __init__(self,ww,wh,root=NONE):

        self.xmin = 0
        self.xmax = ww
        self.ymin = wh
        self.ymax = 0
        
        if root==NONE:
            self.tk=Tk()
        else:
            self.tk = Toplevel(root)
        if ww <= 0.0:
            raise "<woyDraw - init> Fehler - Breite der Zeichenfläche muss > 0 sein!"
        else:
            self.ww = ww
        if wh <= 0.0:
            raise "<woyDraw - init> Fehler - Höhe der Zeichenfläche muss > 0 sein!"
        else:
            self.wh = wh       

    def close(self):
        self.tk.destroy()

    def settitle(self, title):
        self.title = title

    def font(self, setfont):
        self.font = setfont

    def transform(self, myDraw):
        for i in myDraw:
            i[0] = self.ww * (i[0] - self.xmin)/(self.xmax-self.xmin)
            i[1] = self.wh * (i[1] - self.ymax)/(self.ymin-self.ymax)           
        return myDraw
            
    def area(self, xmin,xmax,ymin,ymax):
        
        if xmin==xmax:
            raise "<woyDraw - area> Fehler - xmin darf nicht gleich xmax sein!"
        else:
            self.xmin = xmin
            self.xmax = xmax
        if ymin==ymax:
            raise "<woyDraw - area> Fehler - ymin darf nicht gleich ymax sein!"
        else:
            self.ymin = ymin
            self.ymax = ymax

    def show(self):
        self.tk.wm_title(self.title)
        self.board = Canvas(self.tk,relief=SUNKEN, bd=2, width=self.ww, height=self.wh)
        self.board.pack(fill=BOTH)
        Rectangle(self.board, (0,0), (self.ww,self.wh), fill="white", width=1)
        b = Button(self.tk, text="Close", font=self.font, command = self.close )
        b.pack()

    def draw(self,myDraw,myColor,myWidth):
        myDraw2 = self.transform(myDraw)
        Line(self.board,myDraw2,width=myWidth,fill=myColor)

    def rawdraw(self,myDraw,myColor,myWidth):
        Line(self.board,myDraw,width=myWidth,fill=myColor)

# End Draw

def timeStamp():
    """Returns a String containing the current date and time"""
    
    timeSinceEpoch = time.time() #Seconds since 1.1.1970 00:00 o'clock
    t = time.localtime(timeSinceEpoch) #structured time object
    t = str(t.tm_mday)+'.'+str(t.tm_mon)+'.'+str(t.tm_year)+' '+str(t.tm_hour)+':'+str(t.tm_min)+':'+str(t.tm_sec) #string containing date current date and time

    return t    

def degree(x):
    """Berechnet Winkelgrad aus Radiant"""
    y = 180*x/pi
    return y

def sindeg(x):
    """Sinusfunktion als Funktion des Winkels"""
    xx = x*pi/180.0
    return sin(xx)

def cosdeg(x):
    """Cosinusfunktion als Funktion des Winkels"""
    xx = x*pi/180.0
    return cos(xx)

def frange(start, end=None, inc=1.0):
    """Eine Range-Funktion für Gleitpunktzahlen"""
    "frange recipe from python cookbook page 28"
    if end==None:
        end = start + 0.0
        start = 0.0
    assert inc

    L=[]
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)

    return L

class WoyGraph:
    """Klasse zum Zeichnen von Linien"""

    def __init__(self,xpix,ypix):
        self.pad = None
        self.xpix = xpix
        self.ypix = ypix
    
    def window(self,xmin,xmax,ymin,ymax,title = "Drawing-Window"):
        """Erzeugt ein Zeichenfenster"""
        myfont = "Arial 12 bold"
        self.pad = woyDraw(self.xpix,self.ypix)
        self.pad.font(myfont)
        self.pad.settitle(title)
        self.pad.show()
        self.pad.area(xmin,xmax,ymin,ymax)

    def line(self,x1,y1,x2,y2,colour,thickness):
        """Zeichnet eine Linie"""
        self.pad.draw([[x1,y1],[x2,y2]],colour,thickness)

def animation(xmin,xmax,ymin,ymax,displ,title="Animation",colors="no",allframes="no",thickness= 4):
    """Erzeugt eine einfache Animation"""
    # Oeffnet ein Grafikfenster mit 640*640 Pixeln
    graphics = WoyGraph(640,640)
    graphics.window(xmin,xmax,ymin,ymax,title=title)
    # Ermittlung der Feldlaengen
    ndis = len(displ)-3
    nlen = len(displ[0])
    # Check auf ungleiche Feldlaenge
    for i in displ:
        if len(i)!=nlen:
            print "Fehler in Animation: Sublisten müssen die gleiche Länge aufweisen!"
            raise "Error in Animation!"        
    farben = [ 'black', 'blue', 'red', 'green', 'yellow']
    # Zeichnen der Linien
    for i in range(1):
        for j in range(nlen):
            i=0
            for k in range(0,ndis,2):
                farbe = 'black'
                if colors == 'yes':
                    farbe = farben[i]
                    i=i+1
                    if i==len(farben)-1:
                        i = 0
                graphics.line(displ[k][j],displ[k+1][j],displ[k+2][j],displ[k+3][j],farbe,thickness)
            f = raw_input("Bitte die Return-Taste drücken!")
            for k in range(ndis):
                if allframes=='no':
                    graphics.line(displ[k][j],displ[k+1][j],displ[k+2][j],displ[k+3][j],"white",thickness)      



# Finite Element Analysis of Spring Assemblies
#
class SpringFem:
    """Finite Element Analysis Of A System Of Linear Springs"""

    def __init__(self, Nodes, Springs,Restraints,Forces,name):
        """init contains the complete solution procedure"""
        self.name = name
        self.time = timeStamp()

        # Check the input deck
        Nodes = self.check(Nodes, Springs,Restraints,Forces)
        self.Springs = Springs[:]
        self.Restraints = Restraints[:]
        self.Forces = Forces[:]

        # Partition the displacement vector x
        self.partition(Nodes,Restraints)

        # Assembly of overall stiffness matrix KS
        self.assemble(Springs)

        # Solve the system
        self.solve()

        # Print input deck
        self.printInput()

        # Store results in a text file
        self.exportHTML()

    def partition(self,Nodes,Restraints):
        """partition creates submatrices and subvectors from
        the system stiffness matrix"""

        # Dimension of system stiffness matrix
        self.n = len(Nodes)
        # Dimension of given displacements (restraints)
        self.g = len(Restraints)
        # Dimension of unknown displacements
        self.u = self.n - self.g
        # Create zero system stiffness matrix
        self.KS = zeros([self.n,self.n])
        # Create zero vector xg
        self.XG = zeros([self.g,1])
        # Create zero vector fg
        self.FG = zeros([self.u,1])
        # Create overall displacement vectors as lists
        xu = Nodes[:] #shallow copy
        xg = []
        for i in Restraints:
            xu.remove(i[0])
            xg.append(i[0])
        self.Nodes = xu + xg
        self.xu = xu
        self.xg = xg
        # Create numerical vector self.XG
        for i in Restraints:
            self.XG[Restraints.index(i)]=i[1]
        # Create overall force vector (numerical)
        LoadedNodes = []
        LoadValues = []
        Loads = []
        for i in self.Forces:
            LoadedNodes.append(i[0])
            LoadValues.append(i[1])
        for i in xu:
            f = 0.0
            if i in LoadedNodes:
                f = LoadValues[LoadedNodes.index(i)]
            Loads.append(f)
        for i in Loads:
            ind = Loads.index(i)
            self.FG[ind] = i

    def assemble(self,Springs):
        """assemble creates the overall system stiffness matrix KS"""

        # Assembly of overall stiffness matrix KS
            
        for i in Springs:
                fn = i[1]
                sn = i[2]
                sv = i[3]
                indfn = self.Nodes.index(fn)
                indsn = self.Nodes.index(sn)
                self.KS[indfn][indfn] = self.KS[indfn][indfn] + sv
                self.KS[indsn][indsn] = self.KS[indsn][indsn] + sv
                self.KS[indfn][indsn] = self.KS[indfn][indsn] - sv
                self.KS[indsn][indfn] = self.KS[indsn][indfn] - sv

        # Find the partitioned matrices Kred, A, B and C

        self.Kred = asmatrix(self.KS[0:self.u,0:self.u])
        self.C = asmatrix(self.KS[self.u:self.n,self.u:self.n])
        self.A = asmatrix(self.KS[0:self.u,self.u:self.n])
        self.B = asmatrix(self.KS[self.u:self.n,0:self.u])

    def solve(self):
        """solve solves the system using numpy module"""
            
        self.XU = self.Kred.I*(self.FG - self.A*self.XG)
        self.FU = self.B*self.XU + self.C*self.XG

    def printNodes(self):
        """printNodes print the nodes"""
        print
        print line
        print "Nodes"
        print line
        for i in self.Nodes:
            print i, " ",
        print
        print line

    def printSprings(self):
        """printSprings prints the springs and the spring properties"""
        print line
        print "Spring Elements"
        print line
        print "Label  |  Node1  |  Node2  |  Stiffness"
        print line       
        for i in self.Springs:
            print " %8d  |  %11d  |  %11d  |  %8.4f" % (i[0],i[1],i[2],i[3])
        print

    def printRestraints(self):
        """printRestraints prints the restraints acting on nodes"""
        print line
        print "Restraints"
        print line
        print "Node  | Displacement"
        print line       
        for i in self.Restraints:
            print " %8d  |  %8.3f  " % (i[0],i[1])
        print
            
    def printForces(self):
        """printForces prints the forces acting on the nodes"""
        print line
        print "Forces"
        print line
        print "Node  | Force value"
        print line       
        for i in self.Forces:
            print " %8d  |  %8.3f  " % (i[0],i[1])
        print

    def printKe(self):
        """printKe prints the element stiffness matrix"""
        print line
        print "Element stiffness matrices (springs)"
        print line
        print
        for i in self.Springs:
            print "Spring element: ", i[0]
            s = i[3]
            print " %12.4f  %12.4f " % (s, -s)
            print " %12.4f  %12.4f " % ( -s, s)
            print

    def printKS(self):
        """printKe prints the system stiffness matrix KS"""
        print line
        print "System Stiffness Matrix (KS):"
        print line
        print
        print self.KS
        print

    def info(self):
        """Info prints information about the number of equations,
        the number of variables and the unknowns"""

        print "System name"
        print line
        print self.name
        print line
        print "Date and time"
        print line
        print self.time
        print line
        print "System information"
        print line
        print "Dimension of system stiffness matrix (n)   : ",self.n
        print "Dimension of given displacements (g)        : ",self.g
        print "Dimension of unknown displacements (u): ",self.u
        print

    def check(self,Nodes, Springs,Restraints,Forces):
        """Check performs some test"""

        # Delete nodes which are defined twice

        NewNodes = []
        for i in Nodes:
            if i not in NewNodes:
                NewNodes.append(i)
            else:
                print
                print "Warning in method check: node ",i," is defined twice in nodelist!"
                print "It will be removed automatically!"
            
        # For Springs: check if node labels are in node list
            
        for i in Springs:
            if i[1] not in Nodes:
                print line
                print "******* ERROR *******"
                print line
                print "in Springs:"
                print "First node ", i[1]," is not in nodelist for spring ",i[0]
                raise
            if i[2] not in Nodes:
                print line
                print "******* ERROR *******"
                print line
                print "in Springs:"
                print "Second node ", i[2]," is not in nodelist for spring ",i[0]
                raise

        # For Restraints: check if node labels are in node list

        for i in Restraints:
            if i[0] not in Nodes:
                    print line
                    print "******* ERROR *******"
                    print line
                    print "in Restraints:"
                    print "Node ", i[0]," is not in nodelist for restraint ",i
                    raise

        # For Forces: check if node labels are in node list

        for i in Forces:
            if i[0] not in Nodes:
                print line
                print "******* ERROR *******"
                print line
                print "in Forces:"
                print "Node ", i[0]," is not in nodelist for force ",i
                raise

        return NewNodes

    def printInput(self):
        """printInput prints all entities of the input deck"""
        print line
        print "FEM Spring Analysis - Input Deck"
        print line
        print
        self.info()
        self.printNodes()
        self.printSprings()
        self.printKe()
        self.printKS()
        self.printRestraints()
        self.printForces()

    def printResults(self):
        """printResults prints out the results of the simulation"""
        # Overall output
        print line
        print "FEM Spring Analysis - Output of Results"
        print line
        print
        print line
        print "Displacements"
        print line
        print
        j = 0
        for i in self.XU:
            np = self.xu[j]
            print " %8d  |  %8.4f  " % (np, float(i))
            j += 1
        print line
        print "Forces"
        print line
        print
        j = 0 
        for i in self.FU:
            np = self.xg[j]
            print " %8d  |  %8.4f  " % (np, float(i))
            j += 1

    def exportHTML(self):
        exportFile = open('Results_'+self.name+'.xhtml','w')
        
        #doctype declaration
        doctype = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1 plus MathML 2.0//EN"  '
        doctype += '"http://www.w3.org/Math/DTD/mathml2/xhtml-math11-f.dtd">\n'
        exportFile.write(doctype)
        
        #xhtml document
        htmlStartTag = '<html xmlns="http://www.w3.org/1999/xhtml">\n\n'
        exportFile.write(htmlStartTag)
        
        #head
        headStartTag = '<head>\n\t<title>'+self.name+'</title>\n'
        exportFile.write(headStartTag)
            
        #CSS
        styleStartTag = '\t<style type="text/css">\n\n'
        exportFile.write(styleStartTag)

        #global settings
        table = '\t\t table { text-align: center;\n'
        table += '\t\t\t }\n\n'
        exportFile.write(table)

        #Class "Input"
        all = '\t\t.input { float: left;\n'
        all += '\t\t\t }\n\n'
        exportFile.write(all)
        
        div = '\t\t.input > div{ float: left;\n'
        div += '\t\t\t margin: 20px;\n'
        div += '\t\t\t padding: 10px;\n'
        div += '\t\t\t }\n\n'
        exportFile.write(div)

        #Class "Results"
        all = '\t\t.results { margin: 30px;\n'
        all += '\t\t\t float: right;\n'
        all += '\t\t\t border-style: solid;\n'
        all += '\t\t\t padding: 10px;\n'
        all += '\t\t\t }\n\n'
        exportFile.write(all)

        #End CSS
        styleEndTag = '\t</style>\n\n'
        exportFile.write(styleEndTag)

        #End head        
        headEndTag = '</head>\n\n'
        exportFile.write(headEndTag)        
        
        #body
        bodyStartTag = '<body>\n\n'
        exportFile.write(bodyStartTag)

        #header
        header = '<div class="header">\n\t<h2>Results for '+self.name+'</h2>\n\t<hr />\n\t<p><em>'+self.time+'</em></p>\n</div>\n\n'
        exportFile.write(header)

        #input information
        inputInfoStartTag = '<div class="input">\n\n'
        exportFile.write(inputInfoStartTag)

        #groupe one
        groupeOneStartTag = '\t<div class="groupOne">\n\n'
        exportFile.write(groupeOneStartTag)

        #system information
        systemInfo = '\t\t<div id="information">\n\t\t\t<h3>System information</h3>\n'
        systemInfo += '\t\t\t<p>Dimension of system stiffness matrix (n) : '+str(self.n)+'</p>\n'
        systemInfo += '\t\t\t<p>Dimension of given displacements (g)     : '+str(self.g)+'</p>\n'
        systemInfo += '\t\t\t<p>Dimension of unknown displacements (u)   : '+str(self.u)+'</p>\n\t\t</div>\n\n'
        exportFile.write(systemInfo)

        #Nodes
        nodesInput = '\t\t<div id="nodes">\n\t\t\t<h4>Nodes</h4>\n\t\t\t<p>'
        for node in self.Nodes:
            nodesInput += str(node)+' '
        
        nodesInput += '</p>\n\t\t</div>\n\n'
        exportFile.write(nodesInput)                

        #Springs
        springs = '\t\t<div id="springs">\n\t\t\t<h4>Spring Elements</h4>\n\t\t\t<table>\n'
        springs += 4*'\t'+'<tr>\n'
        springs += 5*'\t'+'<th>Label</th>\n'
        springs += 5*'\t'+'<th>Node 1</th>\n'
        springs += 5*'\t'+'<th>Node 2</th>\n'
        springs += 5*'\t'+'<th>Stiffness</th>\n'
        springs += 4*'\t'+'</tr>\n'
        
        for spring in self.Springs:
            springs += 4*'\t'+'<tr>\n' 
            for info in spring:
                springs += 5*'\t'+'<td>'+str(info)+'</td>\n'

            springs += 4*'\t'+'</tr>\n'
        springs += '\t\t\t</table>\n\t\t</div>\n'
        exportFile.write(springs)

        #end groupe one
        groupeOneEndTag = '\t</div>\n\n'
        exportFile.write(groupeOneEndTag)

        #groupe two
        groupeTwoStartTag = '\t<div class="groupTwo">\n\n'
        exportFile.write(groupeTwoStartTag)        

        #element stiffness matrices (with MathML)
        esmTag = '\t\t<div id="ESM">\n\t\t\t<h4>Element stiffness matrices (springs)</h4>\n'
        mathMLStartTag = '\t\t\t<math xmlns="http://www.w3.org/1998/Math/MathML">\n'
        esmTag += mathMLStartTag 

        esmTag += '\t\t\t<mtable>\n'
        counter = 1
        
        for spring in self.Springs:
            if (counter % 3) == 1:
                esmTag += 4*'\t'+'<mtr>\n'
            
            esmTag += 5*'\t'+'<mtd>\n'
            esmTag += 6*'\t'+'<mover>\n'
            esmTag += 7*'\t'+'<mrow>\n'
            esmTag += 8*'\t'+'<mo>[</mo>\n'
            esmTag += 9*'\t'+'<mtable>\n'            
            esmTag += 9*'\t'+'<mtr>\n'
            esmTag += 10*'\t'+'<mtd><mn>'+str(spring[3])+'</mn></mtd>\n'
            esmTag += 10*'\t'+'<mtd><mn>'+str(-spring[3])+'</mn></mtd>\n'
            esmTag += 9*'\t'+'</mtr>\n'

            esmTag += 9*'\t'+'<mtr>\n'
            esmTag += 10*'\t'+'<mtd><mn>'+str(-spring[3])+'</mn></mtd>\n'
            esmTag += 10*'\t'+'<mtd><mn>'+str(spring[3])+'</mn></mtd>\n'
            esmTag += 9*'\t'+'</mtr>\n'
            esmTag += 8*'\t'+'</mtable>\n\n'
            esmTag += 8*'\t'+'<mo>]</mo>\n'
            esmTag += 7*'\t'+'</mrow>\n'
            esmTag += 7*'\t'+'<mi>Spring element '+str(spring[0])+'</mi>\n'
            esmTag += 6*'\t'+'</mover>\n'
            esmTag += 5*'\t'+'</mtd>\n'

            if (counter % 3) == 0:
                esmTag += 4*'\t'+'</mtr>\n'
            counter += 1            

        esmTag += 4*'\t'+'</mtr>\n'
        esmTag += 4*'\t'+'</mtable>\n\t\t\t</math>\n\t\t</div>\n'
        exportFile.write(esmTag)

        #System stiffness matrix (with MathML)
        ssmTag = '\t\t<div id="SSM">\n\t\t\t<h4>System stiffness matrices (springs)</h4>\n'
        mathMLStartTag = '\t\t\t<math xmlns="http://www.w3.org/1998/Math/MathML">\n'

        ssmTag += mathMLStartTag 
        ssmTag += 4*'\t'+'<mrow>\n'
        ssmTag += 4*'\t'+'<mo>[</mo>\n'
        ssmTag += 5*'\t'+'<mtable>\n'        
        
        for row in self.KS:
            ssmTag += 6*'\t'+'<mtr>\n'
            for column in row:
                ssmTag += 7*'\t'+'<mtd><mn>'+str(column)+'</mn></mtd>\n'
            ssmTag += 6*'\t'+'</mtr>\n'

        ssmTag += 5*'\t'+'</mtable>\n\n'
        ssmTag += 4*'\t'+'<mo>]</mo>\n'
        ssmTag += 4*'\t'+'</mrow>\n'
        ssmTag += '\t\t\t</math>\n'
        ssmTag += '\t\t</div>\n'
        exportFile.write(ssmTag)

        #end groupe two
        groupeTwoEndTag = '\t</div>\n\n'
        exportFile.write(groupeTwoEndTag)

        #groupe three
        groupeThreeStartTag = '\t<div class="groupThree">\n\n'
        exportFile.write(groupeThreeStartTag)

        #Restraints
        restraintsInput = '\t\t<div id="restraints">\n\t\t\t<h4>Restraints</h4>\n\t\t\t<table>\n'
        restraintsInput += 4*'\t'+'<tr>\n'
        restraintsInput += 5*'\t'+'<th>Node</th>\n'
        restraintsInput += 5*'\t'+'<th>Displacement</th>\n'
        restraintsInput += 4*'\t'+'</tr>\n'

        for restraint in self.Restraints:
            restraintsInput += 4*'\t'+'<tr>\n' 
            for info in restraint:
                restraintsInput += 5*'\t'+'<td>'+str(info)+'</td>\n'

            restraintsInput += 4*'\t'+'</tr>\n'

        restraintsInput += '\t\t\t</table>\n\t\t</div>\n'
        exportFile.write(restraintsInput)

        #Forces
        forcesInput = '\t\t<div id="forces">\n\t\t\t<h4>Forces</h4>\n\t\t\t<table>\n'
        forcesInput += 4*'\t'+'<tr>\n'
        forcesInput += 5*'\t'+'<th>Node</th>\n'
        forcesInput += 5*'\t'+'<th>Force-Value</th>\n'
        forcesInput += 4*'\t'+'</tr>\n'

        for force in self.Forces:
            forcesInput += 4*'\t'+'<tr>\n' 
            for info in force:
                forcesInput += 5*'\t'+'<td>'+str(info)+'</td>\n'

            forcesInput += 4*'\t'+'</tr>\n'

        forcesInput += '\t\t\t</table>\n\t\t</div>\n'
        exportFile.write(forcesInput)

        #end groupe three
        groupeThreeEndTag = '\t</div>\n\n'
        exportFile.write(groupeThreeEndTag)
                            
        #end input information
        inputInfoEndTag = '</div>\n\n'
        exportFile.write(inputInfoEndTag)

        #results
        resultsStartTag = '<div class="results">\n\n\t<h3>Results</h3>\n\n'
        exportFile.write(resultsStartTag)

        #Displacements
        displacements = '\t<div id="displacements">\n\t\t<h4>Displacements</h4>\n\t\t<table>\n'
        displacements += 3*'\t'+'<tr>\n'
        displacements += 4*'\t'+'<th>Node</th>\n'
        displacements += 4*'\t'+'<th>Displacement</th>\n'
        displacements += 3*'\t'+'</tr>\n'

        XU = copy(self.XU)
        xu = copy(self.xu)
        
        j = 0
        for displacement in XU:
            np = xu[j]
            displacements += 3*'\t'+'<tr>\n'
            displacements += 4*'\t'+'<td>'+str(np)+'</td>\n'
            displacements += 4*'\t'+'<td>'+str(displacement[0])+'</td>\n'
            displacements += 3*'\t'+'</tr>\n'
            j += 1

        displacements += '\t\t</table>\n\t</div>\n'
        exportFile.write(displacements)

        #Forces
        forces = '\t<div id="forces">\n\t\t<h4>Forces</h4>\n\t\t<table>\n'
        forces += 3*'\t'+'<tr>\n'
        forces += 4*'\t'+'<th>Node</th>\n'
        forces += 4*'\t'+'<th>Force</th>\n'
        forces += 3*'\t'+'</tr>\n'

        FU = copy(self.FU)
        xg = copy(self.xg)
        
        j = 0
        for force in FU:
            np = xg[j]
            forces += 3*'\t'+'<tr>\n'
            forces += 4*'\t'+'<td>'+str(np)+'</td>\n'
            forces += 4*'\t'+'<td>'+str(force[0])+'</td>\n'
            forces += 3*'\t'+'</tr>\n'
            j += 1

        forces += '\t\t</table>\n\t</div>\n'
        exportFile.write(forces)        

        #end results        
        resultsEndTag = '</div>\n\n'
        exportFile.write(resultsEndTag)
        
        #end body               
        bodyEndTag = '</body>\n'
        exportFile.write(bodyEndTag)

        #end xhtml document                
        htmlEndTag = '</html>'
        exportFile.write(htmlEndTag)
        
        exportFile.close()