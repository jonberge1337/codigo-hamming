#include <iostream>

using namespace std;

int main(){
    int numero = 0;
	int prueba;
    while(numero < 100){
        cout << numero << " Esto es con el while" <<endl;
        numero++;
    }
    for(int i = 0; i < 100; i++){

        cout << i << " Esto es con el for" <<endl;

    }
	cout << "introduce un valor" << endl;
	cin >> prueba;
	cout << "Has introducido " << prueba << endl;
}
