from votinglogic import *

def main():
    application = QApplication([])
    window = VotingLogic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()