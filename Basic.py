# In main file
# import script1
# print(script1.sum(1, 3))

// -------------------------------------------

        msg print
        msg="welcome to pythone.."
        print (msg)

// -------------------------------------------

        Input and print with string
        val=int(input("enter a value"))
        print("welcome {}".format(val))
        print(type(val))


// -------------------------------------------

                # User define function
                  # declare function
                def myf(str):
                  # str=print("Welcome to python...")
                  print(str)
                  
                print("my first python function..")
                   
                  # call myf function
                myf("Welcome")
        
        
                  Output:
                  
                  my first python function..
                  Welcome
               // -------------------------------------------
                
                  # User define function
                  # declare function
                def myf(str,str1):
                  # str=print("Welcome to python...")
                  print(str,str1)
                  
                print("my first python function..")
                   
                  # call myf function
                myf("Welcome","python")
                
                Output:
                
                my first python function..
                Welcome python

// -------------------------------------------
                mylist=[10,30,40,20,50,20,40]
                print(mylist)
                
                        Output:
                        [10, 30, 40, 20, 50, 20, 40]
                
                // -------------------------------------------
        
                mylist=[10,30,40,20,50,20,40, "python",5.5]
                print(mylist)
        
                        Output:
                        [10, 30, 40, 20, 50, 20, 40, 'python', 5.5]
                
                // ---------positive index----------------
        
                mylist=[10,30,40,20,50,20,40, "python",5.5]
                print(mylist[0])
        
                        Output:
                        10
                
                // ---------nagetive index----------------
        
                mylist=[10,30,40,20,50,20,40, "python",5.5]
                print(mylist[-2])
        
                        Output:
                        python
                
               // ---------between index----------------
        
                mylist=[10,30,40,20,50,20,40, "python",5.5]
                print(mylist[2:6])
        
                        Output:
                        [40, 20, 50, 20]
                                
                // ---------between index----------------
        
                mylist=[10,30,40,20,50,20,40, "python",5.5]
                print(mylist[2:-2])
        
                       Output:
                        [40, 20, 50, 20, 40]
        
                // ---------length of list----------------
        
                mylist=[10,30,40,20,50,20,40, "python",5.5]
                print(len(mylist))
        
                       Output:
                        9
        
                // ---------type of list----------------
        
                mylist=[10,30,40,20,50,20,40, "python",5.5]
                print(type(mylist))
        
                       Output:
                       <class 'list'>  
        
                // ---------sum of list----------------
        
                mylist=[10,30,40,20,50,20,40]
                print(type(mylist))
        
                       Output:
                       210
        
                // ---------max of list----------------
        
                mylist=[10,30,40,20,50,20,40]
                print(max(mylist))
        
                       Output:
                       50
                
                // ---------max of list----------------
                mylist=[10,30,40,20,50,20,40]
                mylist[0]=100
                print(mylist)
        
                        Output:
                        [100, 30, 40, 20, 50, 20, 40]
                
                // ---------max of list----------------
                mylist=[10,30,40,20,50,20,40]
                mylist.remove(50)
                print(mylist)
                
                        Output:
                        [10, 30, 40, 20, 20, 40]



 // ----------Array-----------------  
        
                        mylist=[[1,2,3],["Hemali","Devanshi","D"]]
                        print(mylist[1][1])
                
                                runfile('C:/Users/admin/untitled0.py', wdir='C:/Users/admin')
                                Devanshi
      
                // ------Insert the item-------------------
                                
                        mylist=[[1,2,3],["Hemali","Devanshi","D"]]
                        mylist.append("NEW")
                        print(mylist)
        
                                runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                [[1, 2, 3], ['Hemali', 'Devanshi', 'D'], 'NEW']

                 // ------Insert the item-------------------
                        
                        mylist=[[1,2,3],["Hemali","Devanshi","D"]]
                        mylist.insert(0,100)
                        print(mylist)
                        
                                runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                [100, [1, 2, 3], ['Hemali', 'Devanshi', 'D']]

                // ------Revome the item-------------------

                        mylist=[[1,2,3],["Hemali","Devanshi","D"]]
                        mylist.insert(0,100)
                        list1=mylist
                        mylist.remove(100)
                        print(list1)

                                runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                [[1, 2, 3], ['Hemali', 'Devanshi', 'D']]


// ------TUPPLE-------------------

                        tuple1=(1,2,5.0,"Hello")
                        print(tuple1)
                        
                                runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                (1, 2, 5.0, 'Hello')

                // ------retrive the item-------------------

                        tuple1=(1,2,5.0,"Hello")
                        print(tuple1[-1])
                        
                                runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                Hello

                        tuple1=(1,2,5.0,"Hello")
                        print(tuple1[2])
                        
                                runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                5.0

        
                // ------Replace the item-------------------





                // ------Revome the item-------------------

                // ------Replace the item-------------------
                // ------Revome the item-------------------


                // ------Replace the item-------------------
                // ------Revome the item-------------------






