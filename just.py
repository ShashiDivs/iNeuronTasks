import logging
logging.basicConfig(filename = 'strs.log',level=logging.INFO,format = ('%(asctime)s %(levelname)s %(message)s' ))


class string:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    logging.info("this is intializing function....")

    def string_concat(self):
        logging.info("String Concatenation Funcion....")
        return self.a + self.b

    def string_uper(self):
        logging.info("String Uppaercase Function....")
        return self.a.upper() + self.b.title()

    def string_reverse(self):
        logging.info("String Revesres Funcion....")
        return self.a[0:300:2] + self.b[::-1].upper()

    def string_count(self):
        logging.info("String Count Function....")
        return [x for x in self.a]

    def string_vowl(self):
        logging.info("String Vowel Found Function....")
        lis = self.b
        emp = ""
        flag=0
        try:
            for i in self.a:
                if i in lis:
                    emp+=i
                    flag+=1
            return emp
        finally:
            logging.info("this is executed succesfully")

class String_Data:
    def __init__(self,a):
        self.a = a

    def Extraction_String(self):
        try:
            for i in self.a:
                if type(i) == list or tuple or dict or set:
                    for j in i:
                        if type(j) == str:
                            logging.info(j)
        except Exception as e:
            logging.info(e)
        finally:
            logging.info("String Elements extracted succesfully ")


class Finding_Ineuron:
    def __init__(self,a):
        self.a = a

    def finding_ineuron(self):
        dics = []
        for i in self.a:
            if type(i) == list or tuple or set:
                for j in i:
                    if type(j) == str:
                        if "ineuron" in j:
                            dics.append(j)
        for k in self.a:
            if type(k) == dict:
                for j in k.items():
                    if "ineuron" in j:
                        dics.append(j)

        logging.info(dics)




obj = string("Shashi is learning Python","divya is learning Java")

logging.info(obj.string_concat())
logging.info(obj.string_uper())
logging.info(obj.string_reverse())
logging.info(obj.string_count())
logging.info(obj.string_vowl())

strs = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objstr = String_Data(strs)
logging.info(objstr.Extraction_String())

ifind = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objineu = Finding_Ineuron(ifind)
logging.info(objineu.finding_ineuron())



logging.info("THIS PART IS ABOUT LISTS........")

class List:
    def __init__(self,a):
        self.a = a
    def list_extraction(self):
        return self.a
    def list_exclusive(self):
        try:
            for i in self.a:
                if type(i) == list:
                    logging.info(i)
        except Exception as e:
            logging.info(e)

lis = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objlis = List(lis)
logging.info(objlis.list_extraction())
logging.info(objlis.list_exclusive())

logging.info("THIS PART IS ABOUT DICTIONARIES..............")


class Dict:
    def __init__(self,a):
        self.a = a
    def dic_extraction(self):
        return self.a
    def dic_exclusive(self):
        try:
            for i in self.a:
                if type(i) == dict:
                    logging.info(i)
        except Exception as e:
            logging.info(e)

class Dict_keys:
    def __init__(self,a):
        self.a = a

    def Find_Keys(self):
        try:
            diclis = []
            for i in self.a:
                if type(i) == dict:
                    for j in i.keys():
                        diclis.append(j)
            logging.info(diclis)
        except Exception as e:
            logging.info(e)


class Alpha_numeric:
    def __init__(self,a):
        self.a = a

    def Finding_alpha_numeric(self):
        try:
            for i in self.a:
                if type(i) == dict:
                    for j in i:
                        if type(j)!=int:
                            logging.info(j)
        except Exception as e:
            logging.info(e)




dic = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objdic = Dict(dic)
logging.info(objdic.dic_extraction())
logging.info(objdic.dic_exclusive())

dictkeys = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objdicts = Dict_keys(dictkeys)
logging.info(objdicts.Find_Keys())

alpha = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objalpha = Alpha_numeric(alpha)
logging.info(objalpha.Finding_alpha_numeric())

logging.info("THIS PART IS ABOUT TUPLES..............")


class Tuples:
    def __init__(self,a):
        self.a = a

    def extract_tuple(self):
        return self.a

    def tuple_excluisve(self):
        try:
            for i in self.a:
                if type(i)==tuple:
                    logging.info(i)
        except Exception as e:
            logging.info(e)

    def tupel_add(self):
        try:
            emp_lis = []
            for i in self.a:
                if type(i) == tuple:
                    for j in i:
                        emp_lis.append(j)
            else:
                sum_tup = 0
                for i in emp_lis:
                    sum_tup = sum_tup + i
                logging.info(sum_tup)
        except Exception as e:
            logging.info(e)

