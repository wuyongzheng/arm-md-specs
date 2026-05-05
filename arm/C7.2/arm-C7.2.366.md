## C7.2.366 ST1 (single structure)

Store a single-element structure from one lane of one register

This instruction stores the specified element of a SIMD&amp;FP register to memory.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: No offset and Post-index

## No offset

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the 8-bit variant

```
Applies when (opcode == 000) ST1 { <Vt>.B }[<index>], [<Xn|SP>]
```

## Encoding for the 16-bit variant

```
Applies when
```

```
(opcode == 010 && size == x0) ST1 { <Vt>.H }[<index>], [<Xn|SP>]
```

## Encoding for the 32-bit variant

```
Applies when (opcode == 100 && size == 00) ST1 { <Vt>.S }[<index>], [<Xn|SP>]
```

## Encoding for the 64-bit variant

```
Applies when (opcode == 100 && S == 0 && size == 01) ST1 { <Vt>.D }[<index>], [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = integer UNKNOWN; constant boolean wback = FALSE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Post-index

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the 8-bit, immediate offset variant

```
Applies when (Rm == 11111 &&
```

```
ST1 { <Vt>.B
```

```
opcode == 000) }[<index>], [<Xn|SP>], #1
```

## Encoding for the 8-bit, register offset variant

```
Applies when (Rm != 11111 && opcode == 000) ST1 { <Vt>.B }[<index>], [<Xn|SP>], <Xm>
```

## Encoding for the 16-bit, immediate offset variant

```
Applies when (Rm == 11111 && opcode == 010 && size == x0)
```

```
ST1 { <Vt>.H }[<index>], [<Xn|SP>], #2
```

## Encoding for the 16-bit, register offset variant

Applies when (Rm != 11111 &amp;&amp; opcode == 010 &amp;&amp; size ==

```
ST1 { <Vt>.H }[<index>], [<Xn|SP>],
```

```
x0) <Xm>
```

## Encoding for the 32-bit, immediate offset variant

```
Applies when (Rm == 11111 && opcode == 100 && size == 00) ST1 { <Vt>.S }[<index>], [<Xn|SP>], #4
```

## Encoding for the 32-bit, register offset variant

```
Applies when (Rm != 11111 && opcode == 100 && size == 00)
```

```
ST1 { <Vt>.S }[<index>], [<Xn|SP>], <Xm>
```

## Encoding for the 64-bit, immediate offset variant

```
Applies when (Rm == 11111 && opcode == 100 && S == 0 && size == 01)
```

```
ST1 { <Vt>.D }[<index>], [<Xn|SP>], #8
```

## Encoding for the 64-bit, register offset variant

```
Applies when (Rm != 11111 && opcode == 100 && S == 0 && size == 01)
```

```
ST1 { <Vt>.D }[<index>], [<Xn|SP>], <Xm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = TRUE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Assembler Symbols

## &lt;Vt&gt;

Is the name of the first or only SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## &lt;index&gt;

For the '8-bit', '8-bit, immediate offset', and '8-bit, register offset' variants: is the element index, encoded in 'Q:S:size'.

For the '16-bit', '16-bit, immediate offset', and '16-bit, register offset' variants: is the element index, encoded in 'Q:S:size&lt;1&gt;'.

For the '32-bit', '32-bit, immediate offset', and '32-bit, register offset' variants: is the element index, encoded in 'Q:S'.

For the '64-bit', '64-bit, immediate offset', and '64-bit, register offset' variants: is the element index, encoded in 'Q'.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the general-purpose post-index register, excluding XZR, encoded in the 'Rm' field.

## Shared Decode

```
bits(2) scale = opcode<2:1>; constant integer selem = UInt(opcode<0>:R) + 1; boolean replicate = FALSE; integer index; case scale of when '11' // load and replicate if L == '0' || S == '1' then EndOfDecode(Decode_UNDEF); end scale = size; replicate = TRUE; when '00' index = UInt(Q:S:size); // B[0-15] when '01' if size<0> == '1' then EndOfDecode(Decode_UNDEF); end index = UInt(Q:S:size<1>); // H[0-7] when '10' if size<1> == '1' then EndOfDecode(Decode_UNDEF); end if size<0> == '0' then index = UInt(Q:S); // S[0-3] else if S == '1' then EndOfDecode(Decode_UNDEF); end index = UInt(Q); // D[0-1] scale = '11'; end end
```

```
constant integer{} datasize = 64 << UInt(Q); constant integer{} esize = 8 << UInt(scale);
```

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); bits(64) address; bits(64) eaddr; bits(64) offs; bits(128) rval; bits(esize) element; constant integer ebytes = esize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_STORE, nontemporal, tagchecked, privileged); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; offs = Zeros(64); if replicate then // load and replicate to all elements for s = 0 to selem-1 eaddr = AddressIncrement(address, offs, accdesc); element = Mem[eaddr, ebytes, accdesc]; // replicate to fill 128or 64-bit register V[t, datasize] = Replicate(element, datasize DIV esize); offs = offs + ebytes; t = (t + 1) MOD 32; else // load/store one element per register for s = 0 to selem-1 rval = V[t, 128]; eaddr = AddressIncrement(address, offs, accdesc); // extract from one lane of 128-bit register Mem[eaddr, ebytes, accdesc] = Elem[rval, index, esize]; offs = offs + ebytes; t = ( t + 1 ) MOD 32; if wback then if m != 31 then offs = X[m, 64]; address = AddressAdd(address, offs, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
