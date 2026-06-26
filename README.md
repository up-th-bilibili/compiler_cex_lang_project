# cexc（c-extension compiler）项目 / cexc(c-extension compiler) project
**注意：以下中英文内容在表意上尽力保持一致**

**Note: We will make the Chinese and English as close in meaning as possible**

这是由CEI(C-extension Standards Initiative，qq群号646926140)负责制定标准的一款语言，以下为成员：
* up泰和 | up-th-bilibili

The language specification is formulated by the CEI (C-extension Standards Initiative, Tencent QQ Group No. 646926140).
Core team members:
* up taihe | up-th-bilibili

项目维护人员目前和组织成员相同。

Current maintainers are the same as core team members.

cex的设计原则如下：
* Make C Simple More - MCSM
* Make C Easy More - MCEM
* Keep Clear Memory Model - KCMM
* Keep cex Is C - KCIC

四条准则不可随意违背，对 cex 而言，违反任意一条都无法接受：
MCSM和MCEM旨在为C生态与cex拉到更多用户；
KCMM是为了不重蹈C++的覆辙，避免走上远离底层、一去不复返的道路；
而KCIC则是最终的底线：永远不要像C++一样，对c不兼容、脱离c生态圈、变得不像c。

The design principles of cex are listed below:
* Make C Simple More — MCSM
* Make C Easy More — MCEM
* Keep Clear Memory Model — KCMM
* Keep cex Is C — KCIC

These four principles must never be breached lightly. Any violation is unacceptable for cex.
MCSM and MCEM are intended to attract more developers for both the C ecosystem and cex.
KCMM prevents the project from repeating the mistakes of C++ and drifting far away from low-level programming.
KCIC serves as the ultimate bottom line: never follow the path of C++ — never break compatibility with C, never break away from the C ecosystem, and never evolve into a language that no longer resembles pure C.

其他相关的技术文档请参见项目的`standard`文件夹。

All other technical specification documents are placed in the `standard` directory of this project.
