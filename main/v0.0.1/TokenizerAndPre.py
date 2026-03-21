from BaseTokenizer import *
class Tokenizer(BaseTokenizer):
    def match_switch_line(self):
        pass
    def __init__(self,text):
        mfuncs = (
            self.match_switch_line,
            self.jump_space,
            self.match_keyword,
            self.match_name
        )
        super().__init__(text,mfuncs)
