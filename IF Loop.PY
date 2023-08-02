// --------IF LOOP----------
 
                // ------Take input and print value----------------
                     class abc:
                         def show(self):
                             print("Welcome")
                     
                     class xyz(abc):
                         def show(self):
                             print("xyz class method...")
                             
                     obj=any
                     a=int(input("Enter a value 0 or 1 :"))
                     
                     if(a==0):
                         obj1=abc()
                         obj=obj1
                         obj.show()
                     if(a==1):
                         obj2=xyz()
                         obj=obj2
                         obj.show()
                     
                                   runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
                                   Enter a value 0 or 1 :1
                                   xyz class method...
                                   
                                   runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
                                   Enter a value 0 or 1 :0
                                   Welcome
