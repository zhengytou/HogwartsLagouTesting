class Test:
    def __enter__(self):
        print('__enter__() is call!')
        return self

    def dosomething(self):
        1/0
        print('dosomethong!')

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__() is call!')
        print(f'type:{exc_type}')
        print(f'value:{exc_value}')
        print(f'trace:{traceback}')
        print('__exit()__ is call!')
        return True


with Test() as sample:
    sample.dosomething()
