from pyray import *

listMainMenu = ["Game","Settings","About","Quit"]
listLevelMenu = ["Game 1","Game 2","Game 3"]
listLevelMenuAbout = ["Game 1 instruction","Game 2 instruction","Game 3 instruction"]
listSettingMenu = ["Color","Reset","Mute"]
listAboutMenu = ["Ajesh","Gaurangi","Subhranil","About Me"]
listAboutMenuAbout = ["Name : Ajesh Sharma\nRegistration Number : RA2211026010383\nContribution : Coding (in Python)",
                  "Name : Gaurangi Rohilla\nRegistration Number : RA2211026010392\nContribution : GUI & Database",
                  "Name : Subhranil Ghosh\nRegistration Number : RA2211026010385\nContribution : Coding (in Java)",
                  "Made For : Advanced Programming Practice\nProgramming Language : Python\nSemester : 3rd\nLicense : MIT"]
listColors = [["Peach",Color(120,66,89,255),Color(185,78,86,255)],
              ["Purple",Color(43,18,76,255), Color(133,79,108,255)],
              ["Terra",Color(30,31,70,255), Color(202,49,63,255)],
              ["Ocean",Color(7,46,51,255) , Color(15,150,156,255)],
              ["Discord",Color(33,34,44,255),Color(98,114,164,255)]]


colorOption = 2
ColorF = listColors[colorOption][2]
ColorB = listColors[colorOption][1]
lineThick = 5
font = 50
rec = Rectangle(0,150,1280,720-150)
subrec = Rectangle(rec.x,rec.y,int(rec.width/4),rec.height)
suprec = Rectangle(rec.x + int(rec.width/4),rec.y,int(rec.width/4),rec.height)
desrec = Rectangle(rec.x + int(rec.width/2),rec.y,int(rec.width/2),rec.height)
button = 150

mainSection = -1
levelSection = -1
settingSection = -1
aboutSection = -1
def mainMenu():
    global mainSection,rec,ColorF
    draw_text("MAZE RUNNER",int((1280 - measure_text("MAZE RUNNER",70))/2),int((150 - 70)/2),70,ColorF)
    for i in range(len(listMainMenu)):
        temp = Rectangle(subrec.x,subrec.y + i*int(subrec.height/len(listMainMenu)),subrec.width,int(subrec.height/len(listMainMenu)))
        if check_collision_point_rec(get_mouse_position(),temp):
            if (is_mouse_button_down(0)):
                #selected
                drawMS(f"{listMainMenu[i]}",temp)
                mainSection = i
            else:
                #hover
                drawMH(f"{listMainMenu[i]}",temp)
        else:
            #normal
            drawMN(f"{listMainMenu[i]}",temp)
            
        #selection logic
        if mainSection == 0:
            levelMenu()
        elif mainSection == 1:
            settingMenu()
        elif mainSection == 2:
            aboutMenu()
        elif mainSection == 3:
            quitMenu()
            
def levelMenu():
    global levelSection
    for i in range(len(listLevelMenu)):
        temp = Rectangle(suprec.x,suprec.y + i*int(suprec.height/len(listLevelMenu)),suprec.width,int(suprec.height/len(listLevelMenu)))
        if check_collision_point_rec(get_mouse_position(),temp):
            if (is_mouse_button_down(0)):
                #selected
                drawMS(f"{listLevelMenu[i]}",temp)
                levelSection = i
            else:
                #hover
                drawMH(f"{listLevelMenu[i]}",temp)
        else:
            #normal
            drawMN(f"{listLevelMenu[i]}",temp)
        if levelSection > -1:
            drawDES(desrec,levelSection,listLevelMenu,listLevelMenuAbout)
            playButton()
         
