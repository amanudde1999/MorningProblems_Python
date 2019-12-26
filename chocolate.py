n_chocloates,m_jars = (input().split())
he_has = []
jar_capacity = []
jar_count = 0
m_jars = int(m_jars)
n_chocloates = int(n_chocloates)
for jars in range(m_jars):
	he_has,jar_capacity = input().split()
	he_has = int(he_has)
	jar_capacity = int(jar_capacity)
	if (jar_capacity - he_has) >= n_chocloates:
		jar_count+=1
print(jar_count)



