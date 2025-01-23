import os
if __name__=='__main__':
    print("Hello, I am Diva a robo speaker.")
    print('Type "Stop" to stop this robo')
    while True:
        x=input("Enter what you want me to speak: ")
        
        if(x=="Stop"):
            os.system("say 'Nice to meet you, bye bye'")
            break
        command=f"say {x}"
        os.system(command)
