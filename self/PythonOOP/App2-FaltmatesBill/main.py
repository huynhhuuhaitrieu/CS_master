from fpdf import FPDF


class Bill:

    def __init__(self,amount,period):
        self.amount = amount
        self.period = period


class Flatemate:

    def __init__(self,name,daysInHouse):
        self.name = name
        self.daysInHouse = daysInHouse

    def pays(self,bill,flatmate2):
        weight = (self.daysInHouse)/(self.daysInHouse + flatmate2.daysInHouse)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    def __init__(self,filename):
        self.filename = filename

    def generate(self,flatmate1,flatmate2,bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font(family='Times', size = 24, style='B')
        pdf.cell(w=0, h=80, txt="Faltmates Bill", border=1, align ="C", ln=1)

        #insert period label and value
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=100, h=40, txt="March 2021", border=1,ln=1)
        #insert naem and due amount of first flatemate  
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=100, h=40, txt="March 2021", border=1,ln=1)


        pdf.output(self.filename)

the_bill = Bill(amount =120, period ="March 2021")
john = Flatemate(name = "John", daysInHouse=20)
marry = Flatemate(name = "Marry", daysInHouse=25)

print("John pays: ",john.pays(bill=the_bill,flatmate2=marry))
print("Marry pays: ",marry.pays(bill=the_bill,flatmate2=john))

pdf_report = PdfReport(filename="report.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)