//
// Created by luckye on 24-8-20.
//
#include "iostream"
#include "memory"
using namespace std;

class Ball
{
     public:
      Ball()
      {
        cout << "Ball()" << endl;
      }
      ~Ball()
      {
        cout << "~Ball()" << endl;
      }
      void play()
      {
        cout << "play()" << endl;
      }
};

int main()
{
    shared_ptr<Ball> ball =make_shared<Ball>();
    ball->play();
    shared_ptr<Ball> ptr1 = ball;
    cout << "ptr1.use_count() = " << ptr1.use_count() << endl;
    shared_ptr<Ball> ptr2 = ball;
    cout << "ptr1.use_count() = " << ptr1.use_count() << "ptr2.use_count() = " << ptr2.use_count() << endl;

    Ball* p = ball.get();
    cout<<"p = "<<p<<endl;

    ball.reset();
    cout << "ptr1.use_count() = " << ptr1.use_count() << "ptr2.use_count() = " << ptr2.use_count() << endl;
    ptr1.reset();
    cout << "ptr1.use_count() = " << ptr1.use_count() << "ptr2.use_count() = " << ptr2.use_count() << endl;
    ptr2.reset();
    cout << "ptr1.use_count() = " << ptr1.use_count() << "ptr2.use_count() = " << ptr2.use_count() << endl;

    //避免智能指针与普通指针混用
    //对象已经析构但是普通指针还在指向，会导致指针悬空
    cout<<"p = "<<p<<endl;
    return 0;
}

