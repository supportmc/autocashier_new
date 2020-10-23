import webbrowser
import os
print ()
f = open('helloworld.html','w')
 
message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""
 
f.write(message)
f.close()

#Change path to reflect file location
filename = 'file:///'+os.getcwd()+'/' + 'setup.html?t=000000000100&p=000000000037&r=28/09/20 19:48:35&spacs=000000000100&appacs=000000000100&vacs=000000000100&spacv=000.022.001.001&appacv=022.101.001.001&vacv=101.501.001.001&c=Lepark_5400001'
webbrowser.open_new_tab(filename)