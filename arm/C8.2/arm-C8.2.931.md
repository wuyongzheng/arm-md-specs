## C8.2.931 WHILERW

While free of read-after-write conflicts

This instruction checks two addresses for a conflict or overlap between address ranges of the form [addr,addr+VL÷8), where VL is the accessible vector length in bits, that could result in a loop-carried dependency through memory due to the use of these addresses by contiguous load and store instructions within the same iteration of a loop. Generate a predicate whose elements are true while the addresses cannot conflict within the same iteration, and false thereafter. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

## SVE2

(FEAT\_SVE2 || FEAT\_SME)

<!-- image -->

## Encoding

```
WHILERW <Pd>.<T>, <Xn>, <Xm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE2) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer d = UInt(Pd);
```

## Assembler Symbols

## &lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

&lt;T&gt;

## &lt;Xn&gt;

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the 64-bit name of the first source general-purpose register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second source general-purpose register, encoded in the 'Rm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) mask = Ones(PL); constant bits(64) src1 = X[n, 64]; constant bits(64) src2 = X[m, 64]; constant integer operand1 = UInt(src1); constant integer operand2 = UInt(src2); bits(PL) result; constant integer psize = esize DIV 8; constant integer diff = Abs(operand2 operand1) DIV (esize DIV 8); for e = 0 to elements-1 if diff == 0 || e < diff then Elem[result, e, psize] = ZeroExtend('1', psize); else Elem[result, e, psize] = ZeroExtend('0', psize); PSTATE.<N,Z,C,V> = PredTest(mask, result, esize); P[d, PL] = result;
```