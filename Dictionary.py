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

                  
