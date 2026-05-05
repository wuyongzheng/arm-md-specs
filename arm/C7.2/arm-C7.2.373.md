## C7.2.373 STBFADD, STBFADDL

Atomic BFloat16 floating-point add, without return

This instruction atomically loads a 16-bit value from memory, adds it to the BFloat16 value held in a register, and stores the result back to memory.

- STBFADDL stores to memory with release semantics.
- STBFADD has no release semantics.

This instruction:

- Disables alternative floating-point behaviors, as if FPCR.AH is 0.
- Generates only the default NaN, as if FPCR.DN is 1.
- Does not modify the cumulative FPSR exception bits (IDC, IXC, UFC, OFC, DZC, and IOC).
- Disables trapped floating-point exceptions, as if the FPCR trap enable bits (IDE, IXE, UFE, OFE, DZE, and IOE) are all zero.

For more information about memory ordering semantics, see Load-Acquire, Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## Floating-point

## (FEAT\_LSFE)

<!-- image -->

## Encoding for the No memory ordering variant

```
Applies when (R == 0) STBFADD <Hs>, [<Xn|SP>]
```

## Encoding for the Release variant

```
Applies when (R == 1) STBFADDL <Hs>, [<Xn|SP>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LSFE) then EndOfDecode(Decode_UNDEF); constant integer s = UInt(Rs); constant integer n = UInt(Rn); constant integer datasize = 16; constant boolean acquire = FALSE; constant boolean release = R == '1'; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Hs&gt;

Is the 16-bit name of the SIMD&amp;FP register holding the data value to be operated on with the contents of the memory location, encoded in the 'Rs' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPEnabled(); bits(64) address; bits(datasize) value; bits(datasize) data; constant AccessDescriptor accdesc = CreateAccDescFPAtomicOp(MemAtomicOp_BFADD, acquire, release, tagchecked); value = V[s, datasize]; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(datasize) comparevalue = bits(datasize) UNKNOWN; // Irrelevant when not executing CAS data = MemAtomic(address, comparevalue, value, accdesc);
```
