
import re

PA = re.compile("(\d+) -> ([a-z]+)")
NOTRULE = re.compile("NOT ([a-z]+) -> ([a-z]+)")
ANDOR = re.compile("([a-z]+) (AND|OR) ([a-z]+) -> ([a-z]+)")
SHIFT = re.compile("([a-z]+) (LSHIFT|RSHIFT) (\d+) -> ([a-z]+)")

data = [
"123 -> x",
"456 -> y",
"x AND y -> d",
"x OR y -> e",
"x LSHIFT 2 -> f",
"y RSHIFT 2 -> g",
"NOT x -> h",
"NOT y -> i"
]

def doit():
	data = open("data7.txt","r").readlines()

TYPE_ASSIGN  = 0
TYPE_NOT = 1
TYPE_ANDOR = 2
TYPE_SHIFT = 3

class Op: pass

class OpAssign(Op):
    def __init__(self,value):
        self.value = value
        self.TYPE = TYPE_ASSIGN
    def __repr__(self):
        return str(self.value)
        
class OpNot(Op):
    def __init__(self,expr):
        self.expr = expr
        self.TYPE = TYPE_NOT
    def __repr__(self):
        return "OpNot: " + str(self.expr)

class OpAndOr(Op):
    def __init__(self,optype,expr1,expr2):
    	self.TYPE = TYPE_ANDOR
        self.optype = optype
        self.expr1 = expr1
        self.expr2 = expr2

class OpShift(Op):
    def __init__(self, optype, expr1, expr2):
    	self.TYPE = TYPE_SHIFT
        self.optype = optype
        self.expr1 = expr1
        self.expr2 = expr2
        
def try_assign(symtable,line):
    m = PA.match(line)
    if m is not None:
        print "Assign", m.group(1), m.group(2)
        symtable[m.group(2)] = OpAssign(int(m.group(1)))
        return True
    return False
    
def try_not(symtable,line):
    m = NOTRULE.match(line)
    if m is not None:
        print "OpNot"
        symtable[m.group(2)] = OpNot(m.group(1))
        return True
    return False

def try_andor(symtable,line):
    m = ANDOR.match(line)
    if m is not None:
        print "OpAndOr"
        symtable[m.group(4)] = OpAndOr(m.group(2),m.group(1),m.group(3))
        return True
    return False

def try_shift(symtable,line):
    m = SHIFT.match(line)
    if m is not None:
        print "OpShift"
        symtable[m.group(4)] = OpShift(m.group(2),m.group(1),m.group(3))
        return True
    return False
    
def parse(symtable, line):
    if try_assign(symtable,line):
        pass
    elif try_not(symtable,line):
        pass
    elif try_andor(symtable,line):
        pass
    elif try_shift(symtable,line):
        pass
    else:
        print "not matched"
            
def eval(symname, symtable):
	print "need to evail for", symname, "in", symtable
	rule = symtable[symname]
	if rule.TYPE == TYPE_ASSIGN:
		pass
	elif rule.TYPE == TYPE_NOT:
		pass

	print "rule is ", rule
	print "looking up next rule"
	rule2 = symtable[rule.expr]
	print "next rule",rule2   
    

symtable = {}
for line in data:
    parse(symtable,line)
# print symtable
eval("h", symtable)





