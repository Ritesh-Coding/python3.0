import random
posUp = [[0,0,0],[0,0,'#'],['*',0,0],[0,0,0],[0,0,0],[0,0,0]]
posLeft = [[0,'#',0,0,0,0],[0,0,0,0,0,0],[0,0,'*',0,0,0]]
posRight = [[0,0,0,'*',0,0],[0,0,0,0,0,0],[0,0,0,0,'#',0]]
posDown = [[0,0,0],[0,0,0],[0,0,0],[0,0,'*'],['#',0,0],[0,0,0]]
sixCount = 0
posWin = [['$','$','$'],['$','$','$'],['$','$','$']]
instantStartA = False
instantStartB = False
instantStartC = False
instantStartD = False
a1Initialized = False
a2Initialized = False
a3Initialized = False
a4Initialized = False
b1Initialized = False
b2Initialized = False
b3Initialized = False
b4Initialized = False
c1Initialized = False
c2Initialized = False
c3Initialized = False
c4Initialized = False
d1Initialized = False
d2Initialized = False
d3Initialized = False
d4Initialized = False
def ludoGameUI():

    for row1 in range(6):
        #upper row print        
        for col1 in range(6):
            print("-",end="     ")
        for item in posUp[row1]:
            print(item,end="     ")
        for col2 in range(6):
            print("-",end="     ")
            
        print("\n\n",end="")
    for i in range(3):
        for item in posLeft[i]:
            print(item,end="     ")
        for item in posWin[i]:
            print(item,end="     ")
        for item in posRight[i]:
            print(item,end="     ")
        print("\n\n",end="")
        
    for row1 in range(6):
        #upper row print
        
        for col1 in range(6):
            print("-",end="     ")
        for item in posDown[row1]:
            print(item,end="     ")
        for col2 in range(6):
            print("-",end="     ")
            
        print("\n\n",end="")


#We have Total 4 player

#player1 players
a1Index = 0
a2Index = 0
a3Index = 0
a4Index = 0

#player2 players
b1Index = 0
b2Index = 0
b3Index = 0
b4Index = 0

#player3 players
c1Index = 0
c2Index = 0
c3Index = 0
c4Index = 0

#player4 players
d1Index = 0
d2Index = 0
d3Index = 0
d4Index = 0

    
def ismyPlayer(myExistingCookie,newCookie,player):

    global a1Index
    global a2Index
    global a3Index
    global a4Index
    global b1Index
    global b3Index
    global b4Index
    global b2Index
    global c1Index
    global c2Index
    global c4Index
    global c3Index
    global d1Index
    global d2Index
    global d3Index
    global d4Index
    
    if player == "player1":
        if myExistingCookie == 0:
            return 'empty'
        if myExistingCookie == 'a1' or myExistingCookie == 'a2' or myExistingCookie == 'a3' or myExistingCookie == 'a4':
            return 'true'
        else:
            myEnemyString = myExistingCookie+"Index"
            myEnemyIsInitialized = myExistingCookie+"Initialized"
                         
            globals()[myEnemyIsInitialized] = False               
            globals()[myEnemyString] = 0    
           
            if len(myExistingCookie)>2:
                    return 'true'
            else:
                    
                    return 'false'   
            
        
    if player == "player2":
        if myExistingCookie == 0:
            return 'empty'
        if myExistingCookie == 'b1' or myExistingCookie == 'b2' or myExistingCookie == 'b3' or myExistingCookie == 'b4':
            return 'true'
        else:
            myEnemyString = myExistingCookie + "Index"
            myEnemyIsInitialized = myExistingCookie + "Initialized"           
                          
            globals()[myEnemyIsInitialized] = False                
            globals()[myEnemyString] = 0               
            removeSpecificCharacterFromSafePosition(posLists,myExistingCookie)
            if len(myExistingCookie)>2:
                return 'true'
            else:
                return 'false'
        
    if player == "player3":
        if myExistingCookie == 0:
            return 'empty'
        if myExistingCookie == 'c1' or myExistingCookie == 'c2' or myExistingCookie == 'c3' or myExistingCookie == 'c4':
            return 'true'
        else:
            myEnemyString=myExistingCookie+"Index"
            myEnemyIsInitialized=myExistingCookie+"Initialized"
            
            globals()[myEnemyIsInitialized]=False               
            globals()[myEnemyString] = 0             
               
            if len(myExistingCookie)>2:
                return 'true'
            else:
                return 'false'
        
    if player == "player4":
        if myExistingCookie==0:
            return 'empty'
        if myExistingCookie=='d1' or myExistingCookie=='d2' or myExistingCookie=='d3' or myExistingCookie=='d4':
            return 'true'
        else:
            myEnemyString=myExistingCookie+"Index"
            myEnemyIsInitialized=myExistingCookie+"Initialized"
                            
            globals()[myEnemyIsInitialized]=False                
            globals()[myEnemyString] = 0           
                
            if len(myExistingCookie)>2:
                return 'true'
            else:
                return 'false'

