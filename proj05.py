
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
project 05
Different files with both vertices and faces
First two lines can disregard
The beginning has vertices
Any line beginning with 3 is faces
Create different functions that solve the following problems
Create a function that allows for a user to choose which of these functions
they would like to see

'''
  
import math

def display_options():
    ''' This function displayes the menu of options'''
    
    menu = '''\nPlease choose an option below:
        1- display the information of the first 5 faces
        2- compute face normal
        3- compute face area
        4- check two faces connectivity
        5- use another file
        6- exit
       '''
       
    print(menu)
    
def open_file():
    '''This function opens files and checks if they're valid'''
    '''Returns a boolean'''
    
    while True: #start try and except
        try:
            fp_str = input("Enter an <off> file name: ")
            fp = open(fp_str, 'r') #only reading
            return fp
            break #end loop
        except IOError: #error when file doesn't exist
            print("Error. Please try again")
            
def check_valid(fp,index,shape):
    '''This function checks if index or shape exists'''
    '''Returns a boolean'''
    
    fp.seek(0) #start from beginning of file
    fp.readline()
    fp.readline() #skip two lines 
    
    if shape != 'vertex': #make sure shape is valid
        if shape != 'face':
            return False
        
    if shape != 'face': #make sure shape is valid
        if shape != 'vertex':
            return False
    
    if index.isdigit(): #index has to be an int
        pass
    else:
        return False
    
    index = int(index)
    
    if index < 0: #cannot be a negative number
        return False
    
    vertex_line = 0
    face_line = 0
    
    for line in fp:
        while line[1] != '3':
            vertex_line += 1 #how many index in vertices
            break
        else:
            face_line += 1 #how many index in faces
            
    fp.seek(0)
        
    if shape == 'vertex': #check index is valid inside of vertex
        if index >= vertex_line: #if greater than vertex_line, invalid
            return False
        else:
            return True
               
    elif shape == 'face': #check index is valid inside of face
        if index >= face_line: #if greater than face_line, invalid
            return False
        else:
            return True       
    
def read_face_data(fp, index):
    '''Thie function finds three vertices that make the face'''
    '''Returns three integers'''
    
    fp.seek(0) #start at the top of file
    fp.readline() #skip first line
    for line in fp:
        while line[1] != '3':
            break #skip lines that don't start with 3 (they're vertices)
        else:
            if index == 0: #break would skip index 0
                int1 = int(line[6])
                int2 = int(line[11])
                int3= int(line[16])
                return int1, int2, int3
            break
    for i in range(index-1): #minus 1 from index since readline will skip the line you want to read
        fp.readline() #skip lines 
    face_line = fp.readline() #read line
    int1 = int(face_line[2:7]) #slice to get integers
    int2 = int(face_line[7:12])
    int3 = int(face_line[12:17])
    return int1, int2, int3
    

def read_vertex_data(fp, index):
    '''This function finds coordinates of the vertex'''
    '''Returns three floats'''
    
    fp.seek(0) #start from beginning
    fp.readline() #skip two lines
    fp.readline()
    for i in range(index):
        fp.readline() #skip lines until the line you want
    line = fp.readline() #read the line
    float1 = float(line[:15]) #slice to get floats
    float2 = float(line[15:30])
    float3 = float(line[30:])
    return float1, float2, float3

        
def compute_cross(v1,v2,v3,w1,w2,w3):
    '''This function computes cross between two vectors.'''
    '''Returns three floats'''
    
    float1 = (v2 * w3) - (v3 * w2) #used equation
    float2 = (v3 * w1) - (v1 * w3)
    float3 = (v1 * w2) - (v2 * w1)
    return round(float1, 5), round(float2,5), round(float3, 5) #round to five decimal places

def compute_distance(x1,y1,z1,x2,y2,z2):
    '''This function computes the Euclidian distance between two points.'''
    '''Returns one float'''
    
    float = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2) #used equation
    
    return round(float, 2) #round to two decimals

def compute_face_normal(fp, face_index):
    '''This function computes the normal vector of a face.'''
    '''Returns three floats'''
    
    fp.seek(0) #go to beginning of file
    first, second, third = read_face_data(fp, face_index)
    fp.seek(0) #go to beginning of file
    x1, y1, z1 = read_vertex_data(fp, first) #side a
    fp.seek(0) #go to beginning of file
    x2, y2, z2 = read_vertex_data(fp, second) #side b
    fp.seek(0) #go to beginning of file
    x3, y3, z3 = read_vertex_data(fp, third) #side c
    v1 = x2 - x1 #first vector (ab)
    v2 = y2 - y1
    v3 = z2 - z1
    w1 = x3 - x1 #second vector (ac)
    w2 = y3 - y1
    w3 = z3 - z1
    return compute_cross(v1,v2,v3,w1,w2,w3)

def compute_face_area(fp, face_index):
    '''This function computes the face area.'''
    '''Returns one float'''
    
    first, second, third = read_face_data(fp, face_index)
    fp.seek(0) #go to beginning of file
    x1, y1, z1 = read_vertex_data(fp, first) #side a
    fp.seek(0) #go to beginning of file
    x2, y2, z2 = read_vertex_data(fp, second) #side b
    fp.seek(0) #go to beginning of file
    x3, y3, z3 = read_vertex_data(fp, third) #side c
    
    
    ab = compute_distance(x1,y1,z1,x2,y2,z2) #ab
    ac = compute_distance(x1,y1,z1,x3,y3,z3) #ac
    bc = compute_distance(x2,y2,z2,x3,y3,z3) #bc
    
    p = (ab + ac + bc) / 2 #used equation
    
    area = math.sqrt(p*(p-ab)*(p-ac)*(p-bc))
    
    return round(area, 2) #round to two places


