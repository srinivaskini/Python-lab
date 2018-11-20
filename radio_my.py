#!C:/Users/user/AppData/Local/Programs/Python/Python36/python.exe
import cgi,cgitb
form=cgi.FieldStorage()
if form.getvalue("g"):
	g="<h1>"+form.getvalue("g")+"</h1>"
else:
	g="<h1>No gender selected</h1>"
print("Content-type:text/html\n")
print("<html>")
print("<body>")
print("<h1>You selected : </h1>")
print(g)
print("</body>")
print("</html>")
