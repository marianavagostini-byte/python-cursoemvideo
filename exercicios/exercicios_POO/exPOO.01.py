class Ficha:                                    # 1. CLASSE — o modelo em branco

	def __init__(self, codigo, descricao):      # 2. __init__ — o ato de preencher na abertura
		self.codigo = codigo                    # 3. ATRIBUTO — um campo do formulário
		self.descricao = descricao              # 3. ATRIBUTO
		self.calibracoes = 0                    # 3. ATRIBUTO (nasce com valor fixo)

	def calibrar(self):                         # 4. MÉTODO — uma instrução do rodapé
		self.calibracoes += 1                   # 5. SELF — "desta ficha aqui"
		print(f'{self.descricao} calibrado. Total: {self.calibracoes}')

	def mostrar(self):                          # 4. MÉTODO
		print(f'[{self.codigo}] {self.descricao} — {self.calibracoes} calibrações')


# ---- programa principal ----

f1 = Ficha('DL-01', 'Datalogger Elitech')       # 6. OBJETO — uma ficha preenchida
f2 = Ficha('TH-07', 'Termo-higrômetro AKSO')    # 6. OBJETO — outra ficha, mesmo modelo

f1.calibrar()
f1.calibrar()
f2.calibrar()

f1.mostrar()
f2.mostrar()