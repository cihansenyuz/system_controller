#include <iostream>
#include "ina238.hpp"
#include <fstream>
#include <ctime>
#include <string>
#include <vector>
#include <chrono>
#include <thread>

/*
A1	A0	Secondary Device Address
GND	GND	1000000
GND	VS	1000001
GND	SDA	1000010
GND	SCL	1000011
VS	GND	1000100
VS	VS	1000101
VS	SDA	1000110
VS	SCL	1000111
SDA	GND	1001000
SDA	VS	1001001
SDA	SDA	1001010
SDA	SCL	1001011
SCL	GND	1001100
SCL	VS	1001101
SCL	SDA	1001110
SCL	SCL	1001111
*/

#define DEVICE_ADDRESS_1 0x80
#define DEVICE_ADDRESS_2 0x82
#define DEVICE_ADDRESS_3 0x84
#define DEVICE_ADDRESS_4 0x86
#define DEVICE_ADDRESS_5 0x88

#define I2C_BUS_NUMBER 1
//#define SHUNT_RESISTANCE 0.022
//#define MAX_CURRENT 0.05

class TimeLabel{
public:
    TimeLabel(){
        time(&current_time);
        local_time = localtime(&current_time);
    }
    std::string StampCurrentTime(){
        std::string stamp = "Time";

        if(local_time->tm_hour < 10)
            stamp.append("0");
        stamp.append(std::to_string(local_time->tm_hour));
        stamp.append(":");

        if(local_time->tm_min < 10)
            stamp.append("0");
        stamp.append(std::to_string(local_time->tm_min));
        stamp.append(":");

        if(local_time->tm_sec < 10)
            stamp.append("0");
        stamp.append(std::to_string(local_time->tm_sec));
        return stamp;
    }
private:
    time_t current_time;
    struct tm *local_time;
};

void RecordMeasurement(TimeLabel* time_label, std::vector<Ina238> &sensors){
    std::ofstream file("measurements.txt", std::ios::app);
    
    file << time_label->StampCurrentTime();
    for(auto &sensor : sensors){
        file << sensor.voltage() << '\t';
    }
    file << std::endl;
    file.close();
}

int main(){

    TimeLabel time_label;
    std::vector<Ina238> sensors;
    sensors.push_back(Ina238(DEVICE_ADDRESS_1, I2C_BUS_NUMBER));
    sensors.push_back(Ina238(DEVICE_ADDRESS_2, I2C_BUS_NUMBER));
    sensors.push_back(Ina238(DEVICE_ADDRESS_3, I2C_BUS_NUMBER));
    sensors.push_back(Ina238(DEVICE_ADDRESS_4, I2C_BUS_NUMBER));
    sensors.push_back(Ina238(DEVICE_ADDRESS_5, I2C_BUS_NUMBER));

    while(true){
        RecordMeasurement(&time_label, sensors);
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }

    return EXIT_SUCCESS; 
}