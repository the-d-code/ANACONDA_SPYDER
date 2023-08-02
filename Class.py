// ------ Class ------------

                // -----Create class and Print value----------------
                                   class abc:
                                       def show():
                                           print("First python class")
                                   
                                   obj=abc()
                                   abc.show()
                                   
                                                 runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                                 First python class
              
                                                   
                         // ---------- class using constructor-------------
                                   
                                          class abc:
                                              def show(self):
                                                  print("First python class")
                                          
                                          obj=abc()
                                          obj.show()
              
                                                        runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                                        First python class
                                                        
                // --------Take static input--------------
                     class abc:
                         def __init__(self,name):
                             self.name=name
                         def show(self):
                             print("Welcome",self.name)
                     
                     obj=abc("Devanshi")
                     obj.show()
                     
                                   runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                   Welcome Devanshi
                                          

                                          
                // ------Create method and print it-----------

                     class abc:
                         def show(self):
                             print("Welcome")
                     
                     class xyz(abc):
                         def disp(self):
                             print("xyz class method...")
                             
                     obj1=xyz()
                     obj1.show()
                     obj1.disp()
                            
                                   runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
                                   Welcome
                                   xyz class method...

                // --------Method over loading -------
                     class abc:
                         def show(self):
                             print("Welcome")
                     
                     class xyz(abc):
                         def show(self):
                             print("xyz class method...")
                             
                     obj1=xyz()
                     obj1.show()
                     
                                   runfile('B:/ICT3-1/OTHER STUUF/SPYDER/ARRAY.py', wdir='B:/ICT3-1/OTHER STUUF/SPYDER')
                                   xyz class method...


                
