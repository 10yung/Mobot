import sys
import traceback

def safe_run(func):

    def func_wrapper(*args, **kwargs):

        try:
            func(*args, **kwargs)

        except Exception as e:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            trace_back = traceback.extract_tb(ex_traceback)

            print("Exception type : %s " % ex_type.__name__)
            print("Exception message : %s" %ex_value)
            print("Exception file info : %s" %trace_back)
            return None

    return func_wrapper

@safe_run
def add_Num_1(num):
    result = 1 + num
    return(result)

add_Num_1("hi")


#
# for trace in trace_back:
#     stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
