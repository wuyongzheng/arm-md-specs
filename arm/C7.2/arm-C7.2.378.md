## C7.2.378 STFADD, STFADDL

Atomic floating-point add, without return

This instruction atomically loads a 16-bit, 32-bit, or 64-bit value from memory, performs a floating-point add with the value held in a register, and stores the result back to memory.

- STFADDL stores to memory with release semantics.
- STFADD has no release semantics.

This instruction:

- Disables alternative floating-point behaviors, as if FPCR.AH is 0.
- Generates only the default NaN, as if FPCR.DN is 1.
- Does not modify the cumulative FPSR exception bits (IDC, IXC, UFC, OFC, DZC, and IOC).
- Disables trapped floating-point exceptions, as if the FPCR trap enable bits (IDE, IXE, UFE, OFE, DZE, and IOE) are all zero.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## Floating-point

(FEAT\_LSFE)

<!-- image -->

## Encoding for the Half-precision no memory ordering variant

```
Applies when (size == 01 && R == 0) STFADD <Hs>, [<Xn|SP>]
```

## Encoding for the Half-precision release variant

```
Applies when (size == 01 && R == 1) STFADDL <Hs>, [<Xn|SP>]
```

## Encoding for the Single-precision no memory ordering variant

```
Applies when (size == 10 && R == 0) STFADD <Ss>, [<Xn|SP>]
```

## Encoding for the Single-precision release variant

```
Applies when (size == 10 && R == STFADDL <Ss>, [<Xn|SP>]
```

```
1)
```

## Encoding for the Double-precision no memory ordering variant

Applies when

STFADD

(size ==

&lt;Ds&gt;, [&lt;Xn|SP&gt;]

11

&amp;&amp;

R

==

0)

## Encoding for the Double-precision release variant

```
Applies when (size == 11 && R == 1)
```

```
STFADDL <Ds>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSFE) then EndOfDecode(Decode_UNDEF); constant integer s = UInt(Rs); constant integer n = UInt(Rn); constant integer datasize = 8 << UInt(size); constant boolean acquire = FALSE; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Hs&gt;

Is the 16-bit name of the SIMD&amp;FP register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

<!-- image -->

## &lt;Ds&gt;

Is the 64-bit name of the SIMD&amp;FP register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## Operation

```
AArch64.CheckFPEnabled(); bits(64) address; bits(datasize) value; bits(datasize) data; constant AccessDescriptor accdesc = CreateAccDescFPAtomicOp(MemAtomicOp_FPADD, acquire, release, tagchecked); value = V[s, datasize]; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(datasize) comparevalue = bits(datasize) UNKNOWN; // Irrelevant when not executing CAS data = MemAtomic(address, comparevalue, value, accdesc);
```

Is the 32-bit name of the SIMD&amp;FP register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.
