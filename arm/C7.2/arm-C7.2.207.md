## C7.2.207 LD2 (multiple structures)

Load multiple 2-element structures to two registers

This instruction loads multiple 2-element structures from memory and writes the result to the two SIMD&amp;FP registers, with de-interleaving.

For an example of de-interleaving, see LD3 (multiple structures) .

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: No offset and Post-index

## No offset

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
LD2 { <Vt>.<T>, <Vt2>.<T> }, [<Xn|SP>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = integer UNKNOWN; constant boolean wback = FALSE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Post-index

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the Immediate offset variant

```
Applies when (Rm == 11111) LD2 { <Vt>.<T>, <Vt2>.<T> }, [<Xn|SP>], <imm>
```

## Encoding for the Register offset variant

```
Applies when (Rm != 11111) LD2 { <Vt>.<T>, <Vt2>.<T> }, [<Xn|SP>], <Xm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = TRUE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Assembler Symbols

&lt;Vt&gt;

Is the name of the first or only SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size |   Q | <T>      |
|--------|-----|----------|
|     00 |   0 | 8B       |
|     00 |   1 | 16B      |
|     01 |   0 | 4H       |
|     01 |   1 | 8H       |
|     10 |   0 | 2S       |
|     10 |   1 | 4S       |
|     11 |   0 | RESERVED |
|     11 |   1 | 2D       |

## &lt;Vt2&gt;

Is the name of the second SIMD&amp;FP register to be transferred, encoded as 'Rt' plus 1 modulo 32.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

Is the post-index immediate offset, encoded in 'Q':

## &lt;Xm&gt;

Is the 64-bit name of the general-purpose post-index register, excluding XZR, encoded in the 'Rm' field.

&lt;T&gt;

|   Q | <imm>   |
|-----|---------|
|   0 | #16     |
|   1 | #32     |

## Shared Decode

```
constant integer{} datasize = 64 << UInt(Q); constant integer{} esize = 8 << UInt(size); constant integer elements = datasize DIV esize; constant integer rpt = 1; constant integer selem = 2; // .1D format only permitted with LD1 & ST1 if size:Q == '110' && selem != 1 then
```

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); bits(64) address; bits(64) eaddr; bits(64) offs; bits(datasize) rval; integer tt; constant integer ebytes = esize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_LOAD, nontemporal, tagchecked, privileged); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; offs = Zeros(64); for r = 0 to rpt-1 for e = 0 to elements-1 tt = (t + r) MOD 32; for s = 0 to selem-1 rval = V[tt, datasize]; eaddr = AddressIncrement(address, offs, accdesc); Elem[rval, e, esize] = Mem[eaddr, ebytes, accdesc]; V[tt, datasize] = rval; offs = offs + ebytes; tt = (tt + 1) MOD 32; if wback then if m != 31 then offs = X[m, 64]; address = AddressAdd(address, offs, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF); end
```
