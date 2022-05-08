# # def calculate_descent_rate(ias_start):
# #     descent_rate = ias_start * 5
# #     return descent_rate
# #
# # def calculate_tod(start_alt, target_alt):
# #     diff = (start_alt - target_alt) * 3
# #     diff /= 1000
# #     return diff
#
# # Performance logic to calculate a three degree descent rate
# #1 in 60 rule: 1 degree offset at 60nm equates to 1nm of displacement
# # Speed/Distance/Time
# #Maximum drift = wind speed / groundspeed (mpm)
# #Good guideline for descent rate: Thirty miles from the airport at 10,000' and 250 knots
# #40 nm per 10000 feet plus 15 usually applicable
#
#
# def calculate_max_drift(gs_current, wind_speed_current):
#     #convert to mpm
#     gs_current /= 52.139
#     max_drift = wind_speed_current / gs_current
#     return max_drift
#
# def calculate_descent_rate():
#
