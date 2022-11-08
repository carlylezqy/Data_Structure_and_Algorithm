from A import A1
from A.AA import AA1
import A.AA.AAA.AAA1 as aaa

from B import B1

if __name__ == "__main__":
    A1.identification()
    AA1.identification()
    aaa.identification()
    