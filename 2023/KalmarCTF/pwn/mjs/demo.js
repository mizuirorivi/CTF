function hello(){
  pirnt("hello");
}
let name = "rivi";
print("hello! " + name);

let name_hex = name.at(0);
print('another name for you is:');
print(name_hex);

let profile = {favorite: "javascript"};
let o = Object.create(profile);

let profile_str = JSON.stringify(o);
print(profile_str);
