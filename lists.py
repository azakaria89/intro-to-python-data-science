__author__ = "Ahmed Zakaria"

def main():
    areas_1=["bedroom",10.5,"Hallway",15,"Living Room",12.8] #creation of lists, lists can hold any types even lists

    #list of lists
    areas_2=[["bedroom",10.5],["Hallway",15],["Living Room",12.8]]

    #printing type of areas
    print (type(areas_1))

    #slicing list[ begin:end-1]
    print(areas_1[0:2]) #to print the first two elements
    print(areas_1[:]) #print the whole list
    print(areas_1[:3]) #print the first 3 elements, if the begin index not mentioned , assumed 0

    #deletion
    del(areas_1[0])
    del(areas_2[0][1]) #delete the 2nd element of first list in areas_2

    #updating
    bathroom=["bathroom",8.0]
    areas_1=areas_1+bathroom #add the bathroom list elements to the areas_1
    areas_2=areas_2+bathroom
    areas_1[0]="BEDROOM"  #modify

    #referencing and copying
    areas_1_copy = areas_1   #copying the address of areas_1 to be the new address of areas_1_copy which means both referes to the same memory space
    areas_1_copy[0]="no"
    print (areas_1) #areas_1 will also change exactly like areases
    print(areas_1_copy)

    # Right way to copy
    areas_2_copy= list(areas_2)
    # or another way by cpying the values
    areas_2_copy=areas_2[:]
    del(areas_2_copy[0])
    print (areas_2_copy)
    print ("*************")
    print(areas_2)
if __name__ == "__main__":
    main()