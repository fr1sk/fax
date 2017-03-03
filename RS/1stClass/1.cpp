#include <vector>
#include <list>
#include <iostream>
#include <numeric>

// namespace std{
//     sort
// }
//
// namespace boost{
//     sort
// }
//namespace -- sluzi da ne dolazi do kolizije
//u zaglavljima nikad - u h nikad u cpp moze ali se ne preporucuje
double pomnozi(double x, double y){
    return x * y;
}

int main(int argc, char *argv[]){
    std::vector<double> numbers; //za razliku od jave on prima i obicne promenjive
    std::list<double> numbersList; //uvek koristimo vector, uvek, uvek, uvek, skoro nikad listu
    std::vector<std::complex<double>> numbersComplex;

    double sum = 0;
    double sumList = 0;

    double n;   //double mora van while
    while(std::cin >> n){ //cin se konvertuje u boolean pa moze da se koristi u if,while
                    // jedino false ako je u predhodnom citanju doslo do greske
                    //operator >> iz cin procitaj jedan double i gurni ga u n
                    // nema % kao u c-u vec na osnovu tipa promenjive zna koji tip treba da uzme
                    //nikako ne pozivamo 2 puta cin (u while i da odvojeno dodajemo u while)
        numbers.push_back(n);
        numbersList.push_back(n);
    }

    const int * p;
    p += 1; //ovo prolazi
    (*p) += 1;  //ovo ne, jer je pokazivac konstantan te se ne moze menjati

    int * const p;
    p += 1; //ovo ne
    (*p) += 1;  //ok

    const int * const p; //konstantan pokazivac na konstantu vrednos
    p += 1; //!ok
    (*p) += 1; //ok

    //iterator koji nije moguce menjati, ali mozemo menjati na sta iterator moze da pokazuje
    // const std::vector<double>::iterator i = ...;
    // std::vector<double>::const_iterator i = ...;
    // const std::vector<double>::const_iterator i = ...;


    //radimo ars
    //kolekcijska for petlja
    for(double number: numbers){
        sum +=number;
    }
    //reduce(par,numbers.begin(), numbers.end(), 1, pomnozi); -- parelelizacija
    //accumulate radi nad svim tipovima koji imaju iteratore
    //accumulate po defaultu poziva +
    double sum = std::accumulate(numbers.begin(), numbers.end(), 0);    //algoritam koji zna da sabere sve br u std bibl
    double mul = std::accumulate(numbers.begin(), numbers.end(), 1, pomnozi);
    const auto sumCompl = std::accumulate(numbers.begin(), numbers.end(), std::complex<double>(0));
    // pokazivaci, iteratori, na vrednost kojie ne mozemo da promenimo
        // numbers.cbegin();
        // numbers.cend();
    // pokazivaci, iteratori, koji idu u obrnutnom redosledu, i dalje sve ide preko ++ ali radi reverse, sa druge strane niza
        // numbers.cbegin();
        // numbers.cend();
    // kombinacija oba
        // numbers.crbegin();
        // numbers.crend();

    //za listu koristimo iterator
    //interno kolekcijska for petlja radi ovo, mozemo da je koristimo
    //auto automatski zakljucuje koji tip ce biti kojia promenjiva, jer automatski zna sta funkcija vraca
    auto begin = numbersList.begin(); //vraca iterator (magicni pokazivac na pocetak)
    auto end = numbersList.end(); // -||-   na kraj
    for (; begin != end; ++begin){
        sumList += *begin;
    }

    //obicna for petlja
    // double sum = 0;
    // for (size_t i=0; i<numbers.size(); i++){
    //     sum += numbers[i];
    // }

    //ovako bi koristili za implemetaciju auto
    //ovo ne koristi!!!
    // std::vector<double>::coust_iterator curr = numbers.cbegin();
    // const std::vector<double>::coust_iterator curr = numbers.cend();
    // while(curr!=end){
    //     sum += *curr;
    //     ++curr;
    // }

    std::cout
        << "preko vektora: "
        << (sum / numbers.size())
        << std::endl
        << '\n';    //backslash n isto kao std::endl

    std::cout
        << "preko liste: "
        << (sumList / numbersList.size())
        << std::endl
        << '\n';    //backslash n

    return 0;
}
