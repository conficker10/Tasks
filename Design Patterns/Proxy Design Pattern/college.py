class College:
    def studyingInCollege(self):
        print("Original Class. Studying In College....")

class CollegeProxy:
    def __init__(self):
        self.feeBalance = 1000
        self.college = None
    
    def studyingInCollege(self):
        print("Proxy Class. Fess Paid or Not.")
        if self.feeBalance <= 500:
            self.college = College()
            self.college.studyingInCollege()
        else:
            print("Your fee balance is greater than 500, first pay the fee")