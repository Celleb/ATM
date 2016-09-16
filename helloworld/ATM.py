# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
class ATM(object):
    def __init__(self, cashload={}):
	self.cassettes = cashload
	self.sum = 0

    def get_balance(self):
	self.sum = 0
	for i in self.cassettes:
	    self.sum += self.cassettes[i] * int(i)
	print "ATM Balance", self.sum
	print "Cassettes", self.cassettes

    def dispense(self, cash={}):
	for i in cash:
	    print "Dispensing: ", i, cash[i]
	    self.cassettes[i] -= cash[i]

    def load_cash(self, cashload={}):
	for i in cashload:
	    print "Cash loaded:", i, cashload[i]
	    self.cassettes[i] += cashload[i]

    def get_avail_note(self, note):
	print "Avaliable: ", self.cassettes[note]
	return self.cassettes[note]