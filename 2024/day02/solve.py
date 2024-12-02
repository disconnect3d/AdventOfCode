import sys
import operator


def is_safe_report(report):
    """
    A report only counts as safe if both of the following are true:
    - The report are either all increasing or all decreasing.
    - Any two adjacent report differ by at least one and at most three.
    """
    #print(report)
    if report[0] == report[1]:
        return False

    easing_rule = operator.gt if report[0] > report[1] else operator.lt
    
    prev_level = report[0]

    for level in report[1:]:
        if not easing_rule(prev_level, level):
            #print("easing", prev_level, level)
            return False

        if not (1 <= abs(level-prev_level) <= 3):
            #print("abs", prev_level, level)
            return False

        prev_level = level

    return True


def iter_reports():
    """Parses the report from stdin and returns them as iterator to array of numbers"""
    return (
        [int(x) for x in line.split(' ')] for line in iter(sys.stdin)
    )

def task1():
    result = sum(map(is_safe_report, iter_reports()))
    print(result)


def task2():
    """
    --- Part Two ---
    The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.
    The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report.
    It's like the bad level never happened!
    Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

    More of the above example's reports are now safe:
        7 6 4 2 1: Safe without removing any level.
        1 2 7 8 9: Unsafe regardless of which level is removed.
        9 7 6 2 1: Unsafe regardless of which level is removed.
        1 3 2 4 5: Safe by removing the second level, 3.
        8 6 4 4 1: Safe by removing the third level, 4.
        1 3 6 7 9: Safe without removing any level.
    Thanks to the Problem Dampener, 4 reports are actually safe!

    Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
    """
    reports = tuple(iter_reports())

    safe_report = 0

    for report in reports:
        if is_safe_report(report):
            safe_report += 1
            continue
        
        # Check report when a single level is removed
        for idx in range(len(report)):
            new_report = report[:idx] + report[idx+1:]
            if is_safe_report(new_report):
                safe_report += 1
                break

    print("Level 2 safe reports:", safe_report)

#task1()
task2()