tup = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objtuple = Tuples(tup)
logging.info(objtuple.tuple_excluisve())
logging.info(objtuple.tupel_add())


logging.info("THIS PART IS FLATTENING OF THE WHOLE LIST..............")

class Flat_List:
    def __init__(self,a):
        self.a = a

    def flat_list(self):
        try:
            lisap = []
            for i in self.a:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == list or tuple or set:
                            lisap.append(j)
            for i in self.a:
                if type(i) == dict:
                    for j in i.items():
                        for k in j:
                            lisap.append(k)
            return lisap
        except Exception as e:
            logging.info(e)


dics = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objs = Flat_List(dics)
logging.info(objs.flat_list())

logging.info("THIS PART IS SUMMATION OF THE NUMERICAL NUMBERS IN THE LIST..............")

class Summation_Inlist:
    def __init__(self,a):
        self.a = a

    def sum_count(self):
        try:
            sumcount = []
            for i in self.a:
                if type(i) == list or tuple or set:
                    for j in i:
                        if type(j) == int:
                            sumcount.append(j)
            for i in self.a:
                if type(i) == dict:
                    for j in i.values():
                        if type(j) == int:
                            sumcount.append(j)
            else:
                sums = 0
                for i in sumcount:
                    sums = sums+i
                logging.info( sums)
        except Exception as e:
            logging.info(e)


sum_count = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objcount = Summation_Inlist(sum_count)
logging.info(objcount.sum_count())

logging.info("THIS PART IS FINDING ODD AND EVEN NUMBERS FROM THE LIST..............")

class Odd_Even_finding:
    def __init__(self,a):
        self.a = a

    def Odd_Finding(self):
        try:
            ods = []
            for i in self.a:
                if type(i) == tuple or list or set:
                    for j in i:
                        if type(j) == int:
                            ods.append(j)
            for i in self.a:
                if type(i) == dict:
                    for j in i.values():
                        if type(j) == int:
                            ods.append(j)

            else:
                odss = []
                eves = []
                for i in ods:
                    if i%2 == 1:
                        odss.append(i)
                for i in ods:
                    if i%2 == 0:
                        eves.append(i)
                logging.info(f" These are odd numbers {odss},and these are even numbes {eves}")
        except Exception as e:
            logging.info(e)

ods = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objodd = Odd_Even_finding(ods)
logging.info(objodd.Odd_Finding())

logging.info("THIS PART IS MULTIPLICATION OF ALL NUMERIC VALUES IN THE LIST..............")

class Multiplication_allnumerics:
    def __init__(self,a):
        self.a = a

    def Multiply_numbers(self):
        try:
            mulall = []
            for i in self.a:
                if type(i) == list or tuple or set or dict:
                    for j in i:
                        if type(j)==int:
                            mulall.append(j)
            for i in self.a:
                if type(i) == dict:
                    for j in i.values():
                        if type(j) == int:
                            mulall.append(j)
        except Exception as e:
            logging.info(e)
        else:
            try:
                muls = 1
                for i in mulall:
                    muls = muls*i
                logging.info(muls)
            except Exception as e:
                logging.info(e)

multipy = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron", "data science"]]
objmultiply = Multiplication_allnumerics(multipy)
logging.info(objmultiply.Multiply_numbers())

logging.info("THIS PART IS FREQUENT OCCURENCES OF THE NUMERICAL VALUES IN THE LIST..............")

class Finding_Occurances:
    def __init__(self,a):
        self.a = a

    def Frequent_Occurance(self):
        try:
            occr =[]
            for i in self.a:
                if type(i) == list or tuple or set:
                    for j in i:
                        if type(j) == int:
                            occr.append(j)
            for i in self.a:
                if type(i) == dict:
                    for j in i.values():
                        if type(j) == int:
                            occr.append(j)
        except Exception as e:
            logging.info(e)

        else:
            try:
                freq_occur = []
                for i in occr:
                    if i not in freq_occur:
                        freq_occur.append(i)
                logging.info(freq_occur)
            except Exception as e:
                logging.info(e)

Occurance = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
         {"k1": "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
objoccur = Finding_Occurances(Occurance)
logging.info(objoccur.Frequent_Occurance())