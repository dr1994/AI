
# coding: utf-8

# In[7]:


from bs4 import BeautifulSoup
html_doc="""<html><head><title>HI!!!</title></head>
<body><h2>曾東嶸</h2>
<p>ADT106128</p>
<a id="link01" href="/my_link">Link 1</a>
<a id="link02" href="/my_link">Link 1</a>
<p>BYE!!!,<b class="boldtext">Bold Text</b></p>
</body>
</html>"""
soup=BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())


# In[8]:


a_tags=soup.find_all('a')
for tag in a_tags:
    print('連結:'+tag.string+'=>'+'連結網址:'+tag.get('href'))

