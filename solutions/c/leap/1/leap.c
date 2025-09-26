#include "leap.h"

bool leap_year(int year)
{

    if (year <= 0) {
        return -1;
    }

    
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            if (year % 400 == 0) {
                return true;
            }
            else {
                return false;
            }
        }
        else {
            return true;
        }
    }
    return false;
    
    
}