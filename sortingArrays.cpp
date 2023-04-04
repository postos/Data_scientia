//Paul Ostos
//Sorting Arrays 

#include <iostream>
using namespace std;

void bubbleSort(int num[], int size){
    int temp;
    //compare and sort
    for (int i = 0; i < size -1 ; i++){
        for (int j = 0; j < size -i -1; j++){
            if (num[j] > num[j+1]){
                temp = num[j];
                num[j] = num[j+1];
                num[j+1] = temp;

                for (int k = 0; k < size; k++){
                    cout << num[k] << " ";
                }
                cout << endl; //go to next line after each iteration of the loop
            }
        }
    }
}

void selectionSort(int num[], int size){

    // compare and sort 
    int low, temp; 
    for (int i = 0; i < size -1; i++){
        low = i;
        for (int j = i +1; j < size; j++){
            if(num[j] < num[low]){
                low = j;
            }
        }
            temp = num[low];
            num[low] = num[i];
            num[i] = temp;

            //show every step of the sort  
            for (int k = 0; k < size; k++){
                cout << num[k] << " ";
            }
            cout << endl; //go to next line after each iteration of the loop
    }
}

int main(){

    int arraySize = 10;
    int nums1[arraySize];
    int nums2[arraySize];

    // populate nums1 array
    for (int i = 0; i < arraySize; i++){
        nums1[i] = rand()%50;
    }

    //display nums1 array before sorting
    cout << "\nArray before the sort: " << endl;  
    for (int k = 0; k < arraySize; k++){
        cout << nums1[k] << " ";
    }
    cout << endl;

    //display nums 1 array being sorted
    cout << "\nSorting array using selection sort: " << endl; 
    selectionSort(nums1, arraySize);

    for (int i = 0; i < arraySize; i++){
        cout << nums1[i] << " ";
    }

    // populate nums2 array
    for (int i = 0; i < arraySize; i++){
        nums2[i] = rand()%50;
    }
    cout << endl;
    
    //display nums2 array before sorting
    cout << "\nArray before the sort: " << endl;  
    for (int k = 0; k < arraySize; k++){
        cout << nums2[k] << " ";
    }
    cout << endl;

    //display nums 2 array being sorted
    cout << "\nSorting array using bubble sort: " << endl; 
    bubbleSort(nums2, arraySize);

    for (int i = 0; i < arraySize; i++){
        cout << nums2[i] << " ";
    }

    return 0;
}