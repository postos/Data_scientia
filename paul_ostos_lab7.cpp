//Paul Ostos

#include <iostream>
#include <cstdlib> //allow for the use the rand() function
#include <ctime> //allow for the use of the time function to set the seed value
using namespace std; 

class Coin{
    private: 
        //create member variable set to private 
        string sideUp;
    public: 
        //create a constructor to initialize the side that is facing up
        Coin(){
            srand((time(0))); //create a seed value using the current time
            int randomNum = rand() % 2; //use modulus to get a random number that will be 0 or 1
            if (randomNum == 0){
                sideUp = "Heads";
            }
            else{
                sideUp = "Tails";
            }
        }
        //create a coin toss simulator
        void toss(){
            int randomNum = rand() % 2;
            if (randomNum == 0){
                sideUp = "Heads";
            }
            else{
                sideUp = "Tails";
            }
        }
        //allow user to access the sideUp
        string getSideUp(){
            return sideUp;

        }
};

int main ()
{
    //initialize the constructor to get the initial sideUp
    Coin cointoss;
    cout << "\nIniticial coin side up: " << cointoss.getSideUp() << endl; 

    //start the counter at 0 for both heads and tails
    int heads = 0;
    int tails = 0;

    //run a for loop to loop through the toss() function 20 times
    for(int tossyToss = 1; tossyToss <=20; tossyToss++){
        cointoss.toss();
        if (cointoss.getSideUp() == "Heads"){
            heads++; //increment heads by 1 each time toss() is 0
        }
        else{
            tails++; //increment tails by 1 each time toss() is 1
        }
    }
    //display the number of times the coin landed on heads and tails
    cout << "\nNumber of times coin landed on heads: " << heads << endl;
    cout << "Number of times coin landed on tails: " << tails << endl;

    return 0; 
}