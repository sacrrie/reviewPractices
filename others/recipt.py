import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

#function to process serial numbers before discounting
class register:
    def __init__(self):
        self.serial=[]
        self.prices={}
        self.point_card=set()
        self.points={}
        self.bucket=[]
        self.card=False
        self.user=None
    def init(self,info):
        for i in info:
            if len(i)>1:
                self.serial.append(i[0])
                self.prices[i[0]]=i[1]
            else:
                self.serial.append(i[0])
    def checksum(self,barcode):
        if int(barcode)%10 != 0:
            return False
        return True
    
    def check_inventory(self,barcode):
        if barcode[:2]=='02':
            if barcode[2:7] not in self.serial:
                return False
            return True
        else:
            if barcode[0:12] not in self.serial:
                return False
            return True
            
    def original_price(self, barcode):
        if barcode[:2]=='02':
            price=int(barcode[7:12])
        else:
            price=int(self.price[barcode[:12]])
        return price

    def discount_price(self,barcode):
        if len(barcode)==15:
            ratio=100-int(barcode[12:14])
            if ratio<0:
                return False
            else:
                return((ratio/100.0)*self.original_price(barcode))
        else:
            original=self.original_price(barcode)
            discount=int(barcode[12:17])
            if discount>original:
                return False
            else:
                return(original-discount)

                
    
    def error_check(self,barcode):
        res=[]
        if (len(barcode) in (15,18)) and (self.check_inventory(barcode)) and (self.checksum(barcode)):
            if (not self.discount_price(barcode)):
                res.append('1')
        if (len(barcode) not in (13,15,18)) or (not self.checksum(barcode)) or (not self.check_inventory(barcode)):
            res.append('2')
        return res

    def scan(self,barcode):
        err=self.error_check(barcode)
        if len(err)>0:
            print("staff call: "," ".join(err))
            return False
        if len(barcode)==13:
            self.bucket.append(self.original_price(barcode))
        else:
            self.bucket.append(self.discount_price(barcode))

    def card(self,barcode):
        if len(barcode)>1:
            self.card=True
            self.user=barcode[1]
            if barcode[1] not in self.point_card:
                self.point_card.add(barcode[1])
                self.points[barcode[1]]=0

    def final(self):
        if self.card:
            pts=self.points[self.user]
        payments=sum(self.bucket)-pts

        if payments<0:
            self.points[self.user]=abs(payments)
            payments=0
        else:
            self.points[self.user]=0
        
        self.points[self.user]+=payments//100
        self.bucket=[]
        self.card=False
        self.user=None
        return payments

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        t=l.rstrip('\r\n')
        t=t.split()
        #t=[int(x) for x in t]
        lines.append(t)
    main(lines)
