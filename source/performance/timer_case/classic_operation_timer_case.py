import numpy
import pcraster as pcr
from performance.timer_case import classic_operation, operation_timer_case


class ClassicOperationTimerCase(operation_timer_case.OperationTimerCase):

    pass


operation_timer_case.add_unary_operation_timer_cases(
    ClassicOperationTimerCase, pcr, classic_operation.unary_operations)
operation_timer_case.add_binary_operation_timer_cases(
    ClassicOperationTimerCase, pcr, classic_operation.binary_operations)