def mapping(playerIndex,mylist,replaceBy):     #player1
    
    if playerIndex==0:              #top one
        mylist[1][2]+=replaceBy
        ludoGameUI()
    elif playerIndex==1:
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=myExistingCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][2]=replaceBy 
        ludoGameUI()
    elif playerIndex==2:
        myExistingCookie=mylist[3][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[3][2]+=replaceBy      
        elif result=="false":
            mylist[3][2]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[3][2]=replaceBy
        ludoGameUI()
    elif playerIndex==3:
        myExistingCookie=mylist[4][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[4][2]+=replaceBy      
        elif result=="false":
            mylist[4][2]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[4][2]=replaceBy
        ludoGameUI()
    elif playerIndex==4:
        myExistingCookie=mylist[5][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[5][2]+=replaceBy      
        elif result=="false":
            mylist[5][2]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[5][2]=replaceBy
        ludoGameUI()
    elif playerIndex==5:
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==6:                #right one
        myExistingCookie=mylist[0][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][1]+=replaceBy      
        elif result=="false":
            mylist[0][1]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][1]=replaceBy
        ludoGameUI()
    elif playerIndex==7:
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][2]=replaceBy
        ludoGameUI()  
    elif playerIndex==8:        
        mylist[0][3]+=replaceBy        
        ludoGameUI()
    elif playerIndex==9:
        myExistingCookie=mylist[0][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][4]+=replaceBy      
        elif result=="false":
            mylist[0][4]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][4]=replaceBy
        ludoGameUI()
    elif playerIndex==10:
        myExistingCookie=mylist[0][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][5]+=replaceBy      
        elif result=="false":
            mylist[0][5]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][5]=replaceBy
        ludoGameUI()
    elif playerIndex==11:
        myExistingCookie=mylist[1][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[1][5]+=replaceBy      
        elif result=="false":
            mylist[1][5]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[1][5]=replaceBy
        ludoGameUI()
    elif playerIndex==12:
        myExistingCookie=mylist[2][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][5]+=replaceBy      
        elif result=="false":
            mylist[2][5]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][5]=replaceBy
        ludoGameUI()
    elif playerIndex==13:
        mylist[2][4]+=replaceBy
        ludoGameUI()
    elif playerIndex==14:
        myExistingCookie=mylist[2][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][3]+=replaceBy      
        elif result=="false":
            mylist[2][3]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][3]=replaceBy
        ludoGameUI()
    elif playerIndex==15:
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][2]=replaceBy
        ludoGameUI()
    elif playerIndex==16:
        myExistingCookie=mylist[2][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][1]+=replaceBy      
        elif result=="false":
            mylist[2][1]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][1]=replaceBy
        ludoGameUI()
    elif playerIndex==17:
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][0]=replaceBy
        ludoGameUI()
    elif playerIndex ==18:       #down
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][2]=replaceBy
        ludoGameUI()
    elif playerIndex ==19:
        myExistingCookie=mylist[1][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[1][2]+=replaceBy      
        elif result=="false":
            mylist[1][2]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[1][2]=replaceBy
        ludoGameUI()
    elif playerIndex ==20:
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]+=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][2]=replaceBy
        ludoGameUI()
    elif playerIndex ==21:
        
        mylist[3][2]+=replaceBy
        ludoGameUI()
    elif playerIndex ==22:
        myExistingCookie=mylist[4][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[4][2]+=replaceBy      
        elif result=="false":
            mylist[4][2]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[4][2]=replaceBy
        ludoGameUI()
    elif playerIndex ==23:
        myExistingCookie=mylist[5][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[5][2]+=replaceBy      
        elif result=="false":
            mylist[5][2]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[5][2]=replaceBy
        ludoGameUI()
    elif playerIndex ==24:
        myExistingCookie=mylist[5][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[5][1]+=replaceBy      
        elif result=="false":
            mylist[5][1]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[5][1]=replaceBy
        ludoGameUI()
    elif playerIndex ==25:
        myExistingCookie=mylist[5][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[5][0]+=replaceBy      
        elif result=="false":
            mylist[5][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[5][0]=replaceBy
        ludoGameUI()
    elif playerIndex == 26:
        
        mylist[4][0]+=replaceBy
        ludoGameUI()
    elif playerIndex == 27:
        myExistingCookie=mylist[3][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[3][0]+=replaceBy      
        elif result=="false":
            mylist[3][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[3][0]=replaceBy
        ludoGameUI()
    elif playerIndex == 28:
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][0]=replaceBy
        ludoGameUI()
    elif playerIndex == 29:
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[1][0]=replaceBy
        ludoGameUI()
    elif playerIndex == 30:
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex == 31:  #left
        myExistingCookie=mylist[2][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][5]+=replaceBy      
        elif result=="false":
            mylist[2][5]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][5]=replaceBy
        ludoGameUI()
    elif playerIndex == 32:
        myExistingCookie=mylist[2][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][4]+=replaceBy      
        elif result=="false":
            mylist[2][4]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][4]=replaceBy
        ludoGameUI()
    elif playerIndex == 33:
        myExistingCookie=mylist[2][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][3]+=replaceBy      
        elif result=="false":
            mylist[2][3]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][3]=replaceBy
        ludoGameUI()
    elif playerIndex == 34:
        mylist[2][2]+=replaceBy
        ludoGameUI()
    elif playerIndex== 35:
        myExistingCookie=mylist[2][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][1]+=replaceBy      
        elif result=="false":
            mylist[2][1]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][1]=replaceBy
        ludoGameUI()
    elif playerIndex==36:
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[2][0]=replaceBy
        ludoGameUI()
    elif playerIndex==37:
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[1][0]=replaceBy
        ludoGameUI()
    elif playerIndex==38:
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==39:
        mylist[0][1]+=replaceBy
        ludoGameUI()
    elif playerIndex==40:
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][2]=replaceBy
        ludoGameUI()
    elif playerIndex==41:
        myExistingCookie=mylist[0][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][3]+=replaceBy      
        elif result=="false":
            mylist[0][3]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][3]=replaceBy
        ludoGameUI()
    elif playerIndex==42:
        myExistingCookie=mylist[0][4]
        newCookie=replaceBy        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][4]+=replaceBy      
        elif result=="false":
            mylist[0][4]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][4]=replaceBy
        ludoGameUI()
    elif playerIndex==43:
        myExistingCookie=mylist[0][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][5]+=replaceBy      
        elif result=="false":
            mylist[0][5]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][5]=replaceBy #again Up
        ludoGameUI()
    elif playerIndex==44:
        myExistingCookie=mylist[5][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[5][0]+=replaceBy      
        elif result=="false":
            mylist[5][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[5][0]=replaceBy
        ludoGameUI()
    elif playerIndex==45:
        myExistingCookie=mylist[4][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[4][0]+=replaceBy      
        elif result=="false":
            mylist[4][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[4][0]=replaceBy
        ludoGameUI()
    elif playerIndex==46:
        myExistingCookie=mylist[3][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[3][0]+=replaceBy      
        elif result=="false":
            mylist[3][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[3][0]=replaceBy
        ludoGameUI()
    elif playerIndex==47:
        mylist[2][0]+=replaceBy
        ludoGameUI()
    elif playerIndex==48:
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[1][0]=replaceBy
        ludoGameUI()
    elif playerIndex==49:
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==50:
        myExistingCookie=mylist[0][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player1")
        if result=="true":
            mylist[0][1]+=replaceBy      
        elif result=="false":
            mylist[0][1]=newCookie
            ludoGameUI()
            playerTurn("player1")
        else:
             mylist[0][1]=replaceBy
        ludoGameUI()
    elif playerIndex==51:
        if mylist[1][1]!=0:
            mylist[1][1]+=replaceBy
        else:
            mylist[1][1]=replaceBy
        ludoGameUI()
    elif playerIndex==52:
        if mylist[2][1]!=0:
            mylist[2][1]+=replaceBy
        else:
            mylist[2][1]=replaceBy
        ludoGameUI()
    elif playerIndex==53:
        if mylist[3][1]!=0:
            mylist[3][1]+=replaceBy
        else:
            mylist[3][1]=replaceBy
        ludoGameUI()
    elif playerIndex==54:
        if mylist[4][1]!=0:
            mylist[4][1]+=replaceBy
        else:
            mylist[4][1]=replaceBy
        ludoGameUI()
    elif playerIndex==55:
        if mylist[5][1]!=0:# if mylist[2][2]!=0 :              
        #     mylist[2][2]+=replaceBy                    
        # else:   
        #     mylist[2][2]=replaceBy 
            mylist[5][1]+=replaceBy
        else:
            mylist[5][1]=replaceBy
        ludoGameUI()
    elif playerIndex==56:           #win
         mylist[0][1]+=replaceBy
         ludoGameUI()
    else:
        print("Please enter a valid position")
    
def mapping2(playerIndex,mylist,replaceBy):
    if playerIndex==0:              #right one
        
        mylist[2][4]+=replaceBy
        ludoGameUI()
    elif playerIndex==1:
        myExistingCookie=mylist[2][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][3]+=replaceBy      
        elif result=="false":
            mylist[2][3]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][3]=replaceBy
        ludoGameUI()
    elif playerIndex==2:
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][2]=replaceBy
        ludoGameUI()
    elif playerIndex==3:
        myExistingCookie=mylist[2][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][1]+=replaceBy      
        elif result=="false":
            mylist[2][1]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][1]=replaceBy
        ludoGameUI()
    elif playerIndex==4:
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][0]=replaceBy
        ludoGameUI()
    elif playerIndex==5:            #down
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][2]=replaceBy
        ludoGameUI()
    elif playerIndex==6:            #down
        myExistingCookie=mylist[1][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[1][2]+=replaceBy      
        elif result=="false":
            mylist[1][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[1][2]=replaceBy
        ludoGameUI()
    elif playerIndex==7:            #down
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][2]=replaceBy
        ludoGameUI()
    elif playerIndex==8:            #down
        mylist[3][2]+=replaceBy
        ludoGameUI()
    elif playerIndex==9:            #down
        myExistingCookie=mylist[4][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[4][2]+=replaceBy      
        elif result=="false":
            mylist[4][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[4][2]=replaceBy
        ludoGameUI()
    elif playerIndex==10:            #down
        myExistingCookie=mylist[5][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[5][2]+=replaceBy      
        elif result=="false":
            mylist[5][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[5][2]=replaceBy
        ludoGameUI()
    elif playerIndex==11:            #down
        myExistingCookie=mylist[5][1]
        newCookie=replaceBy        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[5][1]+=replaceBy      
        elif result=="false":
            mylist[5][1]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[5][1]=replaceBy
        ludoGameUI()
    elif playerIndex==12:            #down
        myExistingCookie=mylist[5][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[5][0]+=replaceBy      
        elif result=="false":
            mylist[5][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[5][0]=replaceBy
        ludoGameUI()
    elif playerIndex==13:            #down
        mylist[4][0]+=replaceBy
        ludoGameUI()
    elif playerIndex==14:            #down
        myExistingCookie=mylist[3][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[3][0]+=replaceBy      
        elif result=="false":
            mylist[3][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[3][0]=replaceBy
        ludoGameUI()
    elif playerIndex==15:            #down
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][0]=replaceBy
        ludoGameUI()
    elif playerIndex==16:            #down
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[1][0]=replaceBy
        ludoGameUI()
    elif playerIndex==17:            #down
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==18:           #left
        myExistingCookie=mylist[2][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][5]+=replaceBy      
        elif result=="false":
            mylist[2][5]=newCookie
            ludoGameUI()
            playerTurn("player2")
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][5]=replaceBy
        ludoGameUI()
    elif playerIndex==19:           #left
        myExistingCookie=mylist[2][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][4]+=replaceBy      
        elif result=="false":
            mylist[2][4]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][4]=replaceBy
        ludoGameUI()
    elif playerIndex==20:           #left
        myExistingCookie=mylist[2][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][3]+=replaceBy      
        elif result=="false":
            mylist[2][3]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][3]=replaceBy
        ludoGameUI()
    elif playerIndex==21:           #left
        mylist[2][2]+=replaceBy
        ludoGameUI()
    elif playerIndex==22:           #left
        myExistingCookie=mylist[2][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][1]+=replaceBy      
        elif result=="false":
            mylist[2][1]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][1]=replaceBy
        ludoGameUI()
    elif playerIndex==23:           #left
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][0]=replaceBy
        ludoGameUI()
    elif playerIndex==24:           #left
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[1][0]=replaceBy
        ludoGameUI()
    elif playerIndex==25:           #left
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==26:           #left
        mylist[0][1]+=replaceBy
        ludoGameUI()
    elif playerIndex==27:           #left
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][2]=replaceBy
        ludoGameUI()
    elif playerIndex==28:           #left
        myExistingCookie=mylist[0][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][3]+=replaceBy      
        elif result=="false":
            mylist[0][3]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][3]=replaceBy
        ludoGameUI()
    elif playerIndex==29:           #left
        myExistingCookie=mylist[0][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][4]+=replaceBy      
        elif result=="false":
            mylist[0][4]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][4]=replaceBy
        ludoGameUI()
    elif playerIndex==30:           #left
        myExistingCookie=mylist[0][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][5]+=replaceBy      
        elif result=="false":
            mylist[0][5]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][5]=replaceBy
        ludoGameUI()
    elif playerIndex==31:           #up
        myExistingCookie=mylist[5][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[5][0]+=replaceBy      
        elif result=="false":
            mylist[5][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[5][0]=replaceBy
        ludoGameUI()
    elif playerIndex==32:           #up
        myExistingCookie=mylist[4][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[4][0]+=replaceBy      
        elif result=="false":
            mylist[4][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[4][0]=replaceBy
        ludoGameUI()
    elif playerIndex==33:           #up
        myExistingCookie=mylist[3][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[3][0]+=replaceBy      
        elif result=="false":
            mylist[3][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[3][0]=replaceBy
        ludoGameUI()
    elif playerIndex==34:           #up
        mylist[2][0]+=replaceBy
        ludoGameUI()
    elif playerIndex==35:           #up
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[1][0]=replaceBy
        ludoGameUI()
    elif playerIndex==36:           #up
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==37:
        myExistingCookie=mylist[0][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][1]+=replaceBy      
        elif result=="false":
            mylist[0][1]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][1]=replaceBy
        ludoGameUI()
    elif playerIndex==38:
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][2]=replaceBy
        ludoGameUI()
    elif playerIndex==39:
        mylist[1][2]+=replaceBy
        ludoGameUI()
    elif playerIndex==40:
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[2][2]=replaceBy
        ludoGameUI()
    elif playerIndex==41:
        myExistingCookie=mylist[3][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[3][2]+=replaceBy      
        elif result=="false":
            mylist[3][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[3][2]=replaceBy
        ludoGameUI()
    elif playerIndex==42:
        myExistingCookie=mylist[4][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[4][2]+=replaceBy      
        elif result=="false":
            mylist[4][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[4][2]=replaceBy
        ludoGameUI()
    elif playerIndex==43:
        myExistingCookie=mylist[5][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[5][2]+=replaceBy      
        elif result=="false":
            mylist[5][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[5][2]=replaceBy
        ludoGameUI()
    elif playerIndex==44:             #again right
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==45:
        myExistingCookie=mylist[0][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][1]+=replaceBy      
        elif result=="false":
            mylist[0][1]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][1]=replaceBy
        ludoGameUI()
    elif playerIndex==46:
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][2]=replaceBy
        ludoGameUI()
    elif playerIndex==47:
        mylist[0][3]+=replaceBy
        ludoGameUI()
    elif playerIndex==48:
        myExistingCookie=mylist[0][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][4]+=replaceBy      
        elif result=="false":
            mylist[0][4]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][4]=replaceBy
        ludoGameUI()
    elif playerIndex==49:
        myExistingCookie=mylist[0][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[0][5]+=replaceBy      
        elif result=="false":
            mylist[0][5]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
             mylist[0][5]=replaceBy
        ludoGameUI()
    elif playerIndex==50:
        myExistingCookie=mylist[1][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player2")
        if result=="true":
            mylist[1][5]+=replaceBy      
        elif result=="false":
            mylist[1][5]=newCookie
            ludoGameUI()
            playerTurn("player2")
        else:
            mylist[1][5]=replaceBy
        ludoGameUI()
    elif playerIndex==51:
        if mylist[1][4]!=0:
            mylist[1][4]+=replaceBy
        else:
             mylist[1][4]+=replaceBy
        ludoGameUI()
    elif playerIndex==52:
        if mylist[1][3]!=0:
            mylist[1][3]+=replaceBy
        else:
             mylist[1][3]+=replaceBy
        ludoGameUI()
    elif playerIndex==53:
        if mylist[1][2]!=0:
            mylist[1][2]+=replaceBy
        else:
             mylist[1][2]+=replaceBy
        ludoGameUI()
    elif playerIndex==54:
        if mylist[1][1]!=0:
            mylist[1][1]+=replaceBy
        else:
             mylist[1][1]+=replaceBy
        ludoGameUI()
    elif playerIndex==55:
        if mylist[1][0]!=0:
            mylist[1][0]+=replaceBy
        else:
             mylist[1][0]+=replaceBy
        ludoGameUI()
    elif playerIndex==56:         #win
        mylist[1][2]+=replaceBy
        ludoGameUI()
    else:
        print("Please provide a valid input")
        
def mapping3(playerIndex,mylist,replaceBy):
    if playerIndex==0:                    #down
        mylist[4][0]+=replaceBy
        ludoGameUI()
    elif playerIndex==1:                    #down
        myExistingCookie=mylist[3][0]
        newCookie=replaceBy        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[3][0]+=replaceBy      
        elif result=="false":
            mylist[3][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[3][0]=replaceBy
        ludoGameUI()
    elif playerIndex==2:                    #down
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][0]=replaceBy
        ludoGameUI()
    elif playerIndex==3:                    #down
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[1][0]=replaceBy
        ludoGameUI()
    elif playerIndex==4:                    #down
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==5:                    #left
        myExistingCookie=mylist[2][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][5]+=replaceBy      
        elif result=="false":
            mylist[2][5]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][5]=replaceBy
        ludoGameUI()
    elif playerIndex==6:                    #left
        myExistingCookie=mylist[2][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][4]+=replaceBy      
        elif result=="false":
            mylist[2][4]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][4]=replaceBy
        ludoGameUI()
    elif playerIndex==7:                    #left
        myExistingCookie=mylist[2][3]
        newCookie=replaceBy        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][3]+=replaceBy      
        elif result=="false":
            mylist[2][3]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][3]=replaceBy
        ludoGameUI()
    elif playerIndex==8:                    #left
        mylist[2][2]+=replaceBy
        ludoGameUI()
    elif playerIndex==9:                    #left
        myExistingCookie=mylist[2][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][1]+=replaceBy      
        elif result=="false":
            mylist[2][1]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][1]=replaceBy
        ludoGameUI()
    elif playerIndex==10:                    #left
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][0]=replaceBy
        ludoGameUI()
    elif playerIndex==11:                    #left
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[1][0]=replaceBy
        ludoGameUI()
    elif playerIndex==12:                    #left
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==13:                    #left
        mylist[0][1]+=replaceBy
        ludoGameUI()
    elif playerIndex==14:                    #left
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][2]=replaceBy
    elif playerIndex==15:                    #left
        myExistingCookie=mylist[0][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][3]+=replaceBy      
        elif result=="false":
            mylist[0][3]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][3]=replaceBy
        ludoGameUI()
    elif playerIndex==16:                    #left
        myExistingCookie=mylist[0][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][4]+=replaceBy      
        elif result=="false":
            mylist[0][4]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][4]=replaceBy
        ludoGameUI()
    elif playerIndex==17:                    #left
        myExistingCookie=mylist[0][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][5]+=replaceBy      
        elif result=="false":
            mylist[0][5]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][5]=replaceBy
        ludoGameUI()
    elif playerIndex==18:                    #up
        myExistingCookie=mylist[5][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[5][0]+=replaceBy      
        elif result=="false":
            mylist[5][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[5][0]=replaceBy
        ludoGameUI()
    elif playerIndex==19:                    #up
        myExistingCookie=mylist[4][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[4][0]+=replaceBy      
        elif result=="false":
            mylist[4][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[4][0]=replaceBy
        ludoGameUI()
    elif playerIndex==20:                    #up
        myExistingCookie=mylist[3][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[3][0]+=replaceBy      
        elif result=="false":
            mylist[3][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[3][0]=replaceBy
        ludoGameUI()
    elif playerIndex==21:                    #up
        mylist[2][0]+=replaceBy
        ludoGameUI()
    elif playerIndex==22:                    #up
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[1][0]=replaceBy
        ludoGameUI()
    elif playerIndex==23:                    #up
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==24:                    #up
        myExistingCookie=mylist[0][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][1]+=replaceBy      
        elif result=="false":
            mylist[0][1]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][1]=replaceBy
        ludoGameUI()
    elif playerIndex==25:                    #up
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][2]=replaceBy
        ludoGameUI()
    elif playerIndex==26:                    #up
        mylist[1][2]+=replaceBy
        ludoGameUI()
    elif playerIndex==27:                    #up
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][2]=replaceBy
        ludoGameUI()
    elif playerIndex==28:                    #up
        myExistingCookie=mylist[3][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[3][2]+=replaceBy      
        elif result=="false":
            mylist[3][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[3][2]=replaceBy
        ludoGameUI()
    elif playerIndex==29:                    #up
        myExistingCookie=mylist[4][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[4][2]+=replaceBy      
        elif result=="false":
            mylist[4][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[4][2]=replaceBy
        ludoGameUI()
    elif playerIndex==30:                    #up
        myExistingCookie=mylist[5][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[5][2]+=replaceBy      
        elif result=="false":
            mylist[5][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[5][2]=replaceBy
        ludoGameUI()
    elif playerIndex==31:                    #right
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==32:                    #right
        myExistingCookie=mylist[0][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][1]+=replaceBy      
        elif result=="false":
            mylist[0][1]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][1]=replaceBy
        ludoGameUI()
    elif playerIndex==33:                    #right
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][2]=replaceBy
        ludoGameUI()
    elif playerIndex==34:                    #right
        mylist[0][3]+=replaceBy
        ludoGameUI()
    elif playerIndex==35:                    #right
        myExistingCookie=mylist[0][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][4]+=replaceBy      
        elif result=="false":
            mylist[0][4]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][4]=replaceBy
        ludoGameUI()
    elif playerIndex==36:                    #right
        myExistingCookie=mylist[0][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][5]+=replaceBy      
        elif result=="false":
            mylist[0][5]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][5]=replaceBy
        ludoGameUI()
    elif playerIndex==37:                    #right
        myExistingCookie=mylist[1][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[1][5]+=replaceBy      
        elif result=="false":
            mylist[1][5]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[1][5]=replaceBy
        ludoGameUI()
    elif playerIndex==38:                    #right
        myExistingCookie=mylist[2][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][5]+=replaceBy      
        elif result=="false":
            mylist[2][5]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][5]=replaceBy
        ludoGameUI()
    elif playerIndex==39:                    #right
        mylist[2][4]+=replaceBy
        ludoGameUI()
    elif playerIndex==40:                    #right
        myExistingCookie=mylist[2][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][3]+=replaceBy      
        elif result=="false":
            mylist[2][3]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][3]=replaceBy
        ludoGameUI()
    elif playerIndex==41:                    #right
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][2]=replaceBy
        ludoGameUI()
    elif playerIndex==42:                    #right
        myExistingCookie=mylist[2][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][1]+=replaceBy      
        elif result=="false":
            mylist[2][1]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][1]=replaceBy
        ludoGameUI()
    elif playerIndex==43:                    #right
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][0]=replaceBy
        ludoGameUI()
    elif playerIndex==44:                    #Again Down
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[0][2]=replaceBy
        ludoGameUI()
    elif playerIndex==45:                    #Again Down
        myExistingCookie=mylist[1][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[1][2]+=replaceBy      
        elif result=="false":
            mylist[1][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[1][2]=replaceBy
        ludoGameUI()
    elif playerIndex==46:                    #Again Down
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[2][2]=replaceBy
        ludoGameUI()
    elif playerIndex==47:                    #Again Down
        mylist[3][2]+=replaceBy
        ludoGameUI()
    elif playerIndex==48:                    #Again Down
        myExistingCookie=mylist[4][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[4][2]+=replaceBy      
        elif result=="false":
            mylist[4][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[4][2]=replaceBy
        ludoGameUI()
    elif playerIndex==49:                    #Again Down
        myExistingCookie=mylist[5][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[5][2]+=replaceBy      
        elif result=="false":
            mylist[5][2]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[5][2]=replaceBy
        ludoGameUI()
    elif playerIndex==50:                    #Again Down
        myExistingCookie=mylist[5][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player3")
        if result=="true":
            mylist[5][1]+=replaceBy      
        elif result=="false":
            mylist[5][1]=newCookie
            ludoGameUI()
            playerTurn("player3")
        else:
            mylist[5][1]=replaceBy
        ludoGameUI()
    elif playerIndex==51:                    #Again Down
        if mylist[4][1]!=0:
            mylist[4][1]+=replaceBy
        else:
            mylist[4][1]=replaceBy
        ludoGameUI()
    elif playerIndex==52:                    #Again Down
        if mylist[3][1]!=0:
            mylist[3][1]+=replaceBy
        else:
            mylist[3][1]=replaceBy
        ludoGameUI()
    elif playerIndex==53:                    #Again Down
        if mylist[2][1]!=0:
            mylist[2][1]+=replaceBy
        else:
            mylist[2][1]=replaceBy
        ludoGameUI()
    elif playerIndex==54:                    #Again Down
        if mylist[1][1]!=0:
            mylist[1][1]+=replaceBy
        else:
            mylist[1][1]=replaceBy
        ludoGameUI()
    elif playerIndex==55:                    #Again Down
        if mylist[0][1]!=0:
            mylist[0][1]+=replaceBy
        else:
            mylist[0][1]=replaceBy
        ludoGameUI()
    elif playerIndex==56:                    #Win
        mylist[2][1]+=replaceBy
        ludoGameUI()
    else:
        print("Please Enter a valid Number")
    
def mapping4(playerIndex,mylist,replaceBy):
    if playerIndex==0:                 #left
        mylist[0][1]+=replaceBy 
        ludoGameUI()
    elif playerIndex==1:                 #left
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][2]=replaceBy
        
        ludoGameUI()
    elif playerIndex==2:                 #left
        myExistingCookie=mylist[0][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][3]+=replaceBy      
        elif result=="false":
            mylist[0][3]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][3]=replaceBy
        ludoGameUI()
    elif playerIndex==3:                 #left
        myExistingCookie=mylist[0][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][4]+=replaceBy      
        elif result=="false":
            mylist[0][4]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][4]=replaceBy
        ludoGameUI()
    elif playerIndex==4:                 #left
        myExistingCookie=mylist[0][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][5]+=replaceBy      
        elif result=="false":
            mylist[0][5]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][5]=replaceBy
        ludoGameUI()
    elif playerIndex==5:                 #up
        myExistingCookie=mylist[5][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[5][0]+=replaceBy      
        elif result=="false":
            mylist[5][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[5][0]=replaceBy
    
        ludoGameUI()
    elif playerIndex==6:                 #up
        myExistingCookie=mylist[4][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[4][0]+=replaceBy      
        elif result=="false":
            mylist[4][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[4][0]=replaceBy
        
        ludoGameUI()
    elif playerIndex==7:                 #up
        myExistingCookie=mylist[3][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[3][0]+=replaceBy      
        elif result=="false":
            mylist[3][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[3][0]=replaceBy
        ludoGameUI()
    elif playerIndex==8:                 #up
        mylist[2][0]+=replaceBy
        ludoGameUI()
    elif playerIndex==9:                 #up
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[1][0]=replaceBy
        ludoGameUI()
        
    elif playerIndex==10:                 #up
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][0]=replaceBy
        ludoGameUI()
    elif playerIndex==11:                 #up
        myExistingCookie=mylist[0][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][1]+=replaceBy      
        elif result=="false":
            mylist[0][1]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][1]=replaceBy
        ludoGameUI()
        
    elif playerIndex==12:                 #up
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][2]=replaceBy
        ludoGameUI()
    elif playerIndex==13:                 #up
       
        mylist[1][2]+=replaceBy
        ludoGameUI()
        
    elif playerIndex==14:                 #up
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][2]=replaceBy
        ludoGameUI()
        
    elif playerIndex==15:                 #up
        myExistingCookie=mylist[3][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[3][2]+=replaceBy      
        elif result=="false":
            mylist[3][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[3][2]=replaceBy
        
        ludoGameUI()
    elif playerIndex==16:                 #up
        myExistingCookie=mylist[4][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[4][2]+=replaceBy      
        elif result=="false":
            mylist[4][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[4][2]=replaceBy
        ludoGameUI()
       
    elif playerIndex==17:                 #up
        myExistingCookie=mylist[5][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[5][2]+=replaceBy      
        elif result=="false":
            mylist[5][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[5][2]=replaceBy
        ludoGameUI()
        
    elif playerIndex==18:                 #right
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][0]=replaceBy
        
        ludoGameUI()
    elif playerIndex==19:                 #right
        myExistingCookie=mylist[0][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][1]+=replaceBy      
        elif result=="false":
            mylist[0][1]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][1]=replaceBy
        ludoGameUI()
    elif playerIndex==20:                 #right
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][2]=replaceBy
        
        ludoGameUI()
    elif playerIndex==21:                 #right
        mylist[0][3]+=replaceBy
        ludoGameUI()
    elif playerIndex==22:                 #right
        myExistingCookie=mylist[0][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][4]+=replaceBy      
        elif result=="false":
            mylist[0][4]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][4]=replaceBy
        
        ludoGameUI()
    elif playerIndex==23:                 #right
        myExistingCookie=mylist[0][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][5]+=replaceBy      
        elif result=="false":
            mylist[0][5]=newCookie
            ludoGameUI()
            playerTurn("player4")

        else:
            mylist[0][5]=replaceBy
        
        ludoGameUI()
    elif playerIndex==24:                 #right
        myExistingCookie=mylist[1][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[1][5]+=replaceBy      
        elif result=="false":
            mylist[1][5]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[1][5]=replaceBy
        
        ludoGameUI()
    elif playerIndex==25:                 #right
        myExistingCookie=mylist[2][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][5]+=replaceBy      
        elif result=="false":
            mylist[2][5]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][5]=replaceBy
        
        ludoGameUI()
    elif playerIndex==26:                 #right
        mylist[2][4]+=replaceBy
        ludoGameUI()
    elif playerIndex==27:                 #right
        myExistingCookie=mylist[2][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][3]+=replaceBy      
        elif result=="false":
            mylist[2][3]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][3]=replaceBy
        ludoGameUI()
        
    elif playerIndex==28:                 #right
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][2]=replaceBy
        
        ludoGameUI()
    elif playerIndex==29:                 #right
        myExistingCookie=mylist[2][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][1]+=replaceBy      
        elif result=="false":
            mylist[2][1]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][1]=replaceBy
        ludoGameUI()
        
    elif playerIndex==30:                 #right
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][0]=replaceBy
        ludoGameUI()
        
    elif playerIndex==31:                 #down
        myExistingCookie=mylist[0][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][2]+=replaceBy      
        elif result=="false":
            mylist[0][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][2]=replaceBy
        ludoGameUI()
        
    elif playerIndex==32:                 #down
        myExistingCookie=mylist[1][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[1][2]+=replaceBy      
        elif result=="false":
            mylist[1][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[1][2]=replaceBy
        ludoGameUI()
        
    elif playerIndex==33:                 #down
        myExistingCookie=mylist[2][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][2]+=replaceBy      
        elif result=="false":
            mylist[2][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][2]=replaceBy
        ludoGameUI()
        
    elif playerIndex==34:                 #down
        mylist[3][2]+=replaceBy
        ludoGameUI()
    elif playerIndex==35:                 #down
        myExistingCookie=mylist[4][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[4][2]+=replaceBy      
        elif result=="false":
            mylist[4][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[4][2]=replaceBy
        
        ludoGameUI()
    elif playerIndex==36:                 #down
        myExistingCookie=mylist[5][2]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[5][2]+=replaceBy      
        elif result=="false":
            mylist[5][2]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[5][2]=replaceBy
        
        ludoGameUI()
    elif playerIndex==37:                 #down
        myExistingCookie=mylist[5][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[5][1]+=replaceBy      
        elif result=="false":
            mylist[5][1]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[5][1]=replaceBy
        
        ludoGameUI()
    elif playerIndex==38:                 #down
        myExistingCookie=mylist[5][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[5][0]+=replaceBy      
        elif result=="false":
            mylist[5][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[5][0]=replaceBy
        ludoGameUI()
        
    elif playerIndex==39:                 #down
        mylist[4][0]+=replaceBy
        ludoGameUI()
    elif playerIndex==40:                 #down
        myExistingCookie=mylist[3][0]
        newCookie=replaceBy        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[3][0]+=replaceBy      
        elif result=="false":
            mylist[3][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[3][0]=replaceBy
        ludoGameUI()
        
    elif playerIndex==41:                 #down
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][0]=replaceBy
        ludoGameUI()
        
    elif playerIndex==42:                 #down
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[1][0]=replaceBy
        
        ludoGameUI()
    elif playerIndex==43:                 #down
        myExistingCookie=mylist[0][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[0][0]+=replaceBy      
        elif result=="false":
            mylist[0][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[0][0]=replaceBy
        
        ludoGameUI()
    elif playerIndex==44:                 #Again left
        myExistingCookie=mylist[2][5]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][5]+=replaceBy      
        elif result=="false":
            mylist[2][5]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][5]=replaceBy
        
        ludoGameUI()
    elif playerIndex==45:                 #Again left
        myExistingCookie=mylist[2][4]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][4]+=replaceBy      
        elif result=="false":
            mylist[2][4]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][4]=replaceBy
        ludoGameUI()
        
    elif playerIndex==46:                 #Again left
        myExistingCookie=mylist[2][3]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][3]+=replaceBy      
        elif result=="false":
            mylist[2][3]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][3]=replaceBy
        
        ludoGameUI()
    elif playerIndex==47:                 #Again left
        mylist[2][2]+=replaceBy
        ludoGameUI()
    elif playerIndex==48:                 #Again left
        
        myExistingCookie=mylist[2][1]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][1]+=replaceBy      
        elif result=="false":
            mylist[2][1]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][1]=replaceBy
        
        ludoGameUI()
    elif playerIndex==49:                 #Again left
        myExistingCookie=mylist[2][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[2][0]+=replaceBy      
        elif result=="false":
            mylist[2][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[2][0]=replaceBy
        ludoGameUI()
        
    elif playerIndex==50:                 #Again left
        myExistingCookie=mylist[1][0]
        newCookie=replaceBy
        
        result = ismyPlayer(myExistingCookie,newCookie,"player4")
        if result=="true":
            mylist[1][0]+=replaceBy      
        elif result=="false":
            mylist[1][0]=newCookie
            ludoGameUI()
            playerTurn("player4")
        else:
            mylist[1][0]=replaceBy
        ludoGameUI()
       
    elif playerIndex==51:                 #Again left
        if mylist[1][1]!=0:
            mylist[1][1]+=replaceBy
        else:
            mylist[1][1]=replaceBy
        ludoGameUI()
    elif playerIndex==52:                 #Again left
        if mylist[1][2]!=0:
            mylist[1][2]+=replaceBy
        else:
            mylist[1][2]=replaceBy
        ludoGameUI()
    elif playerIndex==53:                 #Again left
        if mylist[1][3]!=0:
            mylist[1][3]+=replaceBy
        else:
            mylist[1][3]=replaceBy
        ludoGameUI()
    elif playerIndex==54:                 #Again left
        if mylist[1][4]!=0:
            mylist[1][4]+=replaceBy
        else:
            mylist[1][4]=replaceBy
        ludoGameUI()
    elif playerIndex==55:                 #Again left
        if mylist[1][5]!=0:
            mylist[1][5]+=replaceBy
        else:
            mylist[1][5]=replaceBy
        ludoGameUI()
    elif playerIndex==56:                 #win
        mylist[1][0]+=replaceBy
        ludoGameUI()
    else:
        print("Please Enter a valid Number")  
posLists = [posUp, posLeft, posRight, posDown]           
    
def player1Turn():
    playerTurn("player1")
    player2Turn()
    
def player2Turn():
    playerTurn("player2")    
    player3Turn()
    
def player3Turn():
    playerTurn("player3")
    player4Turn()
    
def player4Turn():
    playerTurn("player4")
    player1Turn()
def removeSpecificCharacterFromSafePosition(posLists, specificCharacter):
    for posList in posLists:
        for i in range(len(posList)):
            for j in range(len(posList[i])):
                element = posList[i][j]                
                if isinstance(element, str):                    
                    if element == specificCharacter:
                        posList[i][j] = '0'
                    else:                                              
                        posList[i][j] = element.replace(specificCharacter, '')                
                if isinstance(element, str) and (element.startswith('*') or element.startswith('#')):
                    
                    if specificCharacter in element:
                        posList[i][j] = element.replace(specificCharacter, '')               
    return posLists




def playerTurn(player,isNumber6=False,playerchoice=0):
        global a1Index
        global a2Index
        global a3Index
        global a4Index
        global b1Index
        global b3Index
        global b4Index
        global b2Index
        global c1Index
        global c2Index
        global c4Index
        global c3Index
        global d1Index
        global d2Index
        global d3Index
        global d4Index
        global a1Initialized
        global a2Initialized
        global a3Initialized
        global a4Initialized
        global b1Initialized
        global b2Initialized
        global b3Initialized
        global b4Initialized
        global c1Initialized
        global c2Initialized
        global c3Initialized
        global c4Initialized
        global d1Initialized
        global d2Initialized
        global d3Initialized
        global d4Initialized
        global sixCount
        
        diceRollSix=False
        randomDiceRoll=False
        if player == "player1":  
            if a1Index!=56 or a2Index!=56 or a3Index!=56 or a4Index!=56:             
                playerSixChoice=[]
                
                print("**********************************player1*********************")
                
                if isNumber6==False:
                    player1Dice=int(input("Press Enter to throw a Dice :"))
                else:
                    sixCount+=1
                    if (sixCount==3):
                        sixCount=0
                        player1Dice=int(input("Press Enter to throw a Dice Again (3rd Time Six)"))
                    else:
                        player1Dice=int(input("Press Enter to throw a Dice Again "))
                # player1Dice = random.randint(1,7)
                print("Dice Number ",player1Dice)
                global instantStartA
                if instantStartA==False:                
                    print("Enter 1 to move A1")
                    print("Enter 2 to move A2")
                    print("Enter 3 to Move A3")
                    print("Enter 4 to Move A4")
                    instantStartA=True
                    
                elif player1Dice==6:
                    
                    diceRollSix=True
                    
                    if a1Index==0 and a1Initialized==False:
                        print("Enter a1 to open A1")
                        playerSixChoice.append('a1')
                        
                    if a2Index==0 and a2Initialized==False:
                        print("Enter a2 to open A2")
                        playerSixChoice.append('a2')
                        
                    if a3Index==0 and a3Initialized==False:
                        print("Enter a3 to open A3")
                        playerSixChoice.append('a3')
                        
                    if a4Index==0 and a4Initialized==False:
                        print("Enter a4 to open A4")
                        playerSixChoice.append('a4')
                        
                    if a1Index!=56:   
                        if a1Index>0 or a1Initialized==True:
                            print("Enter 1 to move A1")
                            playerSixChoice.append('1')
                            
                    if a2Index!=56:
                        if a2Index>0 or a2Initialized==True:
                            print("Enter 2 to move A2")  
                            playerSixChoice.append('2')
                            
                    if a3Index!=56:
                        if a3Index>0 or a3Initialized == True:
                            print("Enter 3 to Move A3")
                            playerSixChoice.append('3')
                            
                    if a4Index!=56:
                        if a4Index>0 or a4Initialized == True:
                            print("Enter 4 to Move A4")
                            playerSixChoice.append('4')
                        
                else:
                    randomDiceRoll=True
                    randomDiceNumberOccured=[]
                    if a1Index!=56:
                        if a1Index>0 or a1Initialized==True:
                            print("Enter 1 to move A1")
                            randomDiceNumberOccured.append('1')
                    if a2Index!=56:
                        if a2Index>0 or a2Initialized==True:
                            print("Enter 2 to move A2") 
                            randomDiceNumberOccured.append('2')
                    if a3Index!=56: 
                        if a3Index>0 or a3Initialized==True:
                            print("Enter 3 to Move A3")
                            randomDiceNumberOccured.append('3')
                    if a4Index!=56:
                        if a4Index>0 or a4Initialized==True:
                            print("Enter 4 to Move A4")
                            randomDiceNumberOccured.append('4')
                 
            while True:
                
                if a1Index==56 and a2Index==56 and a3Index==56 and a4Index==56:
                    return 
                if randomDiceRoll==True and len(randomDiceNumberOccured)==0:
                    
                    return
                while True:
                    
                    player1DiceChoice = input("Enter Your Choice :")
                    if diceRollSix==True:
                        if player1DiceChoice in playerSixChoice:
                            playerSixChoice=[]
                            break
                        else:
                            print("Please Enter a valid Choice in sixer")
                    elif randomDiceRoll==True:
                        if player1DiceChoice in randomDiceNumberOccured:
                            randomDiceNumberOccured=[]
                            break
                        else:
                            print("Please Enter a valid choice in random Number ")
                    else:
                        if player1DiceChoice not in ['1','2','3','4']:
                            print("Please Enter a valid Choice Only between 1 to 4") 
                        else:
                            break
                        
                if player1DiceChoice=="a1":
                    print("a1 initialized")
                    mapping(0,posUp,'a1')
                    a1Initialized=True
                    break
                if player1DiceChoice=="a2":
                    print("a2 initialized")
                    mapping(0,posUp,'a2')
                    a2Initialized=True
                    break
                if player1DiceChoice=="a3":
                    print("a3 initialized")
                    mapping(0,posUp,'a3')
                    a3Initialized=True
                    break
                if player1DiceChoice=="a4":
                    print("a4 initialized")
                    mapping(0,posUp,'a4')
                    a4Initialized=True
                    break
                    
                if player1DiceChoice.isnumeric():
         
                    player1DiceChoice=int(player1DiceChoice)                    
                    if player1DiceChoice==1:
                        # mapping(0,posUp,'a1')
                        a1Initialized=True
                        previousIndex=a1Index
                        
                        a1Index+=player1Dice
                        if a1Index < 57:    
                        
                            if (a1Index<=4):
                               
                                removeSpecificCharacterFromSafePosition(posLists,'a1')                                                    
                                mapping(a1Index,posUp,'a1')
                                
                            elif a1Index>=5 and a1Index<=17:
                               
                                removeSpecificCharacterFromSafePosition(posLists,'a1')                                
                                mapping(a1Index,posRight,'a1')
                                
                            elif a1Index>=18 and a1Index<=30:
                               
                                removeSpecificCharacterFromSafePosition(posLists,'a1')                                
                                mapping(a1Index,posDown,'a1')
                                
                            elif a1Index>=31 and a1Index<=43:
                                removeSpecificCharacterFromSafePosition(posLists,'a1')                                
                                mapping(a1Index,posLeft,'a1')
                                
                            elif a1Index>=44 and a1Index<=56:
                                
                                removeSpecificCharacterFromSafePosition(posLists,'a1')                                
                                if a1Index==56:
                                    mapping(a1Index,posWin,'a1')
                                else:
                                    mapping(a1Index,posUp,'a1')
                                if a1Index==56 and a2Index==56 and a3Index==56 and a4Index==56:
                                    print("\t\t****  Player 1 Wins  ****")
                                    return
                                elif a1Index==56:
                                    print("Congratulation a1 is at home")
                                    if(player1Dice!=6):
                                        return
                            else:
                                print("Your Cookie will not move Ahead")
                        else:
                          
                            a1Index=previousIndex
                      
                            print("Your Cookie will not move Ahead")
                    elif player1DiceChoice==2:
                        
                        a2Initialized=True
                        previousA2Index=a2Index
                        a2Index+=player1Dice
                        if a2Index<57:
                            
                            if (a2Index<=4):
                                removeSpecificCharacterFromSafePosition(posLists,'a2')
                                                    
                                mapping(a2Index,posUp,'a2')                            
                            elif a2Index>=5 and a2Index<=17:
                                removeSpecificCharacterFromSafePosition(posLists,'a2')
                                
                                mapping(a2Index,posRight,'a2')
                            elif a2Index>=18 and a2Index<=30:
                                removeSpecificCharacterFromSafePosition(posLists,'a2')
                                
                                mapping(a2Index,posDown,'a2')
                            elif a2Index>=31 and a2Index<=43:
                                removeSpecificCharacterFromSafePosition(posLists,'a2')
                                
                                mapping(a2Index,posLeft,'a2')
                            elif a2Index>=44 and a2Index<=56:
                                removeSpecificCharacterFromSafePosition(posLists,'a2')
                                
                                if a2Index==56:
                                    mapping(a2Index,posWin,'a2')
                                else:
                                    mapping(a2Index,posUp,'a2')
                                if a1Index==56 and a2Index==56 and a3Index==56 and a4Index==56:
                                    print("\t\t****  Player 1 Wins  ****")
                                    return
                                elif a2Index==56:
                                    print("Congratulation a2 is at home")
                                    if(player1Dice!=6):
                                        return
                            else:
                                print("Your Cookie will not move Ahead")
                        else:
                                a2Index=previousA2Index
                                print("Your Cookie will not move Ahead")    
                    elif player1DiceChoice==3:                        
                        a3Initialized=True                        
                        previousA3Index=a3Index
                      
                        a3Index+=player1Dice
                        
                        if a3Index < 57:
                            
                            if (a3Index<=4):
                                removeSpecificCharacterFromSafePosition(posLists,'a3')                                                    
                                mapping(a3Index,posUp,'a3')                            
                            elif a3Index>=5 and a3Index<=17:
                                removeSpecificCharacterFromSafePosition(posLists,'a3')
                                
                                mapping(a3Index,posRight,'a3')
                            elif a3Index>=18 and a3Index<=30:
                                removeSpecificCharacterFromSafePosition(posLists,'a3')
                                
                                mapping(a3Index,posDown,'a3')
                            elif a3Index>=31 and a3Index<=43:
                                removeSpecificCharacterFromSafePosition(posLists,'a3')
                                
                                mapping(a3Index,posLeft,'a3')
                            elif a3Index>=44 and a3Index<=56:
                                removeSpecificCharacterFromSafePosition(posLists,'a3')
                                
                                if a3Index==56:
                                    mapping(a3Index,posWin,'a3')
                                else:
                                    mapping(a3Index,posUp,'a3')
                                if a1Index==56 and a2Index==56 and a3Index==56 and a4Index==56:
                                    print("\t\t****  Player 1 Wins  ****")
                                    return                                
                                elif a3Index==56:
                                    print("Congratulation a3 is at home")
                                    if(player1Dice!=6):
                                        return
                            else:
                                print("Your Cookie will not move Ahead")                                
                        else:
                            a3Index=previousA3Index
                            print("Your Cookie will not move Ahead")
                    elif player1DiceChoice==4:
                        
                        a4Initialized=True
                        previousA4Index=a4Index
                        a4Index+=player1Dice
                        if a4Index<57:
                            if (a4Index<=4):
                                removeSpecificCharacterFromSafePosition(posLists,'a4')                                                    
                                mapping(a4Index,posUp,'a4')                            
                            elif a4Index>=5 and a4Index<=17:
                                removeSpecificCharacterFromSafePosition(posLists,'a4')                                
                                mapping(a4Index,posRight,'a4')
                            elif a4Index>=18 and a4Index<=30:
                                removeSpecificCharacterFromSafePosition(posLists,'a4')                                
                                mapping(a4Index,posDown,'a4')
                            elif a4Index>=31 and a4Index<=43:
                                removeSpecificCharacterFromSafePosition(posLists,'a4')                                
                                mapping(a4Index,posLeft,'a4')
                            elif a4Index>=44 and a4Index<=56:
                                removeSpecificCharacterFromSafePosition(posLists,'a4')                                
                                if a4Index==56:
                                    mapping(a4Index,posWin,'a4')
                                else:
                                    mapping(a4Index,posUp,'a4')
                                if a1Index==56 and a2Index==56 and a3Index==56 and a4Index==56:
                                    print("\t\t****  Player 1 Wins  ****")
                                    return
                                elif a4Index==56:
                                    print("Congratulation a4 is at home")
                                    if(player1Dice!=6):
                                        return                                    
                            else:
                                print("Your Cookie will not move Ahead")
                        else:
                            a4Index=previousA4Index
                    break
                else:
                    print("Please Provide a valid Input")
                    
            if player1Dice==6:
                playerTurn("player1",True)                
            
            if (b1Index==0 and b2Index==0 and b3Index==0 and b4Index==0) or (c1Index==0 and c2Index==0 and c3Index==0 and c4Index==0) or(d1Index==0 and d2Index==0 and d3Index==0 and d4Index==0) :
                return True
            else:
                player2Turn()
                
        if player == "player2":
            if b1Index!=56 or b2Index!=56 or b3Index!=56 or b4Index!=56:
                playerSixChoice=[]
                
                print("***************************player 2************************")
                if isNumber6==False:
                    player2Dice=int(input("Press Enter to throw a Dice :"))
                else:
                    sixCount+=1
                    if (sixCount==3):
                        sixCount=0
                        player2Dice=int(input("Press Enter to throw a Dice Again (3rd Time Six)"))
                    else:
                        player2Dice=int(input("Press Enter to throw a Dice Again "))           
            
                
                global instantStartB
                
                if instantStartB==False: 
                    print("Enter 1 to move B1")
                    print("Enter 2 to move B2")
                    print("Enter 3 to Move B3")
                    print("Enter 4 to Move B4")
                    instantStartB=True
                elif player2Dice==6:
                    diceRollSix=True               
                    
                    if  b1Index==0 and b1Initialized==False:
                        print("Enter b1 to open B1")
                        playerSixChoice.append('b1')                
                        
                    if b2Index==0 and b2Initialized==False:
                        print("Enter b2 to open B2")
                        playerSixChoice.append('b2')                    
                    
                    if b3Index==0 and b3Initialized==False:
                        print("Enter b3 to open B3")
                        playerSixChoice.append('b3')                
                    
                        
                    if b4Index==0 and b4Initialized==False:
                        print("Enter b4 to open B4")
                        playerSixChoice.append('b4')
                    if b1Index!=56:    
                        if b1Index>0 or b1Initialized:
                            print("Enter 1 to move B1")
                            playerSixChoice.append('1')
                    if b2Index!=56:
                        if b2Index>0 or b2Initialized:
                            print("Enter 2 to move B2") 
                            playerSixChoice.append('2')
                    if b3Index!=56: 
                        if b3Index>0 or b3Initialized:
                            print("Enter 3 to Move B3")
                            playerSixChoice.append('3')
                    if b4Index!=56:
                        if b4Index>0 or b4Initialized:
                            print("Enter 4 to Move B4")
                            playerSixChoice.append('4')
                        
                else:
                    randomDiceRoll=True
                    randomDiceNumberOccured=[]
                    if b1Index!=56:
                        if b1Index>0 or b1Initialized==True:
                            print("Enter 1 to move B1")
                            randomDiceNumberOccured.append('1')
                    if b2Index!=56:
                        if b2Index>0 or b2Initialized==True:
                            print("Enter 2 to move B2")
                            randomDiceNumberOccured.append('2') 
                    if b3Index!=56: 
                        if b3Index>0 or b3Initialized==True:
                            print("Enter 3 to Move B3")
                            randomDiceNumberOccured.append('3')
                    if b4Index!=56:
                        if b4Index>0 or b4Initialized==True:
                            print("Enter 4 to Move B4")
                            randomDiceNumberOccured.append('4')
            while True:
                if b1Index==56 and b2Index==56 and b3Index==56 and b4Index==56:
                    return
                if randomDiceRoll==True and len(randomDiceNumberOccured)==0:
                    return
                # player2DiceChoice = input("Enter Your Choice :")
                while True:
                    player2DiceChoice = input("Enter Your Choice player2:")
                    if diceRollSix==True:
                        if player2DiceChoice in playerSixChoice:
                            playerSixChoice=[]
                            break
                        else:
                            print("Please Enter a valid Choice in sixer")
                    elif randomDiceRoll==True:
                        if player2DiceChoice in randomDiceNumberOccured:
                            randomDiceNumberOccured=[]
                            break
                        else:
                            print("Please Enter a valid choice in random Number ")
                    else:
                        if player2DiceChoice not in ['1','2','3','4']:
                            print("Please Enter a valid Choice Only between 1 to 4") 
                        else:
                            break
                if player2DiceChoice=="b1":
                    print("B1 initialized")
                    mapping2(0,posRight,'b1')
                    b1Initialized=True
                    break
                if player2DiceChoice=="b2":
                    print("B2 initialized")
                    mapping2(0,posRight,'b2')
                    b2Initialized=True
                    break
                if player2DiceChoice=="b3":
                    print("B3 initialized")
                    mapping2(0,posRight,'b3')
                    b3Initialized=True
                    break
                if player2DiceChoice=="b4":
                    print("B4 Initialized")
                    mapping2(0,posRight,'b4')
                    b4Initialized=True
                    break
                if player2DiceChoice.isnumeric():
                    player2DiceChoice=int(player2DiceChoice)
                    if player2DiceChoice==1:
                        b1Initialized=True
                        b1Index+=player2Dice
                        if (b1Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'b1')                                               
                            mapping2(b1Index,posRight,'b1')                            
                        elif b1Index>=5 and b1Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'b1')                            
                            mapping2(b1Index,posDown,'b1')
                        elif b1Index>=18 and b1Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'b1')                            
                            mapping2(b1Index,posLeft,'b1')
                        elif b1Index>=31 and b1Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'b1')                            
                            mapping2(b1Index,posUp,'b1')
                        elif b1Index>=44 and b1Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'b1')                            
                            if b1Index==56:
                                 mapping2(b1Index,posWin,'b1')
                            else:
                                mapping2(b1Index,posRight,'b1')
                            if b1Index==56 and b2Index==56 and b3Index==56 and b4Index==56:
                                    print("\t\t****  Player 2 Wins  ****")
                                    return
                            if b1Index==56:
                                print("Congratulation b1 is at home")
                                if player2Dice!=6:
                                    return
                        else:
                            print("Your Cookie will not move Ahead")
                        
                    if player2DiceChoice==2:
                        b2Initialized=True
                        b2Index+=player2Dice
                        if (b2Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'b2')                                                
                            mapping2(b2Index,posRight,'b2')                            
                        elif b2Index>=5 and b2Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'b2')                            
                            mapping2(b2Index,posDown,'b2')
                        elif b2Index>=18 and b2Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'b2')                            
                            mapping2(b2Index,posLeft,'b2')
                        elif b2Index>=31 and b2Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'b2')
                            
                            mapping2(b2Index,posUp,'b2')
                        elif b2Index>=44 and b2Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'b2')
                            
                            if b2Index==56:
                                mapping2(b2Index,posWin,'b2')
                            else:
                                mapping2(b2Index,posRight,'b2')
                            if b1Index==56 and b2Index==56 and b3Index==56 and b4Index==56:
                                    print("\t\t****  Player 2 Wins  ****")
                                    return
                            elif b2Index==56:
                                print("Congratulation b2 is at home")
                                if player2Dice!=6:
                                    return
                        else:
                            print("Your Cookie will not move Ahead")
                        
                    if player2DiceChoice==3:
                        b3Initialized=True
                        b3Index+=player2Dice
                        if (b3Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'b3')                                                
                            mapping2(b3Index,posRight,'b3')                            
                        elif b3Index>=5 and b3Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'b3')                            
                            mapping2(b3Index,posDown,'b3')
                        elif b3Index>=18 and b3Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'b3')                            
                            mapping2(b3Index,posLeft,'b3')
                        elif b3Index>=31 and b3Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'b3')                            
                            mapping2(b3Index,posUp,'b3')
                        elif b3Index>=44 and b3Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'b3')                            
                            if b3Index==56:
                                mapping2(b3Index,posWin,'b3')
                            else:
                                mapping2(b3Index,posRight,'b3')
                            if b1Index==56 and b2Index==56 and b3Index==56 and b4Index==56:
                                    print("\t\t****  Player 2 Wins  ****")
                                    return
                            elif b3Index==56:
                                print("Congratulation b3 is at home")
                                if player2Dice!=6:
                                    return
                        else:
                            print("Your Cookie will not move Ahead")
                        
                    if player2DiceChoice==4:
                        b4Initialized=True
                        b4Index+=player2Dice
                        if (b4Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'b4')                                                
                            mapping2(b4Index,posRight,'b4')                            
                        elif b4Index>=5 and b4Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'b4')                            
                            mapping2(b4Index,posDown,'b4')
                        elif b4Index>=18 and b4Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'b4')                            
                            mapping2(b4Index,posLeft,'b4')
                        elif b4Index>=31 and b4Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'b4')                            
                            mapping2(b4Index,posUp,'b4')
                        elif b4Index>=44 and b4Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'b4')                            
                            if b4Index==56:
                               mapping2(b4Index,posWin,'b4')
                            else:
                                mapping2(b4Index,posRight,'b4')
                            if b1Index==56 and b2Index==56 and b3Index==56 and b4Index==56:
                                    print("\t\t****  Player 2 Wins  ****")
                                    return
                            elif b4Index==56:
                                print("Congratulation b4 is at home")
                                if player2Dice!=6:
                                    return
                        else:
                            print("Your Cookie will not move Ahead")                        
                    break
                else:
                    print("Please Provide a valid Input")
            if player2Dice==6:
                playerTurn("player2",True)
                
            if (a1Index==0 and a2Index==0 and a3Index==0 and a4Index==0) or (c1Index==0 and c2Index==0 and c3Index==0 and c4Index==0) or(d1Index==0 and d2Index==0 and d3Index==0 and d4Index==0) :
                return
            else:
                if playerChoice==2:
                    player1Turn()
                else:
                     player3Turn()                
           
        if player == "player3":
            if c1Index!=56 or c2Index!=56 or c3Index!=56 or c4Index!=56:
                playerSixChoice=[]
                
                
                print("****************************player3************************")
                
                if isNumber6==False:
                    player3Dice=int(input("Press Enter to throw a Dice :"))
                else:
                    sixCount+=1
                    if (sixCount==3):
                        sixCount=0
                        player3Dice=int(input("Press Enter to throw a Dice Again (3rd Time Six)"))
                    else:
                        player3Dice=int(input("Press Enter to throw a Dice Again "))
                # player3Dice = random.randint(1,7)
                global instantStartC
                if instantStartC==False:
                    print("Dice Number ",player3Dice)
                    print("Enter 1 to move C1")
                    print("Enter 2 to move C2")
                    print("Enter 3 to Move C3")
                    print("Enter 4 to Move C4")
                    instantStartC=True
                elif player3Dice==6:
                    diceRollSix=True
                    if  c1Index==0 and c1Initialized==False:
                        print("Enter c1 to open C1")
                        playerSixChoice.append('c1')
                    
                        
                    if c2Index==0 and c2Initialized==False:
                        print("Enter c2 to open C2")
                        playerSixChoice.append('c2')
                        
                    
                    if c3Index==0 and c3Initialized==False:
                        print("Enter c3 to open C3")
                        playerSixChoice.append('c3')                    
                    
                        
                    if c4Index==0 and c4Initialized==False:
                        print("Enter c4 to open C4")
                        playerSixChoice.append('c4')
                    if c1Index!=56:    
                        if c1Index>0 or c1Initialized:
                            print("Enter 1 to move C1")
                            playerSixChoice.append('1')
                    if c2Index!=56:
                        if c2Index>0 or c2Initialized:
                            print("Enter 2 to move C2") 
                            playerSixChoice.append('2')
                    if c3Index!=56: 
                        if c3Index>0 or c3Initialized:
                            print("Enter 3 to Move C3")
                            playerSixChoice.append('3')
                    if c4Index!=56:
                        if c4Index>0 or c4Initialized:
                            print("Enter 4 to Move C4")
                            playerSixChoice.append('4')
                        
                else:
                    randomDiceRoll=True
                    randomDiceNumberOccured=[]
                    if c1Index!=56:
                        if c1Index>0 or c1Initialized==True:
                            print("Enter 1 to move C1")
                            randomDiceNumberOccured.append('1')
                    if c2Index!=56:
                        if c2Index>0 or c2Initialized==True:
                            print("Enter 2 to move C2")
                            randomDiceNumberOccured.append('2') 
                    if c3Index!=56: 
                        if c3Index>0 or c3Initialized==True:
                            print("Enter 3 to Move C3")
                            randomDiceNumberOccured.append('3')
                    if c4Index!=56:
                        if c4Index>0 or c4Initialized==True:
                            print("Enter 4 to Move C4")
                            randomDiceNumberOccured.append('4')        
            while True:
                if c1Index==56 and c2Index==56 and c3Index==56 and c4Index==56:
                    return
                if randomDiceRoll==True and len(randomDiceNumberOccured)==0:
                    return
                while True:
                    player3DiceChoice = input("Enter Your Choice player3:")
                    if diceRollSix==True:
                        if player3DiceChoice in playerSixChoice:
                            playerSixChoice=[]
                            break
                        else:
                            print("Please Enter a valid Choice in sixer")
                    elif randomDiceRoll==True:
                        if player3DiceChoice in randomDiceNumberOccured:
                            randomDiceNumberOccured=[]
                            break
                        else:
                            print("Please Enter a valid choice in random Number ")
                    else:
                        if player3DiceChoice not in ['1','2','3','4']:
                            print("Please Enter a valid Choice Only between 1 to 4") 
                        else:
                            break
                if player3DiceChoice=="c1":
                    print("c1 Initialized")
                    mapping3(0,posDown,'c1')
                    c1Initialized=True
                    break
                if player3DiceChoice=="c2":
                    print("c2 initialized")
                    mapping3(0,posDown,'c2')
                    c2Initialized=True
                    break
                if player3DiceChoice=="c3":
                    print("c3 initialized")
                    mapping3(0,posDown,'c3')
                    c3Initialized=True
                    break
                if player3DiceChoice=="c4":
                    print("c4 initialized")
                    mapping3(0,posDown,'c4')
                    c4Initialized=True
                    break
                if player3DiceChoice.isnumeric():
                    player3DiceChoice=int(player3DiceChoice)
                    if player3DiceChoice==1:
                        c1Initialized=True
                        c1Index+=player3Dice
                        if (c1Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'c1')                                                
                            mapping3(c1Index,posDown,'c1')                            
                        elif c1Index>=5 and c1Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'c1')
                            
                            
                            mapping3(c1Index,posLeft,'c1')
                        elif c1Index>=18 and c1Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'c1')
                            
                            mapping3(c1Index,posUp,'c1')
                        elif c1Index>=31 and c1Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'c1')
                            
                            mapping3(c1Index,posRight,'c1')
                        elif c1Index>=44 and c1Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'c1')
                            
                            if c1Index==56:
                                mapping3(c1Index,posWin,'c1')
                            else:
                                mapping3(c1Index,posDown,'c1')
                            if c1Index==56 and c2Index==56 and c3Index==56 and c4Index==56:
                                    print("\t\t****  Player 3 Wins  ****")
                                    return
                            elif c1Index==56:
                                print("Congratulation c1 is at home")
                                if player3Dice!=6:
                                    return 
                        else:
                            print("Your Cookie will not move Ahead")
                       
                    if player3DiceChoice==2:
                        c2Initialized=True
                        c2Index+=player3Dice
                        if (c2Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'c2')
                                                
                            mapping3(c2Index,posDown,'c2')                            
                        elif c2Index>=5 and c2Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'c2')
                            
                            mapping3(c2Index,posLeft,'c2')
                        elif c2Index>=18 and c2Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'c2')
                            
                            mapping3(c2Index,posUp,'c2')
                        elif c2Index>=31 and c2Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'c2')
                            
                            mapping3(c2Index,posRight,'c2')
                        elif c2Index>=44 and c2Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'c2')
                            
                            if c2Index==56:
                               mapping3(c2Index,posWin,'c2') 
                            else:
                                mapping3(c2Index,posDown,'c2')
                            if c1Index==56 and c2Index==56 and c3Index==56 and c4Index==56:
                                    print("\t\t****  Player 3 Wins  ****")
                                    return
                            elif c2Index==56:
                                print("Congratulation c2 is at home")
                                if player3Dice!=6:
                                    return 
                        else:
                            print("Your Cookie will not move Ahead")
                        
                    if player3DiceChoice==3:
                        c3Initialized=True
                        c3Index+=player3Dice
                        if (c3Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'c3')
                                              
                            mapping3(c3Index,posDown,'c3')                            
                        elif c3Index>=5 and c3Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'c3')
                            
                            mapping3(c3Index,posLeft,'c3')
                        elif c3Index>=18 and c3Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'c3')
                            
                            mapping3(c3Index,posUp,'c3')
                        elif c3Index>=31 and c3Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'c3')
                            
                            mapping3(c3Index,posRight,'c3')
                        elif c3Index>=44 and c3Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'c3')
                            
                            if c3Index==56:
                               mapping3(c3Index,posWin,'c3') 
                            else:
                                mapping3(c3Index,posDown,'c3')
                            if c1Index==56 and c2Index==56 and c3Index==56 and c4Index==56:
                                    print("\t\t****  Player 3 Wins  ****")
                                    return
                            elif c3Index==56:
                                print("Congratulation c3 is at home")
                                if player3Dice!=6:
                                    return 
                        else:
                            print("Your Cookie will not move Ahead")
                        
                    if player3DiceChoice==4:
                        c4Initialized=True
                        c4Index+=player3Dice
                        if (c4Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'c4')
                                                
                            mapping3(c4Index,posDown,'c4')                            
                        elif c4Index>=5 and c4Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'c4')
                            
                            mapping3(c4Index,posLeft,'c4')
                        elif c4Index>=18 and c4Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'c4')
                            
                            mapping3(c4Index,posUp,'c4')
                        elif c4Index>=31 and c4Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'c4')
                            
                            mapping3(c4Index,posRight,'c4')
                        elif c4Index>=44 and c4Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'c4')
                            
                            if c4Index==56:
                                 mapping3(c4Index,posWin,'c4')
                            else:
                                mapping3(c4Index,posDown,'c4')
                            if c1Index==56 and c2Index==56 and c3Index==56 and c4Index==56:
                                    print("\t\t****  Player 3 Wins  ****")
                                    return
                            elif c4Index==56:
                                print("Congratulation c4 is at home")
                                if player3Dice!=6:
                                    return                                 
                        else:
                            print("Your Cookie will not move Ahead")                        
                    break
                else:
                    print("Please Provide a valid Input")
                    break
            if player3Dice==6:
                playerTurn("player3",True)    
                
            if (a1Index==0 and a2Index==0 and a3Index==0 and a4Index==0) or (b1Index==0 and b2Index==0 and b3Index==0 and b4Index==0) or(d1Index==0 and d2Index==0 and d3Index==0 and d4Index==0) :
                return
            else:
                if playerChoice==3:
                    player1Turn()
                else:
                    player4Turn()
                
            
        if player == "player4":
            if d1Index!=56 or d2Index!=56 or d3Index!=56 or d4Index!=56:       
                playerSixChoice=[]
                print("****************************player4*********************************")            
                if isNumber6==False:
                    player4Dice=int(input("Press Enter to throw a Dice :"))
                else:
                    sixCount+=1
                    if (sixCount==3):
                        sixCount=0
                        player4Dice=int(input("Press Enter to throw a Dice Again (3rd Time Six)"))
                    else:
                        player4Dice=int(input("Press Enter to throw a Dice Again "))
                # player4Dice = random.randint(1,7)
                global instantStartD
                if instantStartD==False:
                    print("Dice Number ",player4Dice)
                    print("Enter 1 to move D1")
                    print("Enter 2 to move D2")
                    print("Enter 3 to Move D3")
                    print("Enter 4 to Move D4")
                    instantStartD=True
                elif player4Dice==6:
                    diceRollSix=True
                    
                    if  d1Index==0 and d1Initialized==False:
                        print("Enter d1 to open D1")
                        playerSixChoice.append('d1')                
                        
                    if d2Index==0 and d2Initialized==False:
                        print("Enter d2 to open D2")
                        playerSixChoice.append('d2')                    
                    
                    if d3Index==0 and d3Initialized==False:
                        print("Enter d3 to open D3")
                        playerSixChoice.append('d3')              
                    
                        
                    if d4Index==0 and d4Initialized==False:
                        print("Enter d4 to open D4")
                        playerSixChoice.append('d4')
                    if d1Index!=56:    
                        if d1Index>0 or d1Initialized:
                            print("Enter 1 to move D1")
                            playerSixChoice.append('1')
                    if d2Index!=56:
                        if d2Index>0 or d2Initialized:
                            print("Enter 2 to move D2") 
                            playerSixChoice.append('2')
                    if d3Index!=56: 
                        if d3Index>0 or d3Initialized:
                            print("Enter 3 to Move D3")
                            playerSixChoice.append('3')
                    if c4Index!=56:
                        if d4Index>0 or d4Initialized:
                            print("Enter 4 to Move D4")
                            playerSixChoice.append('4')
                        
                else:
                    randomDiceRoll=True
                    randomDiceNumberOccured=[]
                    if d1Index!=56:
                        if d1Index>0 or d1Initialized==True:
                            print("Enter 1 to move D1")
                            randomDiceNumberOccured.append('1')
                    if d2Index!=56:
                        if d2Index>0 or d2Initialized==True:
                            print("Enter 2 to move D2")
                            randomDiceNumberOccured.append('2') 
                    if d3Index!=56: 
                        if d3Index>0 or d3Initialized==True:
                            print("Enter 3 to Move D3")
                            randomDiceNumberOccured.append('3')
                    if d4Index!=56:
                        if d4Index>0 or d4Initialized==True:
                            print("Enter 4 to Move D4")
                            randomDiceNumberOccured.append('4')
            while True:
                if d1Index==56 and d2Index==56 and d3Index==56 and d4Index==56:
                    return
                # player4DiceChoice = input("Enter Your Choice :")
                if randomDiceRoll==True and len(randomDiceNumberOccured)==0:
                    return
                while True:
                    player4DiceChoice = input("Enter Your Choice player4:")
                    if diceRollSix==True:
                        if player4DiceChoice in playerSixChoice:
                            playerSixChoice=[]
                            break
                        else:
                            print("Please Enter a valid Choice in sixer")
                    elif randomDiceRoll==True:
                        if player4DiceChoice in randomDiceNumberOccured:
                            randomDiceNumberOccured=[]
                            break
                        else:
                            print("Please Enter a valid choice in random Number ")
                    else:
                        if player4DiceChoice not in ['1','2','3','4']:
                            print("Please Enter a valid Choice Only between 1 to 4") 
                        else:
                            break
                if player4DiceChoice=="d1":
                    print("Player d1 initialized")
                    mapping4(0,posLeft,'d1')
                    d1Initialized=True
                    break
                if player4DiceChoice=="d2":
                    print("player d2 initialized")
                    mapping4(0,posLeft,'d2')
                    d2Initialized=True
                    break
                if player4DiceChoice=="d3":
                    print("player d3 initialized")
                    mapping4(0,posLeft,'d3')
                    d3Initialized=True
                    break
                if player4DiceChoice=="d4":
                    print("player d4 initialized")
                    mapping4(d1Index,posLeft,'d4')
                    d4Initialized=True
                    break
                if player4DiceChoice.isnumeric():
                    player4DiceChoice=int(player4DiceChoice)
                    if player4DiceChoice==1:
                        d1Initialized=True
                        d1Index+=player4Dice
                        if (d1Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'d1')                                                
                            mapping4(d1Index,posLeft,'d1')                            
                        elif d1Index>=5 and d1Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'d1')                            
                            mapping4(d1Index,posUp,'d1')
                        elif d1Index>=18 and d1Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'d1')                            
                            mapping4(d1Index,posRight,'d1')
                        elif d1Index>=31 and d1Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'d1')                            
                            mapping4(d1Index,posDown,'d1')
                        elif d1Index>=44 and d1Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'d1')                            
                            if d1Index==56:
                                mapping4(d1Index,posWin,'d1')
                            else:
                                mapping4(d1Index,posLeft,'d1') 
                            if d1Index==56 and d2Index==56 and d3Index==56 and d4Index==56:
                                    print("\t\t****  Player 4 Wins  ****")
                                    return
                            elif d1Index==56:
                                print("Congratulation d1 is at home")
                                if player4Dice!=6:
                                    return
                        else:
                            print("Your Cookie will not move Ahead")
                        
                    if player4DiceChoice==2:
                        d2Initialized=True
                        d2Index+=player4Dice
                        if (d2Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'d2')                                             
                            mapping4(d2Index,posLeft,'d2')                            
                        elif d2Index>=5 and d2Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'d2')                            
                            mapping4(d2Index,posUp,'d2')
                        elif d2Index>=18 and d2Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'d2')                            
                            mapping4(d2Index,posRight,'d2')
                        elif d2Index>=31 and d2Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'d2')                            
                            mapping4(d2Index,posDown,'d2')
                        elif d2Index>=44 and d2Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'d2')                            
                            if d2Index==56:
                                mapping4(d2Index,posWin,'d2')
                            else:
                                mapping4(d2Index,posLeft,'d2')
                            if d1Index==56 and d2Index==56 and d3Index==56 and d4Index==56:
                                    print("\t\t****  Player 4 Wins  ****")
                                    return
                            elif d2Index==56:
                                print("Congratulation d2 is at home")
                                if player4Dice!=6:
                                    return
                        else:
                            print("Your Cookie will not move Ahead")
                        
                    if player4DiceChoice==3:
                        d3Initialized=True
                        d3Index+=player4Dice
                        if (d3Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'d3')                                                
                            mapping4(d3Index,posLeft,'d3')                            
                        elif d3Index>=5 and d3Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'d3')                            
                            mapping4(d3Index,posUp,'d3')
                        elif d3Index>=18 and d3Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'d3')                            
                            mapping4(d3Index,posRight,'d3')
                        elif d3Index>=31 and d3Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'d3')                            
                            mapping4(d3Index,posDown,'d3')
                        elif d3Index>=44 and d3Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'d3')                            
                            if d3Index==56:
                                mapping4(d3Index,posWin,'d3')
                            else:
                                mapping4(d3Index,posLeft,'d3')
                            if d1Index==56 and d2Index==56 and d3Index==56 and d4Index==56:
                                    print("\t\t****  Player 4 Wins  ****")
                                    return
                            elif d3Index==56:
                                print("Congratulation d3 is at home")
                                if player4Dice!=6:
                                    return
                        else:
                            print("Your Cookie will not move Ahead")
                        
                            
                    if player4DiceChoice==4:
                        d4Initialized=True
                        d4Index+=player4Dice
                        if (d4Index<=4):
                            removeSpecificCharacterFromSafePosition(posLists,'d4')                                                
                            mapping4(d4Index,posLeft,'d4')                            
                        elif d4Index>=5 and d4Index<=17:
                            removeSpecificCharacterFromSafePosition(posLists,'d4')                            
                            mapping4(d4Index,posUp,'d4')
                        elif d4Index>=18 and d4Index<=30:
                            removeSpecificCharacterFromSafePosition(posLists,'d4')                            
                            mapping4(d4Index,posRight,'d4')
                        elif d4Index>=31 and d4Index<=43:
                            removeSpecificCharacterFromSafePosition(posLists,'d4')                            
                            mapping4(d4Index,posDown,'d4')
                        elif d4Index>=44 and d4Index<=56:
                            removeSpecificCharacterFromSafePosition(posLists,'d4')                            
                            if d4Index==56:
                               mapping4(d4Index,posWin,'d4') 
                            else:
                                mapping4(d4Index,posLeft,'d4')
                            if d1Index==56 and d2Index==56 and d3Index==56 and d4Index==56:
                                    print("\t\t****  Player 4 Wins  ****")
                                    return
                            elif d4Index==56:
                                print("Congratulation d4 is at home")
                                if player4Dice!=6:
                                    return                               
                        else:
                            print("Your Cookie will not move Ahead")                        
                    break                    
                else:
                    print("Please Provide a valid Input")
            if player4Dice==6:
                playerTurn("player4")
           
            if (a1Index==0 and a2Index==0 and a3Index==0 and a4Index==0) or (c1Index==0 and c2Index==0 and c3Index==0 and c4Index==0) or(b1Index==0 and b2Index==0 and b3Index==0 and b4Index==0) :
                return
            else:
                player1Turn()                
                             
