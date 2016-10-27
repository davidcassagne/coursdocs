"la valeur est {0:5d}".format(3)
Out[4]: 'la valeur est     3'

"la valeur est {0:8.2f}".format(3)
Out[7]: 'la valeur est     3.00'

"la valeur est {0:10}".format(3)
Out[11]: 'la valeur est          3'

"Nom : {0:10}".format("Durand")
Out[12]: 'Nom : Durand    '

"Nom : {0:>10}".format("Durand")
Out[13]: 'Nom :     Durand'

'<'	The field will be left-aligned within the available space. This is usually the default for strings.
'>'	The field will be right-aligned within the available space. This is the default for numbers.
'0'	If the width field is preceded by a zero ('0') character, sign-aware zero-padding for numeric types will be enabled.


 "la valeur est {0:<8.2f}".format(3)
Out[14]: 'la valeur est 3.00    '

"la valeur est {0:08.2f}".format(3)
Out[15]: 'la valeur est 00003.00'

'+'	indicates that a sign should be used for both positive as well as negative numbers.
'-'	indicates that a sign should be used only for negative numbers, which is the default behavior.
space	indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.

"la valeur est {0:+5d}".format(3)
Out[17]: 'la valeur est    +3'

 "la valeur est {0:+5d}".format(-3)
Out[18]: 'la valeur est    -3'

 "la valeur est {0:< 5d}".format(-3)
Out[19]: 'la valeur est -3   '

"la valeur est {0:< 5d}".format(3)
Out[20]: 'la valeur est  3   '

"la valeur est {0:<5d}".format(3)
Out[21]: 'la valeur est 3    '
