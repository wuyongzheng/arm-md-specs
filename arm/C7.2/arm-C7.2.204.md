## C7.2.204 LD1 (multiple structures)

Load multiple single-element structures to one, two, three, or four registers

This instruction loads multiple single-element structures from memory and writes the result to one, two, three, or four SIMD&amp;FP registers.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: No offset and Post-index

## No offset

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the One register variant

Applies when (opcode == 0111)

```
LD1 { <Vt>.<T> }, [<Xn|SP>]
```

## Encoding for the Two registers variant

```
Applies when (opcode == 1010) LD1 { <Vt>.<T>, <Vt2>.<T> }, [<Xn|SP>]
```

## Encoding for the Three registers variant

Applies when

```
(opcode == 0110) LD1 { <Vt>.<T>, <Vt2>.<T>, <Vt3>.<T>
```

## Encoding for the Four registers variant

Applies when (opcode ==

```
0010)
```

```
LD1 { <Vt>.<T>, <Vt2>.<T>, <Vt3>.<T>, <Vt4>.<T> }, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = integer UNKNOWN; constant boolean wback = FALSE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

```
}, [<Xn|SP>]
```

## Post-index

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the One register, immediate offset variant

Applies when (Rm == 11111 &amp;&amp; opcode == 0111)

```
LD1 { <Vt>.<T> }, [<Xn|SP>],
```

```
<imm>
```

## Encoding for the One register, register offset variant

```
Applies when
```

(Rm != 11111 &amp;&amp; opcode == 0111)

```
LD1 { <Vt>.<T> }, [<Xn|SP>], <Xm>
```

## Encoding for the Two registers, immediate offset variant

```
Applies when (Rm == 11111 &&
```

```
opcode == 1010)
```

```
LD1 { <Vt>.<T>, <Vt2>.<T> }, [<Xn|SP>], <imm>
```

## Encoding for the Two registers, register offset variant

Applies when (Rm != 11111 &amp;&amp;

```
opcode == 1010) LD1 { <Vt>.<T>, <Vt2>.<T> }, [<Xn|SP>], <Xm>
```

## Encoding for the Three registers, immediate offset variant

```
Applies when (Rm == 11111 && opcode == 0110) LD1 { <Vt>.<T>, <Vt2>.<T>, <Vt3>.<T> }, [<Xn|SP>],
```

```
<imm>
```

## Encoding for the Three registers, register offset variant

Applies when (Rm != 11111 &amp;&amp; opcode == 0110)

```
LD1 { <Vt>.<T>, <Vt2>.<T>, <Vt3>.<T> }, [<Xn|SP>], <Xm>
```

## Encoding for the Four registers, immediate offset variant

Applies when (Rm == 11111 &amp;&amp;

```
opcode == 0010)
```

```
LD1 { <Vt>.<T>, <Vt2>.<T>, <Vt3>.<T>, <Vt4>.<T> }, [<Xn|SP>],
```

## Encoding for the Four registers, register offset variant

Applies when (Rm != 11111 &amp;&amp; opcode == 0010)

```
LD1 { <Vt>.<T>, <Vt2>.<T>, <Vt3>.<T>, <Vt4>.<T> }, [<Xn|SP>], <Xm>
```

```
<imm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = TRUE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Assembler Symbols

## &lt;Vt&gt;

Is the name of the first or only SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size |   Q | <T>   |
|--------|-----|-------|
|     00 |   0 | 8B    |
|     00 |   1 | 16B   |
|     01 |   0 | 4H    |
|     01 |   1 | 8H    |
|     10 |   0 | 2S    |
|     10 |   1 | 4S    |
|     11 |   0 | 1D    |
|     11 |   1 | 2D    |

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Vt2&gt;

Is the name of the second SIMD&amp;FP register to be transferred, encoded as 'Rt' plus 1 modulo 32.

## &lt;Vt3&gt;

Is the name of the third SIMD&amp;FP register to be transferred, encoded as 'Rt' plus 2 modulo 32.

## &lt;Vt4&gt;

Is the name of the fourth SIMD&amp;FP register to be transferred, encoded as 'Rt' plus 3 modulo 32.

## &lt;imm&gt;

For the 'One register, immediate offset' variant: is the post-index immediate offset, encoded in 'Q':

|   Q | <imm>   |
|-----|---------|
|   0 | #8      |

&lt;T&gt;

<!-- image -->

## &lt;Xm&gt;

Is the 64-bit name of the general-purpose post-index register, excluding XZR, encoded in the 'Rm' field.

## Shared Decode

```
constant integer{} datasize = 64 << UInt(Q); constant integer{} esize = 8 << UInt(size); constant integer elements = datasize DIV esize; integer rpt; // number of iterations constant integer selem = 1; // structure elements case opcode of when '0010' rpt = 4; // LD/ST1 (4 registers) when '0110' rpt = 3; // LD/ST1 (3 registers) when '1010' rpt = 2; // LD/ST1 (2 registers) when '0111' rpt = 1; // LD/ST1 (1 register) otherwise EndOfDecode(Decode_UNDEF); end
```

|   Q | <imm>   |
|-----|---------|
|   1 | #16     |

For the 'Two registers, immediate offset' variant: is the post-index immediate offset, encoded in 'Q':

|   Q | <imm>   |
|-----|---------|
|   0 | #16     |
|   1 | #32     |

For the 'Three registers, immediate offset' variant: is the post-index immediate offset, encoded in 'Q':

|   Q | <imm>   |
|-----|---------|
|   0 | #24     |
|   1 | #48     |

For the 'Four registers, immediate offset' variant: is the post-index immediate offset, encoded in 'Q':

|   Q | <imm>   |
|-----|---------|
|   0 | #32     |
|   1 | #64     |

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); bits(64) address; bits(64) eaddr; bits(64) offs; bits(datasize) rval; integer tt; constant integer ebytes = esize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_LOAD, nontemporal, tagchecked, privileged); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; offs = Zeros(64); for r = 0 to rpt-1 for e = 0 to elements-1 tt = (t + r) MOD 32; for s = 0 to selem-1 rval = V[tt, datasize]; eaddr = AddressIncrement(address, offs, accdesc); Elem[rval, e, esize] = Mem[eaddr, ebytes, accdesc]; V[tt, datasize] = rval; offs = offs + ebytes; tt = (tt + 1) MOD 32; if wback then if m != 31 then offs = X[m, 64]; address = AddressAdd(address, offs, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
