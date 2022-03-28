from college import CollegeProxy

if __name__ == "__main__":	
    collegeProxy = CollegeProxy()
    print('--------------Balance 1000----------------')
    collegeProxy.studyingInCollege()
    collegeProxy.feeBalance = 100
    print()
    print('--------------Balance 100----------------')
    collegeProxy.studyingInCollege()
