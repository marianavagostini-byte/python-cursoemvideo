from abc import ABC, abstractmethod


class Aluno(ABC):

	def estudar(self):
		print('Estudando...')

	@abstractmethod
	def fazer_prova(self):
		pass


class AlunoPresencial(Aluno):

	def fazer_prova(self):
		print('Fez a prova na sala de aula.')


class AlunoEAD(Aluno):

	def fazer_prova(self):
		print('Fez a prova pelo site.')


a = AlunoPresencial()
b = AlunoEAD()

a.estudar()
a.fazer_prova()

b.estudar()
b.fazer_prova()