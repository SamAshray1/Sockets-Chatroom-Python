import threading

def print_cube(num):
    print("Cube: {}".format(num*num*num))
    print("Inside func: {}\n".format(threading.current_thread().name))

if __name__ == "__main__":
    t1 = threading.Thread(target=print_cube, args=(10, ))
    t2 = threading.Thread(target=print_cube, args=(11, ))
    
    t1.start()
    t2.start()
    print("After start: {}\n".format(threading.current_thread().name))

    t1.join()
    t2.join()
    print("After join: {}\n".format(threading.current_thread().name))

    print('Done')