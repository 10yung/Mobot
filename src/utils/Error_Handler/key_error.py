

def safe_run(func):

    def func_wrapper(*args, **kwargs):

        try:
            func(*args, **kwargs)
        except Exception as e:

            print(f'Exception type: {e.__class__.__name__}, Invalid param {e}')
            return None

    return func_wrapper

@safe_run
def add_Num_1(num):
    result = 1 + num
    return(result)

add_Num_1("hi")