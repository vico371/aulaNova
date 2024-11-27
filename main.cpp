#include <iostream>
using namespace std;-

int main (){
    int idade;
    cout << "Digite a sua idade; ";
    cin >> idade;
    if (idade >= 18){
        cout << "voce pode ser preso";
    }
    else{
        cout << "voce vai pra FASE";
    }
    return 0;
}
