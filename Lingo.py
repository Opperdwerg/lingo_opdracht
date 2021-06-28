class Lingo:

    woord = ""
    hint = ""
    beurt = 0
    gewonnen = False
    verloren = False

    def __init__(self, woord):
        self.woord = woord
        self.hint = woord[0]
        self.beurt = 0
        self.gewonnen = False
        self.verloren = False


    def validate_input(self, input):
        input = input.lower()
        if(len(input) < 6):
            self.hint = ""
            counter = 0
            for ch1 in input:
                if ch1 == self.woord[counter]:
                    self.hint = self.hint + ch1
                else:
                    self.hint = self.hint+"-"
                counter+=1  
                
            if self.hint == self.woord:
                self.gewonnen = True
        else:
            return


        self.beurt += 1
        self.check_turn()

    def check_turn(self):
        if self.beurt >= 5:
            self.verloren = True

    def check_letter(self, ch, counter):
        ch = ch.lower()
        if ch == self.woord[counter]:
            return "goed"
        if ch in self.woord:
            return "ergens"
        return "nergens"
