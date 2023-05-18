import os
os.system('bash install.sh')
os.system('tamp -start')
os.system('bash fix_phpmyadmin.sh')
os.system('bash tamp -start')