#player chance one By One
def playerChoice(playerChoiceSelect):
    
    while True:        
        if a1Index==0 and a2Index==0 and a3Index==0 and a4Index==0:
            print("Player 1 start:")
            diceNumber=input("Press enter to Roll the dice Player1 :")  
            diceNumber=int(diceNumber)  
            # diceNumber=random.randrange(7)
            print("Your Dice Number :",diceNumber)
            if(diceNumber==6):
                print("Player 1 Game Start")
                playerTurn("player1",playerChoiceSelect)            
        
        else:        
             playerTurn("player1",playerChoiceSelect)            
            
        if b1Index==0 and b2Index==0 and b3Index==0 and b4Index==0:
            print("Player 2 start:")
            diceNumber=int(input("Press enter to Roll the dice Player2 :"))      
            # diceNumber=random.randrange(7)
            print("Your Dice Number :",diceNumber)
            if(int(diceNumber)==6):
                print("Player 2 Game Start")
                playerTurn("player2",playerChoiceSelect)          
        
        else:                    
            playerTurn("player2",playerChoiceSelect)   
            
        if playerChoiceSelect==3 or playerChoiceSelect==4:   
            if c1Index==0 and c2Index==0 and c3Index==0 and c4Index==0:
                print("Player 3 start:")
                diceNumber=int(input("Press enter to Roll the dice player3 :"))       
                # diceNumber=random.randint(1,6)
                print("I have selected player ",playerChoiceSelect)
                print("Your Dice Number :",diceNumber)
                if(int(diceNumber)==6):
                    print("Player 3 Game Start")
                    playerTurn("player3",playerChoiceSelect)        
                    
            else:        
                playerTurn("player3",playerChoiceSelect)
           
        if playerChoiceSelect==4:    
            if d1Index==0 and d2Index==0 and d3Index==0 and d4Index==0:
                print("Player 4 start:")
                diceNumber=int(input("Press enter to Roll the dice player4 :"))        
                # diceNumber=random.randrange(7)
                print("Your Dice Number :",diceNumber)
                if(int(diceNumber)==6):
                    print("Player 4 Game Start")
                    playerTurn("player4",playerChoiceSelect)            
            
            else:        
                playerTurn("player4",playerChoiceSelect)
                
def startGame():
    print("Welcome to the Ludo Game ")
    ludoGameUI()
    while True:
        print("Enter 2 to have 2 player Game ") 
        print("Enter 3 to have 3 player Game ")
        print("Enter 4 to have 4 player Game ")  
        userplayerChoice = input("Enter Your Choice : ")     
        
        if userplayerChoice in ['2','3','4']:
            if userplayerChoice=='2':
                print("2 player")  
                playerChoice(2) 
                break       
            elif userplayerChoice=='3':
                print("3 player choice")
                playerChoice(3)
                break
            elif userplayerChoice=='4':
                print("4 player game")
                playerChoice(4)
                break                
        else:
            print("please enter a valid choice")
startGame()     
    
            
        
     
        

     
     
     