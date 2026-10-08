// SPDX-License-Identifier: MPL-2.0
#ifndef _STDCEX_CEX26KW_MACROS_H
#define _STDCEX_CEX26KW_MACROS_H {0,9,0}
#ifdef __STDCEX__
#define namespace _Namespace
#define private _Private
#define keyword _Keyword
#define operator _Operator
#define yield _Yield
#define translate _Translate
#define destroy _Destroy
#else
#warning "cex26keyword.h is Cex standard library, not for C or C++."
#endif
#endif
