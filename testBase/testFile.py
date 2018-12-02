try:
	f = open('../resources/test.txt','r')
	for line in f.readlines():
		print(line.split('|')) # 按照每一行来读取
	# print(f.read())
finally:
	if f:
		f.close()

# 每次都这样close()太繁琐		
# try:
	# f = open(''../resources/test.txt','r')
	# print(f.read())
# finally:
	# if f:
		# f.close()
		
# 这样就不用每次都手动关闭资源了,系统搞定
# with open('../resources/test.txt', 'r') as f:
#     print(f.read())
