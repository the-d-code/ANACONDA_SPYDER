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


