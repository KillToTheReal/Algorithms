#include <stdio.h>
#include <iostream>
#include <sstream> //istringstream
#include <vector>
#include <iterator>
using namespace std;

/*Смена местами слов под номером 1 с 2, 3 с 4, 5 с 6 и т.д в строке*/

void show_vector(vector<string>a_vec)
{
        for (vector<string>::iterator it = a_vec.begin() ; it!=a_vec.end() ; ++it) //Вывод по итераторам
                cout<<" "<<*it;
}

int main()
{
   string s;
   getline(cin,s); //Считывание строки
   istringstream str(s); //Обработка строки
   vector<string> words; //Контейнер для разбиения предложения на слова
   copy(istream_iterator<string>(str) , istream_iterator<string>() , back_inserter(words) ); //Заполнение контейнера словами при помощи итератора
   
   for(int i = 0; i<words.size()-1; i=i+2) //Смена местами начиная с 0 позиции с шагом в 2
   {
       string tmp;
        tmp = words[i];
        words[i] = words[i+1];
        words[i+1] = tmp;
   }
   
   show_vector(words);

    return 0;
}
