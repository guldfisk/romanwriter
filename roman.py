from collections import OrderedDict

class RomanWriter:
	romanKeys = OrderedDict((
		(1000, 'M'),
		(900, 'CM'),
		(500, 'D'),
		(400, 'CD'),
		(100, 'C'),
		(90, 'XC'),
		(50, 'L'),
		(40, 'XL'),
		(10, 'X'),
		(9, 'IX'),
		(5, 'V'),
		(4, 'IV'),
		(1, 'I')
	))
	@staticmethod
	def _roman(num):
		for r in RomanWriter.romanKeys.keys():
			x, y = divmod(num, r)
			yield RomanWriter.romanKeys[r]*x
			num -= (r*x)
			if num>0:
				RomanWriter._roman(num)
			else:
				break
	@staticmethod
	def get(num):
		return "".join([a for a in RomanWriter._roman(num)])