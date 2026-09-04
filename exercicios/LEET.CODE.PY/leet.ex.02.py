class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        contagem = {}

        for letra in s:
            contagem[letra] = contagem.get(letra, 0) +1
        
        for letra in t:
            if letra not in contagem:
                return False
            contagem[letra] -=1
            if contagem[letra]==0:
                del contagem[letra]

        return len(contagem) ==0
