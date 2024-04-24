#include<iostream>
using namespace std;
int main(){
cout<<"\t\t\t***BMI CALCULATOR***\n";
double weight;
double height;
double BMI;
cout<<"Enter your weight(in kg):";
cin>>weight;
cout<<"Enter your height(in meters):";
cin>>height;
        //General Formula for Body Mass Indux Calculator
//BMI=Weight(kg)/Height(meters)^2
BMI=weight/(height*height);
cout<<"Your BMI:"<<BMI<<endl;
if(BMI<18.5){
    cout<<"Oops!!! You are UnderWeight(Unhealthy)\n";
}else{
    if(BMI>=18.5 && BMI<=24.9){
        cout<<"Congratulations!!! You have Normal Weight(Healthy)\n";
    }else{
        if(BMI>=25 && BMI>=29.9){
        cout<<"Oops!!! You are OverWeight. You should decrease your weight(Unhealthy)\n";
        }else{
            //BMI>=30
        cout<<"Oops!!! You are Obese. You must decrease your weight(Very Unhealthy)\n";
        }
    }
}
    return 0;
}