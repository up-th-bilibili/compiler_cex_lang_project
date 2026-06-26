# cexc（c-extension compiler）项目 / cexc(c-extension compiler) project
**注意：以下中英文内容在表意上尽力保持一致**

**Note: We will make the Chinese and English as close in meaning as possible**

这是由CEI(C-extension Standards Initiative，qq群号646926140)负责制定标准的一款语言，以下为成员：
* up泰和 | up-th-bilibili

The language specification is formulated by the CEI (C-extension Standards Initiative, Tencent QQ Group No. 646926140).
Core team members:
* up taihe | up-th-bilibili

项目维护人员目前和组织成员相同。

the maintainers in now are same with Core team members.

cex的设计原则如下：
* Make C Simple More - MCSM
* Make C Easy More - MCEM
* Keep Clear Memory Model - KCMM
* Keep cex Is C - KCIC

这四条原则绝不能轻易违反，对于cex来讲，违背哪一条都是不可接受的事，MCSM和MCEM是为了为c生态拉到更多用户；KCMM是为了不落入c++的后尘，陷入远离底层一骑绝尘；而KCIC则是最终的底线：永远不要像c++一样，对c不兼容、脱离c生态圈、变得不像c。

The design principles of cex are listed below:
* Make C Simple More — MCSM
* Make C Easy More — MCEM
* Keep Clear Memory Model — KCMM
* Keep cex Is C — KCIC

These four principles must never be breached lightly. Any violation is unacceptable for cex.
MCSM and MCEM are intended to attract more developers from the C ecosystem.
KCMM prevents the project from repeating the mistakes of C++ and drifting far away from low-level programming.
KCIC serves as the ultimate bottom line: never follow the path of C++ — never break compatibility with C, never break away from the C ecosystem, and never evolve into a language that no longer resembles pure C.
