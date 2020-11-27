# python code from decaf file
class Program:
    def __init__(self):
        self._fp_4 = 0
        self._fp_8 = 0
        self._fp_12 = 0
        self._fp_16 = 0
        self._fp_20 = 0
    def fib(self):
        print("holarip")
        # load immediate literal into var1
        self._fp_16 = 1
        # load immediate literal into var1
        self._fp_8 = 1
        # load immediate literal into var1
        self._fp_12 = 0
        # load immediate literal into var1
        self._fp_20 = 0
        # loads data into t1, t0, set s_ to verify ifs
        _s_2 = ( self._fp_20  <  10 )
        # jump if condition
        if (_s_2):
            self._L23()
        # jump if not condition
        if not (_s_2):
            self._L24()
    def _L23(self):
        print("_L23")
        # intermidate operetions to var 1
        self._fp_12 = ( self._fp_16  +  self._fp_8 )
        # moving var2 into var1
        self._fp_16 = self._fp_8
        # moving var2 into var1
        self._fp_8 = self._fp_12
        # sums var1 + immediate, saves in var1
        self._fp_20 = self._fp_20 + 1
        # loads data into t1, t0, set s_ to verify ifs
        _s_3 = ( self._fp_20  <  10 )
        # jump if condition
        if (_s_3):
            self._L23()
        # jump if not condition
        if not (_s_3):
            self._L24()
    def _L24(self):
        print("_L24")
if __name__ == "__main__":
    program = Program()
    program.fib()
