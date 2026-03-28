import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from forms.login import LoginWindow

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()