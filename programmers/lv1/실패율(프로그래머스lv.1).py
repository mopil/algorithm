def get_reach_count(stage, stages):
    count = 0
    for i in stages:
        if i >= stage:
            count += 1
    return count


def solution(N, stages):
    result = []
    stage_fail = {}
    for stage in range(1, N+1):
        reach_count = get_reach_count(stage, stages)
        not_clear_count = stages.count(stage)
        if reach_count != 0:
            fail_rate = not_clear_count / reach_count
            stage_fail[stage] = fail_rate
        else:
            stage_fail[stage] = 0
    sorted_result = sorted(stage_fail.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_result:
        result.append(item[0])
    return result
