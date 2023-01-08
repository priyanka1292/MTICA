import sys
print("coming through stdout")
#stdout is saved
save_stdout=sys.stdout
print('sys.stdout:',sys.stdout)
fh=open(r"D:\pythonpractice25\day17\test.txt","w")
sys.stdout=fh
print("this line goes to test.txt")
print(input())
#return to normal:
sys.stdout=save_stdout
fh.close()
