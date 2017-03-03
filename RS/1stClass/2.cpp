#include <iostream>
#include <vector>

class Razlomak {
public:
    //kada inicijalizujemo ne moramo da pravimo vise kostruktora za 1 i za 0 el
    //i uvek mora da se definisu sve ili ni jedna vrednost
    Razlomak(int brojilac = 0, unsigned int imenilac = 1)
        : m_brojilac(brojilac)
        , m_imenilac(imenilac)
        {
            //skratiRazlomak();
        }

    void setImenilac(unsigned int imenilac){
        m_imenilac = imenilac;
        //stratiRazlomak();
    }

    //zbog this da bi bio const, koj radi tako ispod haube
    unsigned int getImeilac() const{
        return m_imenilac;
    }

private:
    int m_brojilac;
    unsigned int m_imenilac;
};

int main(int argc, char *argv[]){
    //moze i viticaste umesto obicnih
    Razlomak nula; //0/1
    Razlomak cetres_dva(42); //41/1 idu redom
    Razlomak cetres_dva_pola(42,2); //41/2
}
