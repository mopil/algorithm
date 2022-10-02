def solution(record):
    answer = []
    arr = {}
    for r in record:
        if "Leave" in r:
            cmd, id = r.split()

        else:
            cmd, id, name = r.split()
            arr[id] = name

    for r in record:
        if "Leave" in r:
            cmd, id = r.split()
            answer.append(arr[id] + "님이 나갔습니다.")

        else:
            cmd, id, name = r.split()
            if cmd == "Enter":
                answer.append(arr[id] + "님이 들어왔습니다.")
    return answer