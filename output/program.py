# python code from decaf file
class Program:
    def __init__(self):
        self._fp_4 = 0
        self._fp_8 = 0
        self._fp_12 = 0
        self._fp_16 = 0
        self._fp_20 = 0
        self._fp_24 = 0
        self._fp_28 = 0
    def main(self):
        print("holarip")
        # load immediate literal into var1
        self._fp_8 = 0
        # load immediate literal into var1
        self._fp_12 = 1
        # sums var1 + immediate, saves in var1
        self._fp_12 = self._fp_12 + 3
        # intermidate operetions to var 1
        self._fp_12 = ((( self._fp_8  +  1 ) /  2 ) *  self._fp_12 )
        # intermidate operetions to var 1 bool
        self._fp_16 = self._fp_12==1 or self._fp_8!=2
        # intermidate operetions to var 1
        self._fp_20 = ( self._fp_12  ==  1 )
        # load immediate literal into var1
        self._fp_24 = 1
        # moving var2 into var1
        self._fp_28 = self._fp_24
        # sums var1 + var2, saves in var1
        self._fp_24 = self._fp_24 + self._fp_8
         # loads data into t1, t0, set s_ to verify ifs
        _s_3 = ( self._fp_24  <=  5 )
        # jump if condition
        if (_s_3):
            self._L37()
        # jump if not condition
        if not (_s_3):
            self._L38()
    def _L37(self):
        print("_L37")
         # loads data into t1, t0, set s_ to verify ifs
        _s_4 = (( self._fp_8  ==  self._fp_12 ) and ( self._fp_8  !=  0 ))
        # jump if condition
        if (_s_4):
            self._L42()
        # jump if not condition
        if not (_s_4):
            self._L43()
    def _L42(self):
        print("_L42")
        # sums var1 + immediate, saves in var1
        self._fp_8 = self._fp_8 + 1
    def _L43(self):
        print("_L43")
        # subs var1 - immediate, saves in var1
        self._fp_8 = self._fp_8 - 1
    def _L44(self):
        print("_L44")
        # sums var1 + immediate, saves in var1
        self._fp_24 = self._fp_24 + 1
         # loads data into t1, t0, set s_ to verify ifs
        _s_5 = ( self._fp_24  <=  5 )
        # jump if condition
        if (_s_5):
            self._L37()
        # jump if not condition
        if not (_s_5):
            self._L38()
    def _L38(self):
        print("_L38")
if __name__ == "__main__":
    program = Program()
    program.main()
