# application返回res_body
# res_fun构造res_start_line, res_headers

# 疑问:
#   1.为什么不让res_fun构造的res_start_line, res_headers直接返回给application,
#     然后application直接返回res = res_start_line + res_header + res_body


