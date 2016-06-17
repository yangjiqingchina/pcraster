import os
import performance_analyst as pa
import performance.timer_data
import performance.timer_case.timer_case_base


def hack_settings_in(
        data_prefix,
        repeat):

    performance.timer_data.TimerData.data_prefix = data_prefix
    performance.timer_case.timer_case_base.TimerCase.repeat = repeat


def measure_classic_operation_performance(
        data_prefix,
        repeat,
        runner):

    hack_settings_in(data_prefix, repeat)

    loader = pa.TimerLoader()

    names = [
        "classic_operation_timer_case.ClassicOperationTimerCase"
    ]
    cases = [loader.load_timers_from_name(name, [os.path.split(__file__)[0]])
        for name in names]
    suites = pa.TimerSuite(cases)
    runner.run(suites)


def measure_multicore_operation_performance(
        data_prefix,
        repeat,
        runner):

    hack_settings_in(data_prefix, repeat)

    loader = pa.TimerLoader()

    names = [
        "multicore_operation_timer_case.MulticoreOperationTimerCase"
    ]
    cases = [loader.load_timers_from_name(name, [os.path.split(__file__)[0]])
        for name in names]
    suites = pa.TimerSuite(cases)
    runner.run(suites)


def measure_multicore_operation_scalability(
        data_prefix,
        repeat,
        runner):

    hack_settings_in(data_prefix, repeat)
