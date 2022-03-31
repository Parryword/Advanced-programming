#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node *next;

    Node(int data, Node *n) {
        this->data = data;
        next = n;
    }
};

class Stack {
private:
    Node *head;
public:
    Stack() {
    head = nullptr;
    }
    void push(int x) {
        if (head == nullptr) {
            head = new Node(x, nullptr);
        }
        else {
            Node *oldHead = head;
            head = new Node(x, oldHead);
        }
    }
    int pop() {
        int value = head->data;
        head = head->next;
        return value;
    }
    int top() {
        return head->data;
    }
    bool isEmpty() {
        if (head == nullptr) {
            return true;
        }
        else
            return false;
    }
    int size() {
        int size = 0;
        Node *temp;
        for(temp=head; temp!=nullptr; temp=temp->next) {
        size++;
    }   return size;
    }
    void print() {
        Node *temp;
        for(temp=head; temp!=nullptr; temp=temp->next) {
        cout << temp->data << " ";
    } cout << endl;
    }
};

int main()
{   
    Stack *s = new Stack();

    int input;
    do {
        cout << "Please enter a value to push/Press -1 to exit:" << endl;
        cin >> input;
        if (input != -1) {
            s->push(input);
        }
    } while (input != -1);

    s->print();

    cout << "Calling func top()" << endl;

    cout << s->top() << endl;


    cout << "Calling func pop()" << endl;

    cout << s->pop() << endl;

    s->print();

    cout << "Calling func size()" << endl;

    cout << s->size() << endl;

    return 0;
}


