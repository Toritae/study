def solution(lottos, win_nums):
    win_cnt = 0
    zero_cnt = 0
    rank_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    for lotto in lottos:
        if lotto in win_nums:
            win_nums.remove(lotto)
            win_cnt += 1
        if lotto == 0:
            zero_cnt += 1
    max_cnt = win_cnt + zero_cnt
    # 최고순위, 최저순위
    min_rank = rank_dict[max_cnt]
    max_rank = rank_dict[win_cnt]
    answer = [min_rank, max_rank]
    return answer