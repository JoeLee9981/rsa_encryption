'''
Created on Sep 22, 2012

@author: Joseph Lee
'''
from mod_exponent import mod_exp

class Encryption(object):
    '''
    classdocs
    '''
    def __init__(self):
        self.p = 61
        self.q = 53
        self.e = 17
   
    def encrypt(self, message):
        a = self._convert_to_numeric(message)
       
        for i in range(len(a)):
                a[i] = self._encrypt(a[i])
        m = ""
        for i in range(len(a)):
            if i != 0:
                m += ","
            m += str(a[i])
        return m
   
    def _encrypt(self, m):
        p = self.p
        q = self.q
        n = p * q
        e = self.e
        return mod_exp(m, e, n)
   
    def decrypt(self, message):
        a = message.split(',')
        m = ""
        for i in range(len(a)):
                m += self._num_to_letter(self._decrypt(int(a[i])))
        return m
           
    def _decrypt(self, c):
        n = self.p * self.q
        e = self.e
        phi = (self.p - 1) * (self.q - 1)
        d = 2753
        return mod_exp(c, d, n)
        
    def _convert_to_numeric(self, message):
        m = []

        for i in range(len(message)):
            m.append(self._letter_to_num(message[i]))
        return m
   
   
    def _num_to_letter(self, m):
        return chr(int(m))
           
    def _letter_to_num(self, m):
        return ord(m)
        