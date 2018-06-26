## 贪吃蛇游戏

### 一. 序列图


```sequence
场地->蛇: 游戏开始,放蛇 
Note right of 蛇:  蛇在场地找食物
蛇-->食物: 吃食物 
Note right of 食物: 食物被蛇吃掉
食物->>蛇: 蛇增加长度
```



### 二. 类图

```sequence



```


<img src='https://g.gravizo.com/g?
 digraph G {
   main -> parse -> execute;
   main -> init;
   main -> cleanup;
   execute -> make_string;
   execute -> printf
   init -> make_string;
   main -> printf;
   execute -> compare;
 }
'/>


        
<img src='https://g.gravizo.com/svg?
  digraph G {
    aize ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf}
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }'/>

