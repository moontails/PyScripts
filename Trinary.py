class Trinary_Tree:
    def __init__(self, val=None):
        self.value = val
        self.left_child = None
        self.middle_child = None
        self.right_child = None
    
    def insert_Left(self, value):
        #Base Case
        if self.left_child == None:
            self.left_child = Trinary_Tree(value)
        else:
            if value < self.left_child.value:
                self.left_child.insert_Left(value)
            elif value == self.left_child.value:
                self.left_child.insert_Middle(value)
            else:
                self.left_child.insert_Right(value)
        
    def insert_Middle(self, value):
        #Base Case
        if self.middle_child == None:
            self.middle_child = Trinary_Tree(value)
        else:
            if value < self.middle_child.value:
                self.middle_child.insert_Left(value)
            elif value == self.middle_child.value:
                self.middle_child.insert_Middle(value)
            else:
                self.middle_child.insert_Right(value)
                
    def insert_Right(self, value):
        # Base Case
        if self.right_child == None:
            self.right_child = Trinary_Tree(value)
        else:
            if value < self.right_child.value:
                self.right_child.insert_Left(value)
            elif value == self.right_child.value:
                self.right_child.insert_Middle(value)
            else:
                self.right_child.insert_Right(value)
    
    def display(self):
        if self.value == None:
            return
        print str(self.value) + "\t"
        if self.left_child != None:
            self.left_child.display()
        if self.middle_child != None:
            self.middle_child.display()
        if self.right_child != None:
            self.right_child.display()
        
if __name__ == "__main__":
    # A List to store the input numbers and a choice variable to keep track of the input
    numbers = []
    choice = 'Y'
    
    while ( choice == 'Y' ) :
        numbers.append(int(raw_input("Enter the number: ")))
        choice = raw_input("Do you wish to continue [Y/N]: ")
        
    root = Trinary_Tree(numbers[0])
    
    n = len(numbers)
    for i in range(1,n):
        if numbers[i] < root.value:
            root.insert_Left(numbers[i])
        elif numbers[i] == root.value:
            root.insert_Middle(numbers[i])
        else:
            root.insert_Right(numbers[i])
    
    root.display()
