import random
import csv
import time

#csv filepath
filepath = "E:/PythonScripts/nusas_custom_fortune_cookie.csv"

def main():
    print('-'*10+'Fortune Cookie Simulator v2'+'-'*10)
    print(' '*15+'by Julian Cheung\n')
    cookie_new()
    print('Loading')
    time.sleep(1)
    delay()
    menu()

def menu():
    keypress = input('Press \'ENTER\' to open a random fortune cookie!\n')
    if keypress == "":
        rand_draw()
    else:
        menu()
    
def rand_draw():
    print('Opening fortune cookie...\n')
    delay()
    cookie_open()
    #read csv into list
    with open(filepath,newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        #generate random choice from data
        pick = random.choice(data)
        output = '*** ' + pick[0] + ' ***'
        print(output,'\n')
        print('~'*80,'\n')
    menu()

def delay():
    for i in range(0,3):
        print('.')
        time.sleep(1)
    print('\n')

def cookie_new():
    print(r"""                                                            
                       ..,,*******                      
                 .**..,,,,**(%#/**,**                   
            .*/*.....,,*,,**&%#(/******                 
          **,,,,,...,,*,,**/&%#(/***,,**,               
         ,*,,,.,,.,,,**,***#&%#(/*********,             
        ,**,,,...,,********(&%##(/*/***,****            
       ,.**,,,,,***********/&%#(((//***,****/,          
       ,,***********//*****/%%##((****,*****///         
        ,,**/*******///*****%%%##(/****,******/*        
        .*.**///*****///****%%%##(/***********/,        
         .,,//////*****/****   %#(//********/(*         
           ..,*((///*******/       ,/*/*******          
         ......,//////*****            (/(/**           
        .  ....,(%**////**                              
     ... ....     **(*//                                
   . ......                                             
      ...
      
    """)

def cookie_open():
    print(r"""                                                                     
                    ,*#/*.                                  .......   
                 .,.,,,(#*/,                         ...............  
               .,..,,,,*//%#(/*                .....................    
              ,,...,,,,***(&%##(*       ............ / .............. 
            ,,....,,,,,,**//*......     .....  %.. .............      
          ,,,,...,,,,,,*******.....   %.*#%  ...  %#........          
        ..,.....,,,,,,,******//.......   . #%  . ....                 
       ,,,....,,,,,,,,,********/... ...  .....                        
     ,,,,,...,,,,,,,,***********(.,       */*(###/*,,,,,              
   ,,,,,,,,,,,,,**,*************,/(.    ,***/****//&@@&%**..          
  ,*,,,,*********,***,**,********,,    ***/**/////*,**#&&&%/*,        
    /,****/////((((/**,,..           .*************/**,**&&&%#*,      
       .,,,,,...                    ,,,,,,,,,,,******/*,,/(&&%%#**    
                                  .,,,,,,,,,,,,,,******/****%%%##(,   
                                  ,*,,,,,,,,,,,,*,,******/***/%%%#(.  
                                     ....,*/*,,,,,,,,,*********###(,  
                                                  ...,,***,***/**/#.  
                                                                      
                                                                      
    """)
main()
