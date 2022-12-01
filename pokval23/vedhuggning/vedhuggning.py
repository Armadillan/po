from collections import deque
N = int(input())
S = int(input())

v = []
t = []

for _ in range(N):
    li, vi, ti = map(int, input())
    S -= li
    v.append(vi)
    t.append(ti)

sorted_t_indices = sorted(range(N), key=lambda i: t[i], reverse=True)
max_t_indices = deque()

#max_t_index: (total speed over last interval, growth this interval in addition to previous growth, time_in_this_interval)
data = {}



# total_speed_over_last_interval = 0
# total_growth_over_last_interval = 0
# current_t_index = sorted_t_indices[0]
# for i in sorted_t_indices:
#     if t[i] < t[current_t_index]:
#         max_t_indices.appendleft(current_t_index)
#         data[current_t_index] = (total_speed_over_last_interval, total_growth_over_last_interval, t[current_t_index]-t[i])
#     total_speed_over_last_interval += v[i]
#     total_growth_over_last_interval +=

# max_t_indices.appendleft(current_t_index)
# data[current_t_index] = (total_speed_over_last_interval, total_growth_over_last_interval, t[current_t_index])
