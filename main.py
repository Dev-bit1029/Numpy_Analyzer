import numpy as np 


class NumpyAnalyzer :
    
    def __init__(self):
        self.data = None
        
    def Create(self):
        
        try:
            print("1. 1D Array ")
            print("2. 2D Array ")
            print("3. 3D Array ")
            
            
            choice = int(input("Enter The Number Between (1-3) :- "))
            
            if choice == 1:
                num = input("Enter The Number Of 1D Array:- ").split()
                arr = list(map(int,num))
                self.data = np.array(arr)
                print("")
                print(f"Element :- {self.data}") 
                print("Element Added Successfully !")
                return self.data
            
            elif choice == 2 :
                
                row = int(input("Enter The Number OF Row For 2D Array ;- "))
                cols = int(input("Enter The Number OF cols For 2D Array :- "))
                arr = input(f"Enter {row * cols} elements for the 2D array separated by spaces:- ").split()
                arr = list(map(int, arr))
                self.data = np.array(arr).reshape(row, cols)
                print("")
                print(f"Element :\n{self.data}")
                print("Element Added Successfully !")
                return self.data

            elif choice == 3 :
                   d = int(input("Enter The Number OF Depth For 3D Array :- "))
                   row = int(input("Enter The Number OF Row For 3D Array :- "))
                   cols = int(input("Enter The Number OF cols For 3D Array :-"))
                   arr = input(f"Enter {d * row * cols} elements for the 3D array separated by spaces:- ").split()
                   arr = list(map(int, arr))
                   self.data = np.array(arr).reshape(d, row, cols)
                   print("")
                   print(f"Element :\n{self.data}")
                   print("Element Added Successfully !")
                   return self.data

        except:
            print("Enter The Correct Number Of Element !")

    def indexing(self,data):
        try:
            
            while True:
                print(" Choose The Indexing Option ")
                print("1. Indexing Array ")
                print("2. Slicing Array ")
                print("3. Go Back To Main Menu ")
                
                choice = int(input("Enter The Number Between (1-3) :- "))
                if choice == 1:
                    if data.ndim == 1:
                        index = int(input("Enter The Index Of Element You Want To Access :- "))
                        print(f"Element At Index {index} : {self.data[index]}")
                    elif data.ndim == 2:
                        row = int(input("Enter The Row Index :- "))
                        col = int(input("Enter The Column Index :- "))
                        print(f"Element At Index ({row}, {col}) : {data[row, col]}")
                    elif data.ndim == 3:
                        depth = int(input("Enter The Depth Index :- "))
                        row = int(input("Enter The Row Index :- "))
                        col = int(input("Enter The Column Index :- "))
                        print(f"Element At Index ({depth}, {row}, {col}) : {data[depth, row, col]}")
                    else:
                        print("Invalid Array Dimension")
                elif choice == 2:
                    
                    print("Slicing The Array:")
                    
                    if data.ndim == 1:
                        start = int(input("Enter The Start Index :- "))
                        end = int(input("Enter The End Index :- "))
                        print(f"Sliced Array : {self.data[start:end]}")
                    elif data.ndim == 2:
                        row_start = int(input("Enter The Start Row Index :- "))
                        row_end = int(input("Enter The End Row Index :- "))
                        col_start = int(input("Enter The Start Column Index :- "))
                        col_end = int(input("Enter The End Column Index :- "))
                        print(f"Sliced Array :\n{self.data[row_start:row_end, col_start:col_end]}")
                        
                    elif data.ndim == 3:
                        depth_start = int(input("Enter The Start Depth Index :- "))
                        depth_end = int(input("Enter The End Depth Index :- "))
                        row_start = int(input("Enter The Start Row Index :- "))
                        row_end = int(input("Enter The End Row Index :- "))
                        col_start = int(input("Enter The Start Column Index :- "))
                        col_end = int(input("Enter The End Column Index :- "))
                        print(f"Sliced Array :\n{self.data[depth_start:depth_end, row_start:row_end, col_start:col_end]}")
                        
                    else:
                        print("Invalid Array Dimension")
                elif choice == 3:
                    print("Returning To Main Menu...")
                    break
                else:
                    print("Invalid Choice. Please Try Again.")
        except:
            print("Invalid Input Try Again!")
    
    def mathematical_operations(self, data):
        
        try :
            print("=========================================")
            print("Choose The Mathematical Operation ")
            print("=========================================")
            print("1. Addition ")
            print("2. Subtraction ")
            print("3. Multiplication ")
            print("4. Division ")
            
            choice = int(input("Enter The Number Between (1-4) :- "))
            
            if choice == 1:
                arr = input(f"Enter {data.size} elements for the second array separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data + arr2
                print(f"  {data} \n+ {arr2} \n= {result}")
                
                
            elif choice == 2:
                arr = input(f"Enter {data.size} elements for the second array separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data - arr2
                print(f"  {data} \n- {arr2} \n= {result}")
                
            elif choice == 3 :
                arr = input(f"Enter {data.size} elements for the second array separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data * arr2
                print(f"  {data} \n× {arr2} \n= {result}")
                
            elif choice == 4:
                arr = input(f"Enter {data.size} elements for the second array separated by spaces:- ").split()
                arr1 = list(map(int, arr))
                arr2 = np.array(arr1).reshape(data.shape)
                result = data / arr2
                print(f"  {data} \n÷ {arr2} \n= {result}")    
                
                
        except:
            print("Invalid Input Try Again !")
      
    def combine_array(self,data):
        try :
            print("===============")
            print("Enter The Choose ")
            print("===============")
            print("1.Combine Array")
            print("2. Split Array ")
            
            choice = int(input("Enter The Chioce Between (1-2):- "))
            
            if choice == 1:
                
                arr = input(f"Enter {data.size} Elements For Another Array :-  ").split()
                arr1 = list(map(int,arr))
                arr2 = np.array(arr1).reshape(data.shape)
                print(f"Original Data :- \n{data}")
                print(f"Second Array :- \n{arr2}")
                print("Combined Array (Vertical Stack):")
                new = np.vstack((data, arr2))
                print(new)
                
            elif  choice == 2 :
                
                arr1 = int(input("Enter The Number Of Split Array  :- "))
                arr2 = np.array_split(data,arr1)
                print(f"Original Array:- \n{data}")
                print(f"Split Array:- \n{arr2}")
                
            else:
                print("Invalid Choice between (1-2)")    
        except:
            print("Invalid Input Try Again !")

    def Search_array(self,data):
        
        try:
            print("=====================")
            print("Choose A Option ")
            print("=====================")
            print("")
            print("1. Search A Value")        
            print("2. Sort A Array ")        
            print("3. Filter Value ")
            
            choice = int(input("Enter The Choice Between (1-3) :- "))
            
            if choice == 1:
                print(f"Original Array :- {data}")
                search = int(input("Enter A value To Search For :- "))
                
                if search in data :
                    print("Value Found At Indexing :")
                    arr = np.where(data == search)
                    print(arr[0])
                else:
                    print("Value Not Found In The Array !") 
        
            elif choice == 2:
                print(f"Original Array :- {data}")
                sort_arr = np.sort(data)
                print(f"Sorted A Array :- {sort_arr}")
                
                
            elif choice == 3 :
                print("")
                print("Choose a filter:")
                print("1. Values less than")
                print("2. Values greater than")
                
                
                choice = int(input("Enter The Choice Between (1-2) :- "))
                value = int(input("Enter the threshold value:- "))
                
                if choice == 1 :
                    print(f"Original Array :- {data}")
                    print("Filter Data")
                    less = data[data<value]
                    print(f"Less Array :- {less}")
                    
                elif choice == 2:
                    print(f"Original Array :- {data}")
                    print("Filter Data")
                    greater = data[data<value]
                    print(f"Greater Array :- {greater}")
                    
                else:
                    print("Invalid Cjoice Between (1-2) !")
                                    
            else:
                print("Invalid Choice Between (1-3)")           
                    
        except:
            print("Invalid Input Try Again !")
        
        
    def Aggregates_operations(self, data):

        try:
  
            print()
            print("Choose an option:")
            print("1. Sum ")
            print("2. Mean")
            print("3. Median")

            choice = int(input("Enter your choice:- "))

            if choice == 1:
                print(f"Original array: - {data}")
                sum_arr = np.sum(data)
                print(f"Sum of all elements: \n{sum_arr}")

            elif choice == 2:
                print(f"Original array:- {data}")
                mean_arr = np.mean(data)
                print(f"Mean of all elements: \n{mean_arr}")

            elif choice == 3:
                print(f"Original array:- {data}")
                median_arr = np.median(data)
                print(f"Median of all elements: \n{median_arr}")

            else:
                print("Invalid choice Between (1-3)!")
        except:
            print("Invalid Input Try Again !")
        
        

while True:
    print("===================================")
    print("Welcome To The Numpy Analyzer ")
    print("===================================")
    
    print("1. Create A Numpy Array ")
    print("2. Perform Mathematical Operation ")
    print("3. Combine Or Split Array ")
    print("4. Search , Sort Or Filter Arrays ")
    print("5. Compute Aggregates And Statistics ")
    print("6. Exit......")
    
    choice = int(input("Enter The Number Between (1-6) :- "))
    
    if choice == 1:
        analyzer = NumpyAnalyzer()
        data = analyzer.Create()
        if data is not None:
            analyzer.indexing(data)
    elif choice == 2:
        analyzer.mathematical_operations(data)
    elif choice == 3:
        analyzer.combine_array(data)
    elif choice == 4:
        analyzer.Search_array(data)
    elif choice == 5:
        analyzer.Aggregates_operations(data)
    elif choice == 6:
        print("Exiting The Program. Goodbye!")
        break
    
