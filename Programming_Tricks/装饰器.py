def model():
    print("model infomation")

def to_cuda(func):
    def wrapper(): #包装器
        print(f"{func.__name__} is to cuda")
        return func()

    return wrapper

@to_cuda
def model2():
    print("model infomation")

if __name__ == "__main__":
    model = to_cuda(model)
    model()
    model2()


