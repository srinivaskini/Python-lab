#!C:/Users/user/AppData/Local/Programs/Python/Python36/python.exe
import cgi,cgitb
form=cgi.FieldStorage()
subjects="<br/>"
if form.getvalue("E"):
	subjects+="English<br/>"
if form.getvalue("H"):
	subjects+="Hindi<br/>"
if form.getvalue("K"):
	subjects+="Kannada<br/>"
print("Content-type:text/html\n")
print("<html>")
print("<body>")
print("<h1>Selected subjects are : <br/></h1>")
print("<h2>"+subjects+"</h2>")
print("</body>")
print("</html>")

