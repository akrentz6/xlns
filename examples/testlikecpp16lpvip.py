import xlns as xl
import lpvip_ufunc #uncomment for lpvip
#xl.sbdb_ufunc = lpvip_ufunc.sbdb_ufunc_premitAddidealSub #uncomment for premit-add/above premit-sing-sub
#xl.sbdb_ufunc = lpvip_ufunc.sbdb_ufunc_premitAddlpvipSub #uncomment for premit-add/above premit-sing-sub
xl.sbdb_ufunc = lpvip_ufunc.sbdb_ufunc_premitAddpremitSub #uncomment for premit-add/above premit-sing-sub

def test1fp():
	odd = 1
	sum = 0
	for i in range(1,101): #iter for xlns16
		sum += odd
		odd += 2.0
	print("test1fp odd="+str(odd)+" sum="+str(sum))

def test2fp():
	num = 1.0
	fact = 1.0
	sum = 0.0
	for i in range(1,9):
		sum = sum + 1.0/fact
		fact = fact * num
		num = num + 1.0
	print("test2fp1 num="+str(num)+" fact="+str(fact)+" sum="+str(sum))

def test3fp():
	num = 1.0
	fact = 1.0
	sum = 0.0
	for i in range(1,11):
		sum = sum + 1.0/fact
		fact = -fact * num * (num + 1.0)
		num = num + 2.0
	print("test3fp1 num="+str(num)+" fact="+str(fact)+" sum="+str(sum))



# compute pi the hard way

def test5xlns32_float():
	num = xl.xlns(1.0)
	sum = xl.xlns(0.0)
	val = xl.xlns(num)
	for i in range(1,11):
		sum = sum + val/num
		val = -val
		num = num + 2.0
	print("test5xlns32_float num="+str(num)+" 4*sum="+str(4*sum))

def test5fp():
	num = 1.0
	sum = 0.0
	val = num
	for i in range(1,11): #iter for xlns16
		sum = sum + val/num
		val = -val
		num = num + 2.0
	print("test5fp num="+str(num)+" 4*sum="+str(4*sum))

#Mandelbrot set fpI*/

def test4fp(iter):
	mone = -1.0
	two = 2.0
	four = 4.0
	yscale = 12.0
	xscale = 24.0
	for iy in range(11,-12,-1):
		for ix in range(-40, 39):
			y = iy/yscale
			x = ix/xscale
			x1 = x
			y1 = y
			count = 0
			while ((x*x+y*y < four) and (count<iter)):
				xnew = x*x - y*y + x1
				ynew = x*y*two + y1
				count += 1
				x = xnew
				y = ynew
			if (count < iter):
				print("*",end="")
			else:
				print(" ",end="")
		print("")

def test4xlns32_float(iter):
	mone = xl.xlns(-1.0)
	two = xl.xlns(2.0)
	four = xl.xlns(4.0)
	yscale = xl.xlns(12.0)
	xscale = xl.xlns(24.0)
	for iy in range(11,-12,-1):
		for ix in range(-40, 39):
			y = iy/yscale
			x = ix/xscale
			x1 = x
			y1 = y
			count = 0
			while ((x*x+y*y < four) and (count<iter)):
				xnew = x*x - y*y + x1
				ynew = x*y*two + y1
				count += 1
				x = xnew
				y = ynew
			if (count < iter):
				print("*",end="")
			else:
				print(" ",end="")
		print("")


def test1xlns32_float():
	odd = xl.xlns(1)
	sum = xl.xlns(0)
	for i in range(1,101):
		sum += odd
		odd += 2.0
	print("test1xlns_float odd="+str(odd)+" sum="+str(sum))


def test2xlns32_float():
	num = xl.xlns(1.0)
	fact = xl.xlns(1.0)
	sum = xl.xlns(0.0)
	for i in range(1,9):
		sum = sum + 1.0/fact
		fact = fact * num
		print("test2xlns_float num="+str(num)+" fact="+str(fact)+" sum="+str(sum))
		num = num + 1.0
	print("test2xlns_float num="+str(num)+" fact="+str(fact)+" sum="+str(sum))

def test3xlns32_float():
	num = xl.xlns(1.0)
	fact = xl.xlns(1.0)
	sum = xl.xlns(0.0)
	for i in range(1,11):
		sum = sum + 1.0/fact
		fact = -fact * num * (num + 1.0)
		num = num + 2.0
	print("test3xlns_float num="+str(num)+" fact="+str(fact)+" sum="+str(sum))

def main():
	print("xlns16 Python doing same tests as the C++ version (16-bit like bfloat)");
	xl.xlnssetF(7)

	test5fp();
	test5xlns32_float();
	test1fp();
	test1xlns32_float();
	test2fp();
	test2xlns32_float();
	test3fp();
	test3xlns32_float();

	test4fp(2000);
	test4xlns32_float(2000);


main()

