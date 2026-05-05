## C7.2.212 LD3R

Load single 3-element structure and replicate to all lanes of three registers

This instruction loads a 3-element structure from memory and replicates the structure to all the lanes of the three SIMD&amp;FP registers.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: No offset and Post-index

## No offset

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
LD3R { <Vt>.<T>, <Vt2>.<T>, <Vt3>.<T> }, [<Xn|SP>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = integer UNKNOWN; constant boolean wback = FALSE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Post-index

## (FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the Immediate offset variant

```
Applies when (Rm == 11111) LD3R { <Vt>.<T>, <Vt2>.<T>, <Vt3>.<T> }, [<Xn|SP>], <imm>
```

## Encoding for the Register offset variant

Applies when

```
(Rm != 11111) LD3R { <Vt>.<T>, <Vt2>.<T>, <Vt3>.<T> }, [<Xn|SP>], <Xm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = TRUE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Assembler Symbols

&lt;Vt&gt;

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

## &lt;Vt2&gt;

Is the name of the second SIMD&amp;FP register to be transferred, encoded as 'Rt' plus 1 modulo 32.

## &lt;Vt3&gt;

Is the name of the third SIMD&amp;FP register to be transferred, encoded as 'Rt' plus 2 modulo 32.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;imm&gt;

Is the post-index immediate offset, encoded in 'size':

|   size | <imm>   |
|--------|---------|
|     00 | #3      |
|     01 | #6      |
|     10 | #12     |
|     11 | #24     |

&lt;T&gt;

<!-- image -->

Is the 64-bit name of the general-purpose post-index register, excluding XZR, encoded in the 'Rm' field.

## Shared Decode

```
bits(2) scale = opcode<2:1>; constant integer selem = UInt(opcode<0>:R) + 1; boolean replicate = FALSE; integer index; case scale of when '11' // load and replicate if L == '0' || S == '1' then scale = size; replicate = TRUE; when '00' index = UInt(Q:S:size); // B[0-15] when '01' if size<0> == '1' then EndOfDecode(Decode_UNDEF); end index = UInt(Q:S:size<1>); // H[0-7] when '10' if size<1> == '1' then EndOfDecode(Decode_UNDEF); end if size<0> == '0' then index = UInt(Q:S); // S[0-3] else if S == '1' then EndOfDecode(Decode_UNDEF); end index = UInt(Q); // D[0-1] scale = '11'; end end constant integer{} datasize = 64 << UInt(Q); constant integer{} esize = 8 << UInt(scale);
```

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); bits(64) address; bits(64) eaddr; bits(64) offs; bits(128) rval; bits(esize) element; constant integer ebytes = esize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_LOAD, nontemporal, tagchecked, privileged); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; offs = Zeros(64); if replicate then // load and replicate to all elements for s = 0 to selem-1 eaddr = AddressIncrement(address, offs, accdesc); element = Mem[eaddr, ebytes, accdesc]; // replicate to fill 128or 64-bit register V[t, datasize] = Replicate(element, datasize DIV esize);
```

```
EndOfDecode(Decode_UNDEF); end
```

```
offs = offs + ebytes; t = (t + 1) MOD 32; else // load/store one element per register for s = 0 to selem-1 rval = V[t, 128]; eaddr = AddressIncrement(address, offs, accdesc); Elem[rval, index, esize] = Mem[eaddr, ebytes, accdesc]; V[t, 128] = rval; offs = offs + ebytes; t = ( t + 1 ) MOD 32; if wback then if m != 31 then offs = X[m, 64]; address = AddressAdd(address, offs, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