def settingMenu():
    global settingSection
    for i in range(len(listLevelMenu)):
        temp = Rectangle(suprec.x,suprec.y + i*int(suprec.height/len(listSettingMenu)),suprec.width,int(suprec.height/len(listSettingMenu)))
        if check_collision_point_rec(get_mouse_position(),temp):
            if (is_mouse_button_down(0)):
                #selected
                drawMS(f"{listSettingMenu[i]}",temp)
                settingSection = i
            else:
                #hover
                drawMH(f"{listSettingMenu[i]}",temp)
        else:
            #normal
            drawMN(f"{listSettingMenu[i]}",temp)
        if settingSection == 0:
            settingColor()
       
def aboutMenu():
    global aboutSection
    for i in range(len(listAboutMenu)):
        temp = Rectangle(suprec.x,suprec.y + i*int(suprec.height/len(listAboutMenu)),suprec.width,int(suprec.height/len(listAboutMenu)))
        if check_collision_point_rec(get_mouse_position(),temp):
            if (is_mouse_button_down(0)):
                #selected
                drawMS(f"{listAboutMenu[i]}",temp)

                aboutSection = i
            else:
                #hover
                drawMH(f"{listAboutMenu[i]}",temp)
             
        else:
            #normal
            drawMN(f"{listAboutMenu[i]}",temp)
        if aboutSection > -1:
            drawDES(desrec,aboutSection,listAboutMenu,listAboutMenuAbout)

#hover
def drawMH(a,r):
    global font
    draw_rectangle_lines_ex(r,lineThick,ColorF)
    draw_text(a,int(r.x + 10),int((r.height - font)/2 + r.y), font,ColorF)
     
#normal
def drawMN(a,r):
    global font
    draw_rectangle_lines_ex(r,int(lineThick/2),ColorF)
    draw_text(a,int(r.x + 10),int((r.height - font)/2 + r.y), font,ColorF)

#selected
def drawMS(a,r):
    global font
    draw_rectangle_rec(r,ColorF)
    draw_rectangle_lines_ex(r,lineThick,ColorF)
    draw_text(a,int(r.x + 10),int((r.height - font)/2 + r.y), font,ColorB)
    
def settingColor():
    global font,colorOption,ColorF,ColorB
    for i in range(len(listColors)):
        draw_rectangle(int(desrec.x),int(desrec.height/len(listColors))*i + int(desrec.y),int(desrec.width/2),int(desrec.height/len(listColors)),listColors[i][1])
        draw_rectangle(int(desrec.x)+ int(desrec.width/2),int(desrec.height/len(listColors))*i + int(desrec.y),int(desrec.width/2),int(desrec.height/len(listColors)),listColors[i][2])
        draw_text(f"{listColors[i][0]}",int(desrec.x),int(desrec.height/len(listColors))*i + int(desrec.y), font*2,BLACK)
        if check_collision_point_rec(get_mouse_position() ,Rectangle(int(desrec.x),int(desrec.height/len(listColors))*i + int(desrec.y),int(desrec.width),int(desrec.height/len(listColors)))):
            draw_rectangle_lines_ex(Rectangle(int(desrec.x),int(desrec.height/len(listColors))*i + int(desrec.y),int(desrec.width),int(desrec.height/len(listColors))),5,WHITE)
            if (is_mouse_button_down(0)):
                colorOption = i
                ColorF = listColors[colorOption][2]
                ColorB = listColors[colorOption][1]

def playButton():
    temp = Rectangle(int(desrec.x),int(desrec.height - 150 + desrec.y),int(desrec.width),150)
    if check_collision_point_rec(get_mouse_position(),temp):
        if (is_mouse_button_down(0)):
            #selected
            drawMS("Play",temp)
            
        else:
            #hover
            drawMH("Play",temp)
    else:
        #normal
        drawMN("Play",temp)

def drawDES(r,i,t1,t2):
    #draw_rectangle_lines_ex(r,lineThick,ColorF)
    draw_text(f"{t1[i]}",int(r.x),int(r.y + 5),font*2,ColorF)
    draw_text(f"{t2[i]}",int(r.x),int(r.y + font*3 + font),int(font/2),ColorF)