def is_connected_faces(fp, f1_ind, f2_ind):
    '''This function checks if faces are connected.'''
    '''Returns boolean'''
    
    fp.seek(0) #go to beginning of file
    #index 1 face
    first1, second1, third1 = read_face_data(fp, f1_ind)
    fp.seek(0) #go to beginning of file
    #index 2 face
    first2, second2, third2 = read_face_data(fp,f2_ind)
    fp.seek(0) #go to beginning of file
    
    true_statement = 0 #count how many faces are equal to eachother
    
    if first1 == first2:
        true_statement += 1
    if first1 == second2:
        true_statement += 1
    if first1 == third2:
        true_statement += 1
    if second1 == first2:
        true_statement += 1
    if second1 == second2:
        true_statement += 1
    if second1 == third2:
        true_statement += 1
    if third1 == first2:
        true_statement += 1
    if third1 == second2:
        true_statement += 1
    if third1 == third2:
        true_statement += 1
    
    if true_statement >= 2: #only connected if two faces are equal to eachother
        return True
    else:
        return False
        
def main():
    '''This function is used to display results, depending on user's input.'''
    
    print('''\nWelcome to Computer Graphics!
We are creating and handling shapes. Any shape can be represented by polygon meshes, 
which is a collection of vertices, edges and faces.''')
    
    fp = open_file() #open file
    
    display_options() #display options
    
    option = input(">> Choice: ") #prompt loop
    
    while option != '6': #6 will end loop
        
        if option == '1': #show first 5 face index
            
            fp.seek(0) #go to beginning of file
            #face 0:
            first0, second0, third0 = read_face_data(fp, 0)
            fp.seek(0) #go to beginning of file
            #face 1:
            first1, second1, third1 = read_face_data(fp, 1)
            fp.seek(0) #go to beginning of file
            #face 2:
            first2, second2, third2 = read_face_data(fp, 2)
            fp.seek(0) #go to beginning of file
            #face 3:
            first3, second3, third3 = read_face_data(fp, 3)
            fp.seek(0) #go to beginning of file
            #face 4:
            first4, second4, third4 = read_face_data(fp, 4)
            fp.seek(0) #go to beginning of file
            
            #printed statements:
            print("{:^7s}{:^15s}".format('face', 'vertices'))
            print("{:>5s}{:>5d}{:>5d}{:>5d}".format('0', first0, second0, third0))
            print("{:>5s}{:>5d}{:>5d}{:>5d}".format('1', first1, second1, third1))
            print("{:>5s}{:>5d}{:>5d}{:>5d}".format('2', first2, second2, third2))
            print("{:>5s}{:>5d}{:>5d}{:>5d}".format('3', first3, second3, third3))
            print("{:>5s}{:>5d}{:>5d}{:>5d}".format('4', first4, second4, third4))
            
            display_options()
            option = input(">> Choice: ") #prompt loop again
            
        if option == '2': #Show normal of face index of user's choice
            
            face_index = input("Enter face index as integer: ")
            while True:
                if check_valid(fp,face_index,'face'): #check if index is valid
                    face_index = int(face_index) #if it is valid, change to int
                    break
                else:
                    print("This is not a valid face index.")
                    face_index = input("Enter face index as integer: ") #prompt until valid index
                    
            face1, face2, face3 = compute_face_normal(fp, face_index)
            
            print("The normal of face {:d}:{:>9.5f}{:>9.5f}{:>9.5f}".format(face_index, face1, face2,face3))
            
            display_options()
            option = input(">> Choice: ") #prompt loop
            
        if option == '3': #area of face index of user's choice
            
            face_index = input("Enter face index as integer: ") 
            while True:
                if check_valid(fp,face_index,'face'): #check if input is valid
                    face_index = int(face_index) #change to int if valid
                    break
                else:
                    print("This is not a valid face index.")
                    face_index = input("Enter face index as integer: ") #prompt until valid loop
                    
            area = compute_face_area(fp, face_index)
            print("The area of face {:d}:{:>9.2f}".format(face_index, area))
            
            display_options()
            option = input(">> Choice: ") #prompt loop
            
        if option == '4': #check if faces of two index of the users choice are connected
            
            face_index1 = input("Enter face 1 index as integer: ") #index 1
            while True:
                if check_valid(fp,face_index1,'face'): #check if valid
                    face_index1 = int(face_index1) #change to int if valid
                    break
                else:
                    print("This is not a valid face index.")
                    face_index1 = input("Enter face 1 index as integer: ") #prompt until index is valid
            
            face_index2 = input("Enter face 2 index as integer: ") #index 2
            while True:
                if check_valid(fp,face_index2,'face'): #check if valid
                    face_index2 = int(face_index2) #change to int if valid
                    break
                else:
                    print("This is not a valid face index.")
                    face_index2 = input("Enter face 2 index as integer: ") #prompt until valid
                    
            if is_connected_faces(fp, face_index1, face_index2):
                print('The two faces are connected.') #if True
            else:
                print("The two faces are NOT connected.") #if False
            
            display_options()
            option = input(">> Choice: ") #prompt loop
            
        if option == '5': #open a different file
            
            fp = open_file() 
            
            display_options()
            option = input(">> Choice: ") #prompt loop
            
        #if put an invalid option:
        if option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6':
            print("Please choose a valid option number.")
            option = input(">> Choice: ") #prompt loop again
            
    else: #when user inputs 6
        print("Thank you, Goodbye!")
        fp.close() #close file
            
    
# Do not modify the next two lines.
if __name__ == "__main__":
    main()