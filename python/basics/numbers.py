response1 = 1.2
response2 = 1.5
response3 = 1.1
response4 = 2.0
response5 = 1.7
max_response_time = 2.0

total_res = response1 + response2 + response3 + response4 + response5
num_res = 5
avg_res = total_res / num_res
res_within_max = avg_res < max_response_time

print(f"Average response time: {avg_res}")
print(f"Within max: {res_within_max}")
