import sys, os
INTERP = os.path.join(os.environ['HOME'], 'zawya.husainhk.com', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

sys.path.append('zawya_newsletter_webapp')
from zawya_newsletter_webapp import app as application
