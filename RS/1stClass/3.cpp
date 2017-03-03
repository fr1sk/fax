//korisnik unosi neke reci, a te reci se uokvire sa zvezdicama
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char *argv[]){
    std::vector<std::string> messages;
    std::string message; //dinamicki niz karaktera
    size_t maxlen = 0;
    //std::cin >> message;
    //std::cin.getline(); //ovo lose jer radi kao c !!!NIKAD NE KORISTI OVO!!!

    while(std::getline(std::cin, message)){
        //std::getline(std::cin, message); //args - odakle citamo, u sta citamo
        //kad god cin uvek u headu while petlje
        messages.push_back(message);
        if(message.length()>maxlen){
            maxlen = message.length();
        }
    }
        //specijalni konstruktor koj prima jedan int i 1 char
        std::string bar(maxlen + 4, '*');

    std::cout << bar << std::endl;
    //koristimo & kako ne bi kopirali (efikasnost) vec koristimo postojeci
    for(const auto& message: messages){
        std::cout
            << "* "
            << message
            << std::string(maxlen - message.length(), ' ')
            << " *"
            << std::endl;
    }
    std::cout << bar << std::endl;


    return 0;
}
