from abc import ABC,abstractmethod

class interestCalculator(ABC):

    def __init__(self,investment):
        self.investment = investment
        self.USD = 70
        self.AUS = 53
        self.EU = 65
        if isinstance(self,USInvestors):
            print ("The Investment from US NRI in INR = ",investment*self.USD)
            investment = investment*65
            self.interest = self.investment*(6/100)
        elif isinstance(self,AUSInvestors):
            print("The Investment from Australian NRI in INR = ", investment * self.AUS)
            investment = investment * 53
            self.interest = self.investment * (6 / 100)
        elif isinstance(self,EUInvestors):
            print("The Investment from Europian NRI in INR = ", investment * self.EU)
            investment = investment * 53
            self.interest = self.investment * (6 / 100)
        super().__init__()

    @abstractmethod
    def moneyConvertor(self):
        pass

class USInvestors(interestCalculator):

    def moneyConvertor(self):
        print ("The Interest gained is = ",self.interest*self.USD)

class AUSInvestors(interestCalculator):

    def moneyConvertor(self):
        print ("The Interest gained is = ",self.interest*self.AUS)

class EUInvestors(interestCalculator):

    def moneyConvertor(self):
        print ("The Interest gained is = ",self.interest*self.EU)

#Check the interest accrued by an US NRI
us1 = USInvestors(5000) # the value is in US dollar
us1.moneyConvertor()

#Check the interest accrued by an Australian NRI
aus1 = AUSInvestors(600) # the value is in Australian dollar
aus1.moneyConvertor()

#Check the interest accrued by an European NRI
eu1 = EUInvestors(800) # the value is in European dollar
eu1.moneyConvertor()