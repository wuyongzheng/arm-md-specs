## C8.2.530 PSEL

Predicate select between predicate register or all-false

This instruction places the contents of the first source predicate register into the destination predicate register if the indexed element of the second source predicate is true, otherwise it sets the destination predicate to all-false. The indexed element is determined by the sum of a general-purpose index register and an immediate, modulo the number of elements. This instruction does not set the condition flags. For programmer convenience, an assembler must also accept predicate-as-counter register names for the destination predicate register and the first source predicate register.

## SVE2

(FEAT\_SME || FEAT\_SVE2p1)

<!-- image -->

## Encoding

```
PSEL <Pd>, <Pn>, <Pm>.<T>[<Wv>, <imm>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME) && !IsFeatureImplemented(FEAT_SVE2p1) then EndOfDecode(Decode_UNDEF); constant bits(5) imm5 = i1:tszh:tszl; integer esize; integer imm; case tszh:tszl of when '0000' EndOfDecode(Decode_UNDEF); when '1000' esize = 64; imm = UInt(imm5<4>); when 'x100' esize = 32; imm = UInt(imm5<4:3>); when 'xx10' esize = 16; imm = UInt(imm5<4:2>); when 'xxx1' esize = 8; imm = UInt(imm5<4:1>); constant integer n = UInt(Pn); constant integer m = UInt(Pm); constant integer d = UInt(Pd); constant integer v = UInt('011':Rv);
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

&lt;Pn&gt;

Is the name of the first source scalable predicate register, encoded in the 'Pn' field.

&lt;Pm&gt;

Is the name of the second source scalable predicate register, encoded in the 'Pm' field.

&lt;T&gt;

Is the size specifier, encoded in 'tszh:tszl':

## &lt;Wv&gt;

Is the 32-bit name of the vector select register W12-W15, encoded in the 'Rv' field.

## &lt;imm&gt;

Is the element index, in the range 0 to one less than the number of vector elements in a 128-bit vector register, encoded in 'i1:tszh:tszl'.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant bits(PL) operand1 = P[n, PL]; constant bits(PL) operand2 = P[m, PL]; constant bits(32) idx = X[v, 32]; constant integer element = (UInt(idx) + imm) MOD elements; bits(PL) result; if ActivePredicateElement(operand2, element, esize) then result = operand1; else result = Zeros(PL); P[d, PL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| tszh   | tszl   | <T>      |
|--------|--------|----------|
| 0      | 000    | RESERVED |
| x      | xx1    | B        |
| x      | x10    | H        |
| x      | 100    | S        |
| 1      | 000    | D        |