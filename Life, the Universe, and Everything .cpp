//Code is in C++
#include <iostream>
using namespace std;
int main()
{
    int a;
    do//We use a do-While and not just a while loop because the input command is inside the loop.
    {
        cin>>a;
        if(a!=42&&a<100&&a>(-100))//Prints number only if it is not equal to 42 and not more than two digits
        cout<<a<<"\n";
    }
    while(a!=42&&a<100&&a>(-100));//The loop will continue only if the number is not equal to 42 and not more than two digits
}
