#global scope
my_global = 10


def fn1():
    enclosed_v = 8
    print("access to glball", my_global)

    def fn2():
        local_v = 5
        print("access to glball", my_global)
        print("access to glball", enclosed_v)
    fn2()
fn1()

