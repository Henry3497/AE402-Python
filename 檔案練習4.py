file = open("images.png","rb")
a = file.read()
file.close()
file = open("複製.png","wb")
file.write(a)
file.close()
            
