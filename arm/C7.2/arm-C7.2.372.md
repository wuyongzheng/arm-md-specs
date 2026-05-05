## C7.2.372 ST4 (single structure)

Store single 4-element structure from one lane of four registers

This instruction stores a 4-element structure to memory from corresponding elements of four SIMD&amp;FP registers.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: No offset and Post-index

## No offset

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the 8-bit variant

```
Applies when (opcode == 001) ST4 { <Vt>.B, <Vt2>.B, <Vt3>.B, <Vt4>.B }[<index>], [<Xn|SP>]
```

## Encoding for the 16-bit variant

Applies when

```
(opcode == 011 && size == x0) ST4 { <Vt>.H, <Vt2>.H, <Vt3>.H,
```

```
<Vt4>.H }[<index>], [<Xn|SP>]
```

## Encoding for the 32-bit variant

```
Applies when (opcode == 101 && size == 00) ST4 { <Vt>.S, <Vt2>.S, <Vt3>.S,
```

```
<Vt4>.S }[<index>], [<Xn|SP>]
```

## Encoding for the 64-bit variant

```
Applies when (opcode == 101 && S == 0 && size == 01) ST4 { <Vt>.D, <Vt2>.D, <Vt3>.D, <Vt4>.D }[<index>], [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = integer UNKNOWN; constant boolean wback = FALSE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Post-index

## (FEAT\_AdvSIMD)

<!-- image -->

## Encoding for the 8-bit, immediate offset variant

Applies when (Rm == 11111 &amp;&amp;

```
opcode == 001)
```

```
ST4 { <Vt>.B, <Vt2>.B, <Vt3>.B,
```

```
<Vt4>.B }[<index>], [<Xn|SP>], #4
```

## Encoding for the 8-bit, register offset variant

```
Applies when (Rm != 11111 && opcode == 001)
```

```
ST4 { <Vt>.B, <Vt2>.B, <Vt3>.B, <Vt4>.B }[<index>], [<Xn|SP>], <Xm>
```

## Encoding for the 16-bit, immediate offset variant

Applies when (Rm == 11111 &amp;&amp; opcode == 011 &amp;&amp; size ==

```
x0) ST4 { <Vt>.H, <Vt2>.H, <Vt3>.H, <Vt4>.H }[<index>], [<Xn|SP>], #8
```

## Encoding for the 16-bit, register offset variant

Applies when (Rm != 11111 &amp;&amp; opcode == 011 &amp;&amp; size ==

```
x0) ST4 { <Vt>.H, <Vt2>.H, <Vt3>.H, <Vt4>.H }[<index>], [<Xn|SP>],
```

```
<Xm>
```

## Encoding for the 32-bit, immediate offset variant

```
Applies when (Rm == 11111 && opcode == 101 && size == 00)
```

```
ST4 { <Vt>.S, <Vt2>.S, <Vt3>.S, <Vt4>.S }[<index>], [<Xn|SP>], #16
```

## Encoding for the 32-bit, register offset variant

Applies when (Rm != 11111 &amp;&amp; opcode == 101 &amp;&amp; size == 00)

```
ST4 { <Vt>.S, <Vt2>.S, <Vt3>.S, <Vt4>.S }[<index>], [<Xn|SP>], <Xm>
```

## Encoding for the 64-bit, immediate offset variant

Applies when (Rm == 11111 &amp;&amp; opcode == 101 &amp;&amp; S == 0 &amp;&amp; size == 01) ST4 { &lt;Vt&gt;.D, &lt;Vt2&gt;.D, &lt;Vt3&gt;.D, &lt;Vt4&gt;.D }[&lt;index&gt;], [&lt;Xn|SP&gt;], #32

## Encoding for the 64-bit, register offset variant

Applies when (Rm != 11111 &amp;&amp; opcode == 101 &amp;&amp; S == 0 &amp;&amp; size == 01)

```
ST4 { <Vt>.D, <Vt2>.D, <Vt3>.D, <Vt4>.D }[<index>], [<Xn|SP>], <Xm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean wback = TRUE; constant boolean nontemporal = FALSE; constant boolean tagchecked = wback || n != 31;
```

## Assembler Symbols

## &lt;Vt&gt;

Is the name of the first or only SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## &lt;Vt2&gt;

Is the name of the second SIMD&amp;FP register to be transferred, encoded as 'Rt' plus 1 modulo 32.

## &lt;Vt3&gt;

Is the name of the third SIMD&amp;FP register to be transferred, encoded as 'Rt' plus 2 modulo 32.

## &lt;Vt4&gt;

Is the name of the fourth SIMD&amp;FP register to be transferred, encoded as 'Rt' plus 3 modulo 32.

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
bits(2) scale = opcode<2:1>; constant integer selem = UInt(opcode<0>:R) + 1; boolean replicate = FALSE; integer index; case scale of when '11' // load and replicate if L == '0' || S == '1' then EndOfDecode(Decode_UNDEF); end scale = size; replicate = TRUE; when '00' index = UInt(Q:S:size); // B[0-15] when '01' if size<0> == '1' then EndOfDecode(Decode_UNDEF); end
```

```
index = UInt(Q:S:size<1>); // H[0-7] when '10' if size<1> == '1' then EndOfDecode(Decode_UNDEF); end if size<0> == '0' then index = UInt(Q:S); // S[0-3] else if S == '1' then EndOfDecode(Decode_UNDEF); end index = UInt(Q); // D[0-1] scale = '11'; end end constant integer{} datasize = 64 << UInt(Q); constant integer{} esize = 8 << UInt(scale);
```

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); bits(64) address; bits(64) eaddr; bits(64) offs; bits(128) rval; bits(esize) element; constant integer ebytes = esize DIV 8; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_STORE, nontemporal, tagchecked, privileged); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; offs = Zeros(64); if replicate then // load and replicate to all elements for s = 0 to selem-1 eaddr = AddressIncrement(address, offs, accdesc); element = Mem[eaddr, ebytes, accdesc]; // replicate to fill 128or 64-bit register V[t, datasize] = Replicate(element, datasize DIV esize); offs = offs + ebytes; t = (t + 1) MOD 32; else // load/store one element per register for s = 0 to selem-1 rval = V[t, 128]; eaddr = AddressIncrement(address, offs, accdesc); // extract from one lane of 128-bit register Mem[eaddr, ebytes, accdesc] = Elem[rval, index, esize]; offs = offs + ebytes; t = ( t + 1 ) MOD 32; if wback then if m != 31 then offs = X[m, 64]; address = AddressAdd(address, offs, accdesc); if n == 31 then SP[64] = address; else X[n, 64] = address;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
