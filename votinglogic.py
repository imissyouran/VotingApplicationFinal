from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from VotingApplication_ui import *
import csv

class VotingLogic(QMainWindow, Ui_VotingApplication):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.SubmitButton.clicked.connect(lambda : self.submit())
    
    def submit(self):
        # Called when submit button gets pressed
        id = self.IDInput.text()
        id = id.strip()
        vote = 'None'
        counter = 0

        if self.JaneVote.isChecked():
            # If Jane is selected, raise counter and change vote
            vote = 'Jane'
            counter = 1
        if self.JohnVote.isChecked():
            # If John is selected, raise counter and change vote
            vote = 'John'
            counter = 1
        if vote == 'None':
            # If no votes are selected, give error
            self.InfoLabel.setText('Please choose a candidate')
            self.InfoLabel.setStyleSheet('color: red;')
            self.IDInput.clear()

        if len(id) != 5 or id.isnumeric() == False:
            self.InfoLabel.setText('INVALID: ID must be 5 digits long')
            self.InfoLabel.setStyleSheet('color: red;')
            self.IDInput.clear()
            counter = 0
        
        if counter == 1:
            # If you've voted for a candidate, check if the user has voted already, if not, record vote
            with open('votes.csv', 'r', newline='') as votes_file:
                reader = csv.reader(votes_file)
                for line in reader:
                    if len(line) > 0:
                        print(line)
                        if line[0].strip() == id:
                            print(line)
                            print(id)
                            self.InfoLabel.setText('Already Voted')
                            self.InfoLabel.setStyleSheet('color: red;')
                            break
                else:
                    with open('votes.csv', 'a', newline='') as votes_file:
                        writer = csv.writer(votes_file)
                        writer.writerow([id, vote])
                    self.InfoLabel.setText('Input ID and Vote')
                    self.InfoLabel.setStyleSheet('color: black;')
        self.IDInput.clear()
        counter = 0
        if self.VotingGroup.checkedButton() is not None:
            # Clears voting for next user
            self.VotingGroup.setExclusive(False)
            self.VotingGroup.checkedButton().setChecked(False)
            self.VotingGroup.setExclusive(True)
            vote = 'None'