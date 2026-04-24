from typing import Any,Union,List,Literal
from enum import Enum, auto
from dataclasses import dataclass
Void = None.__class__
class TokenTypes(Enum):
    LIT = auto() # true false null
    NUMBER = auto() # 1 1.1 1/2 0xb
    STR = auto() # "string"
    NAME = auto() # name
    SYMBOL = auto() # {}[]:,
    EOF = auto() # End Of File
@dataclass(frozen=True)
class Token:
    toktyp: TokenTypes
    line: int
    row: int
    store:Any = None

    def __eq__(self,other) -> bool:
        if other.__class__ is not self.__class__:
            return False
        return self.toktyp == other.toktyp and self.store == other.store
    
    def __str__(self) -> str:
        if self.store is None:
            return f"<{self.toktyp.name}>"
        return f"<{self.toktyp.name}:{self.store!r}>"

class BaseTokenizer:
    '''
    接口规则：
        函数签名为name(self,fallback,arr) -> rtype,在arr默认值为Void时表示不在意arr
        rtype可以为以下2种：
            bool 跳过类
            Union[Token,Literal[False]] 返回类
    '''
    __slots__ = ('_code','_pos','_line','_row','_lcache','_mfuncs')
    def __init__(self,text,mfuncs=None,options=None) -> Void:
        self._code = text
        self._pos = 0
        self._line = 0
        self._row = 0
        self._lcache = [len(i)+1 for i in text.split('\n')]
        self._mfuncs = mfuncs or tuple()
        self.options = options or CompileOptions()
    def using(self,size=1) -> bool:
        self._pos += size
        self._row += size
        while self._line < len(self._lcache) and self._row >= self._lcache[self._line]:
            self._row -= self._lcache[self._line]
            self._line += 1
        return self._pos < len(self._code)
    def peek(self,range_extras=0) -> str:
        return self._code[self._pos:self._pos+range_extras+1] or '\0'
    def tokenize(self) -> List[Token]:
        tokens = []
        while self._pos < len(self._code):
            fallback = (self._pos,self._line,self._row)
            for i in self._mfuncs:
                get = i(fallback)
                if get:
                    if get is not True:
                        tokens.append(get)
                    break
                self._pos,self._line,self._row = fallback
            else:
                raise SyntaxError(f'unmatch the matchers in line {self._line+1} column {self._row+1}.')
        if not tokens:
            tokens.append(Token(toktyp=TokenTypes.EOF,line=1,row=1))
        elif tokens[-1] != Token(toktyp=TokenTypes.EOF):
            tokens.append(Token(toktyp=TokenTypes.EOF,line=len(self._lcache)-1,row=self._lcache[-1]))
        return tokens
