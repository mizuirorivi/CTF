#include<bits/stdc++.h>
using namespace std;

string input = "hello";
void copy_str(int a,int b){
  cout << "copy_str(" << a << "," << b << ")" << endl;
  if(a==0){
    return;
  }
  int j = b % 5;
  char *k = 4 - j;
  
}

/*
 *
  var g:int = 4;
  var h:int = e[2];//b 
  var i:int = 5;
  var j:int = h % i;
 *
 *
  var k:ubyte_ptr = g - j;
  var l:int = k[1067];
  var m:int = 24;
  var n:int = l << m;
  var o:int = n >> m;
  var p:int = e[3];
  var q:int = p ^ o;
 */
int main(){
  for(int i=0;i<input.size();i++){
    copy_str((int)input[i],i);
  }
}
