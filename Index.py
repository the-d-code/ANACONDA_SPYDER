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
