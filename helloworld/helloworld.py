#@author Jonas Tomanga <celleb@mrcelleb.com>
#Just Checking the new snake in the business

'''
    This is a very wired way of commenting
'''
from ATM import ATM
notes = (200, 100, 50, 20, 10)
output_notes = {"200":0, "100":0, "50":0, "20":0, "10":0}
cassettes = {"200": 0, "100":0, "50":0, "20":0, "10":1000}
amount = 500
atm = ATM(cassettes)

amount = 500

for i in notes:
    avail_note = atm.get_avail_note(str(i))
    while amount >= i and avail_note >= 1 and (float(amount) / i > 1.5 or i == notes[len(notes)-1]):
	output_notes[str(i)] += 1
	amount -= i
	avail_note -= 1

print output_notes
print "Before:",
atm.get_balance()
atm.dispense(output_notes)
print "After:"
atm.get_balance();
atm.load_cash(cassettes)
atm.get_balance()