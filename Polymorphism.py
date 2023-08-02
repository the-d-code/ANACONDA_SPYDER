// ---run time polymorphism-------------

                     class abc:
                         def show(self):
                             print("Welcome")
                     
                     class xyz(abc):
                         def show(self):
                             print("xyz class method...")
                             
                     obj=any
                     
                     obj1=abc()
                     obj=obj1
                     obj.show()
                     
                     obj2=xyz()
                     obj=obj2
                     obj.show()
                     
                     
                                   runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
                                   Welcome
                                   xyz class method...
