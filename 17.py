n = int(raw_input())
arr = map(int, raw_input().split())
t=max(arr)
new = filter(lambda x:x!=t,arr)
print max(new)