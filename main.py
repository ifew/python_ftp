import ftplib
import socket

with ftplib.FTP_TLS('ip or host') as session:

	try:
		session.set_debuglevel(2)
		session.login('username', 'password')
		session.prot_p()
		session.af = socket.AF_INET6
		session.cwd("/folder/to/store")

		#session.storbinary('STOR test.jpg', open('test.jpg', 'rb'))
		session.storlines("STOR test.txt", open('test.txt', 'rb'))

		session.quit()
	
	except ftplib.all_errors as e:
		print('FTP error:', e)
