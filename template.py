######      TEMPLATE

from string import Template


class MyTemplate(Template):
	delimiter='#'


def main():
	cart=[]



	cart.append(dict(item="coke",price=80,qty=1))
	cart.append(dict(item="waffers",price=40,qty=5))
	cart.append(dict(item="cake",price=200,qty=1))

	t = MyTemplate("#qty x #item = #price")
	total=0
	print("cart : ")
	for data in cart:
		print(t.substitute(data))
		total+=data["price"]
	print("Total = {}".format(total))	


if __name__ == '__main__':
		main()	
