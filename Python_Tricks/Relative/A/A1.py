from AA import AA1
import AA.AAA.AAA1 as AAA1

def identification():
    print(f"[{__name__}] A1 is running")

if __name__ == "__main__":
    AA1.identification()
    AAA1.identification()