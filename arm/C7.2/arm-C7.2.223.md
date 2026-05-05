## C7.2.223 LDFADD, LDFADDA, LDFADDAL, LDFADDL

Atomic floating-point add

This instruction atomically loads a 16-bit, 32-bit, or 64-bit value from memory, performs a floating-point add with the value held in a register, and stores the result back to memory. The value initially loaded from memory is returned in the destination register.

- LDFADDA and LDFADDAL load from memory with acquire semantics.
- LDFADDL and LDFADDAL store to memory with release semantics.
- LDFADD has neither acquire nor release semantics.

## This instruction:

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
Applies when (size == 01 && A == 0 && R == 0)
```

```
LDFADD <Hs>, <Ht>, [<Xn|SP>]
```

## Encoding for the Half-precision acquire variant

```
Applies when (size == 01 && A == 1 && R ==
```

```
LDFADDA
```

```
0) <Hs>, <Ht>, [<Xn|SP>]
```

## Encoding for the Half-precision acquire-release variant

```
Applies when (size == 01 && A == 1 && R ==
```

```
LDFADDAL
```

```
1) <Hs>, <Ht>, [<Xn|SP>]
```

## Encoding for the Half-precision release variant

```
Applies when (size == 01 && A == 0 && R ==
```

```
LDFADDL
```

```
1) <Hs>, <Ht>, [<Xn|SP>]
```

## Encoding for the Single-precision no memory ordering variant

```
Applies when (size == 10 && A == 0 && R == 0)
```

```
LDFADD <Ss>, <St>, [<Xn|SP>]
```

## Encoding for the Single-precision acquire variant

```
Applies when (size == 10 && A == 1 && R == 0)
```

```
LDFADDA <Ss>, <St>, [<Xn|SP>]
```

## Encoding for the Single-precision acquire-release variant

```
Applies when (size == 10 && A == 1 && R == 1)
```

```
LDFADDAL <Ss>, <St>, [<Xn|SP>]
```

## Encoding for the Single-precision release variant

```
Applies when (size == 10 && A == 0 && R == 1)
```

LDFADDL

&lt;Ss&gt;, &lt;St&gt;, [&lt;Xn|SP&gt;]

## Encoding for the Double-precision no memory ordering variant

```
Applies when (size == 11 && A == 0 && R == 0)
```

```
LDFADD <Ds>, <Dt>, [<Xn|SP>]
```

## Encoding for the Double-precision acquire variant

```
Applies when (size == 11 && A == 1 && R == 0)
```

```
LDFADDA <Ds>, <Dt>, [<Xn|SP>]
```

## Encoding for the Double-precision acquire-release variant

```
Applies when (size == 11 && A == 1 && R ==
```

```
LDFADDAL
```

```
1) <Ds>, <Dt>, [<Xn|SP>]
```

## Encoding for the Double-precision release variant

```
Applies when (size == 11 && A == 0 && R == 1)
```

```
LDFADDL <Ds>, <Dt>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_LSFE) then constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer s = UInt(Rs); constant integer datasize = 8 << UInt(size); constant boolean acquire = A == '1'; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Hs&gt;

Is the 16-bit name of the SIMD&amp;FP register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## &lt;Ht&gt;

Is the 16-bit name of the SIMD&amp;FP register to be loaded, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Ss&gt;

<!-- image -->

## &lt;Ds&gt;

## &lt;Dt&gt;

Is the 64-bit name of the SIMD&amp;FP register to be loaded, encoded in the 'Rt' field.

## Operation

```
AArch64.CheckFPEnabled(); bits(64) address; bits(datasize) value; bits(datasize) data; constant AccessDescriptor accdesc = CreateAccDescFPAtomicOp(MemAtomicOp_FPADD, acquire, release, tagchecked); value = V[s, datasize]; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(datasize) comparevalue = bits(datasize) UNKNOWN; // Irrelevant when not executing CAS data = MemAtomic(address, comparevalue, value, accdesc); V[t, datasize] = data;
```

Is the 32-bit name of the SIMD&amp;FP register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

Is the 32-bit name of the SIMD&amp;FP register to be loaded, encoded in the 'Rt' field.

Is the 64-bit name of the SIMD&amp;FP register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.
