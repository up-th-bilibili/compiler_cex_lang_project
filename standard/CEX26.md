# cex26标准

version: 0.0.2

## 1. 增加的关键字

class

\_\_slots\_\_

_Private

_Translate

_Operator

_Repeat

_Namespace

_Keyword

_Destroy

\_\_super\_\_

## 2. 必须的编译选项
-fbreak-change(默认)
-fno-break-change

## 3. class、多态struct和多态class
语法说明：内容中`[]`表示可选，并非实际字符
```cex
class %name%[<T>][(%father%)]{
    __slots__{
        int x; //普通内部变量，语法参考struct内部
        _Private int y; //私有变量
    }
    _Private int func(self){
        //私有函数
    }
    void __init__(self){
        //初始化函数
    }
    _Translate int(self){
        //类型转化函数
    }
    _Operator add(self,other){
        //运算符重载
    }
}
```
- \_\_slots\_\_：记录类新增/持有的内部变量
- _Private：修饰的变量、函数仅可被当前类及子类访问，该限制由编译器直接校验
- \_\_init\_\_：对象创建时自动调用
- \_\_new\_\_：负责对象内存分配；当前版本分配失败会触发段错误，后续新增异常机制后，分配失败将抛出可捕获的MemoryAllocError
- \_\_super\_\_：用于定位并使用父类相关方法
- _Translate：自定义当前类型对象的类型转换逻辑
- _Operator：运算符重载，各运算符对应独立命名

### 多态struct语法
```cex
struct<T>{
    //普通结构体内部，T代表类型
}
```
规则：每使用该结构体生成一种独立类型，都会生成全新结构体。

### 多态class
语法沿用上述class可选格式，类型生成规则同多态struct。

### 对象销毁
cex 无自动销毁机制，需手动执行；\_Destroy 会先调用自定义的\_\_del\_\_，再释放内存。
语法：
```cex
_Destroy obj;
```

## 4. 命名空间
语法：
```cex
_Namespace %name%{
    //内部内容
}
```
访问方式：`%name%.内部内容`

## 5. 次数循环
语法：
```cex
_Repeat(n){
    //循环体，支持正常跳出、跳入
}
```
规则：n 可以是任意可显式/隐式转换为 int 的数据。

## 6. 多行字符串
规则：字符串行尾的`\`，若无法构成转义序列，则自动续行；若构成合法转义序列，则不续行。
示例：
```
"ysbsydgdb\\
123"//不续行
"128467867gsghdb\
ysgd"//续行
```

## 7. 破坏性更改与函数输入关键字限制
说明：除单独标注`[]`外，本节内容在 -fno-break-change 下均无效。

### 连续比较
```cex
a+b==c>d<e!=f
```
等价于标准C：
```c
(a+b==c)&&(c>d)&&(d<e)&&(e!=f)
```

### 函数输入格式
函数支持 `arg_name=value` 传参形式；`[在参数格式前使用 _Keyword 关键字时，必须使用该传参格式]`。

## 8. 日后展望：异常
本条仅为规划内容，不属于本标准。

后续版本计划加入异常机制以提升安全性，目前确定内容：

1. 异常数据存放于独立内存区域，异常向上传递依靠返回流实现
2. 规划新增关键字：try、catch、final、throw

## 9. 日后展望：动态类型
本条仅为规划内容，不属于本标准。
计划通过类型结构等实现动态类型，具体方案暂未确定。
