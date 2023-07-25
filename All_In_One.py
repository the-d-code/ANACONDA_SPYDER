


=====================================LECTURE 1=============================================================================================


// ------- msg print---------------------------

       
        msg="welcome to pythone.."
        print (msg)

// -----Input and print with string--------------------------

        
        val=int(input("enter a value"))
        print("welcome {}".format(val))
        print(type(val))


// -------User define function----------------

                
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

============= 22/7/23 ========================================== LECTURE 2 =============================================================================================

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
         
                        tuple1=(1,2,5.0,"Hello")
                        tuple.append(100)
                        print(tuple1[-1])
                        
                                type(mylist)
                                Out[20]: list
                        
                // ------reverse the item-------------------

                        mylist=[[1,2,3],["Hemali","Devanshi","D"]]
                        mylist.reverse()
                        print(mylist)
                        
                                runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                [['Hemali', 'Devanshi', 'D'], [1, 2, 3]]

                // ------sorting the item-------------------

                        mylist=[10,20,30,40,50,60,1000,250]
                        l1=sorted(mylist)
                        print(l1)
                        
                                runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                [10, 20, 30, 40, 50, 60, 250, 1000]

                // ------for loop the item-------------------

                        mylist=[10,20,30,40,50,60,1000,250]
                        for i in mylist:
                            print(i)
                                
                                runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                10
                                20
                                30
                                40
                                50
                                60
                                1000
                                250

        
                        // ------multi the item-------------------

                        mylist=[10,20,30,40,50,60,1000,250]
                        for i in mylist:
                            print(i*2)
                        
                                runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                20
                                40
                                60
                                80
                                100
                                120
                                2000
                                500


============= 25/7/23 ========================================== LECTURE 3 =============================================================================================
  
// ------Dictionary-----------

                // ------Create & Print Dictionary-----------
                     
                     mydict={1:10,2:30,3:50}
                     print(mydict)
                     
                     mydict1={'A':10,'B':30,'C':50}
                     print(mydict1)
                     
                     mydict2={'A':"HELLO",'B':"Python",'C':"Program"}
                     print(mydict2)


                            runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                            {1: 10, 2: 30, 3: 50}
                            {'A': 10, 'B': 30, 'C': 50}
                            {'A': 'HELLO', 'B': 'Python', 'C': 'Program'}


                // -------------------------
                     mydict3={'A':"HELLO",'B':"Python",'C':"Program",3:3.5}
                     print(mydict3)
                     print(mydict3['A'])
                     
                     runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                     {'A': 'HELLO', 'B': 'Python', 'C': 'Program', 3: 3.5}
                     HELLO

                // ---VALUE FROM DICTIONARY----------------

                     mydict3={'A':"HELLO",'B':"Python",'C':"Program",3:3.5}
                     print(mydict3.values())
                     
                            runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                            dict_values(['HELLO', 'Python', 'Program', 3.5])

                // ------Dictionary from dictionary-----------
                     mydict3={'A':"HELLO",'B':"Python",'C':"Program",3:{1:10,2:30,3:50}}
                     print(mydict3.values())
                     
                            runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                            dict_values(['HELLO', 'Python', 'Program', {1: 10, 2: 30, 3: 50}])
 
                // ------View sub dictionary----------

                     mydict3={'A':"HELLO",'B':"Python",'C':"Program",3:{1:10,2:30,3:50}}
                     print(mydict3[3])
                     
                            runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                            {1: 10, 2: 30, 3: 50}

                // ------Delete bfrom dictionary---------
                     mydict3={'A':"HELLO",'B':"Python",'C':"Program",3:{1:10,2:30,3:50}}
                     del(mydict3[3])
                     print(mydict3)
                     
                            runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                            {'A': 'HELLO', 'B': 'Python', 'C': 'Program'}

                // -------create empty dictionry --------
                     mydict=dict()
                     print(mydict)
                     
                            runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                            {}

                 // -------create empty dictionry and asssigne value--------
                     mydict=dict()
                     mydict={'A':"HELLO"}
                     print(mydict)
                     
                            runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                            {'A': 'HELLO'}

                  
// ------SETS-------------------

                // -----Create and Print sets-------------
                     S1={1,2,3,4,5,6,7,8}
                     print(S1)
                     
                            runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                            {1, 2, 3, 4, 5, 6, 7, 8}

                // -----Find union--------------
                     S1={1,3,5,7,9}
                     S2={2,4,6,8,10,12,15}
                     print(S1.union(S2))
                     
                            runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                            {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15}
                      
                // -------Inter section--------------

                     S1={1,3,4,5,6,7,8}
                     S2={2,4,6,8,10,12,15}
                     print(S1.intersection(S2))
                            
                            runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                            {8, 4, 6}

                // ------Diffrenece----------

                     S1={1,3,4,5,6,7,8}
                     S2={2,4,6,8,10,12,15}
                     print(S1.difference(S2))
                     
                                   runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                   {1, 3, 5, 7}

                     S1={1,3,4,5,6,7,8}
                     S2={2,4,6,8,10,12,15}
                     print(S2.difference(S1))
                     
                                   runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                   {2, 10, 12, 15}
                                           
                // ------symmetric difference-----------
                     S1={1,3,4,5,6,7,8}
                     S2={2,4,6,8,10,12,15}
                     print(S1.symmetric_difference(S2))
                     
                                   runfile('B:/ICT3-1/SPYDER/ARRAY.py', wdir='B:/ICT3-1/SPYDER')
                                   {1, 2, 3, 5, 7, 10, 12, 15}




// ------ Class ------------

                // -------------------------


                // -------------------------
 
                // -------------------------

                // -------------------------

                // -------------------------

                // -------------------------
 
                // -------------------------

                // -------------------------
 
                // -------------------------

                // -------------------------

                // -------------------------

                // -------------------------
 
                // -------------------------

                // -------------------------

 






