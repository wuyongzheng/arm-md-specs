## C8.2.534 PTRUES

Initialize predicate from named constraint and set the condition flags

This instruction sets elements of the destination predicate to true if the element number satisfies the named predicate constraint, or to false otherwise. If the constraint specifies more elements than are available at the current vector length, then all elements of the destination predicate are set to false.

The named predicate constraint limits the number of active elements in a single predicate to:

- Afixed number (VL1 to VL256)
- The largest power of two (POW2)
- The largest multiple of three or four (MUL3 or MUL4)
- All available, implicitly a multiple of two (ALL).

Unspecified or out of range constraint encodings generate an empty predicate or zero element count rather than Undefined Instruction exception. This instruction sets the First (N), None (Z), and !Last (C) condition flags based on the predicate result, and sets the V flag to zero.

## Setting the condition flags

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
PTRUES <Pd>.<T>{, <pattern>}
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer d = UInt(Pd); constant boolean setflags = TRUE; constant bits(5) pat = pattern;
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

Is the size specifier, encoded in 'size':

<!-- image -->

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

## &lt;pattern&gt;

Is the optional pattern specifier, defaulting to ALL, encoded in 'pattern':

| pattern   | <pattern>   |
|-----------|-------------|
| 00000     | POW2        |
| 00001     | VL1         |
| 00010     | VL2         |
| 00011     | VL3         |
| 00100     | VL4         |
| 00101     | VL5         |
| 00110     | VL6         |
| 00111     | VL7         |
| 01000     | VL8         |
| 01001     | VL16        |
| 01010     | VL32        |
| 01011     | VL64        |
| 01100     | VL128       |
| 01101     | VL256       |
| 0111x     | #uimm5      |
| 101x1     | #uimm5      |
| 10110     | #uimm5      |
| 1x0x1     | #uimm5      |
| 1x010     | #uimm5      |
| 1xx00     | #uimm5      |
| 11101     | MUL4        |
| 11110     | MUL3        |
| 11111     | ALL         |

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; constant integer elements = VL DIV esize; constant integer count = DecodePredCount(pat, esize); bits(PL) result; constant integer psize = esize DIV 8; for e = 0 to elements-1 constant bit pbit = if e < count then '1' else '0'; Elem[result, e, psize] = ZeroExtend(pbit, psize); if setflags then PSTATE.<N,Z,C,V> = PredTest(result, result, esize); P[d, PL] = result;
```

size

&lt;T&gt;

## Operational Information

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the NZCV condition flags written by this instruction might be significantly delayed.