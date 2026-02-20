## F6.1.138 VMOV (scalar to general-purpose register)

Copy a vector element to a general-purpose register with sign or zero extension

Copy a vector element to a general-purpose register with sign or zero extension copies a byte, halfword, or word from an Advanced SIMD scalar to a general-purpose register. Bytes and halfwords can be either zero-extended or sign-extended.

On a Floating-point-only system, this instruction transfers one word from the upper or lower half of a double-precision floating-point register to a general-purpose register. This is an identical operation to the Advanced SIMD single word transfer.

For more information about scalars see Advanced SIMD scalars.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VMOV{<c>}{<q>}{.<dt>} <Rt>, <Dn[x]>
```

## Decode for this encoding

```
constant bits(4) opc = opc1:opc2; if (U:opc) IN {'1\texttt{0x00}', 'x\texttt{0x10}'} then UNdefined; constant integer lsb = LowestSetBit(opc<0,3>); constant integer esize = 8 << lsb; constant integer index = UInt(opc<2:lsb>); constant boolean advsimd = (esize < 32); constant boolean unsigned = (U == '1'); constant integer t = UInt(Rt); constant integer n = UInt(N:Vn); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
VMOV{<c>}{<q>}{.<dt>} <Rt>, <Dn[x]>
```

## Decode for this encoding

```
constant bits(4) opc = opc1:opc2; if (U:opc) IN {'1\texttt{0x00}', 'x\texttt{0x10}'} then UNdefined; constant integer lsb = LowestSetBit(opc<0,3>); constant integer esize = 8 << lsb; constant integer index = UInt(opc<2:lsb>); constant boolean advsimd = (esize < 32); constant boolean unsigned = (U == '1'); constant integer t = UInt(Rt); constant integer n = UInt(N:Vn); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields. <dt> The data type. It must be one of: S8 Encoded as U = 0, opc1<1> = 1. [x] is encoded in opc1<0> , opc2 . S16 Encoded as U = 0, opc1<1> = 0, opc2<0> = 1. [x] is encoded in opc1<0> , opc2<1> . U8 Encoded as U = 1, opc1<1> = 1. [x] is encoded in opc1<0> , opc2 . U16 Encoded as U = 1, opc1<1> = 0, opc2<0> = 1. [x] is encoded in opc1<0> , opc2<1> . 32 Encoded as U = 0, opc1<1> = 0, opc2 = 0b00 . [x] is encoded in opc1<0> . omitted Equivalent to 32 .
```

## &lt;Rt&gt;

The destination general-purpose register.

## &lt;Dn[x]&gt;

The scalar. For details of how [x] is encoded see the description of &lt;dt&gt; .

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDOrVFPEnabled(TRUE, advsimd); if unsigned then R[t] = ZeroExtend(Elem[D[n],index,esize], 32); else R[t] = SignExtend(Elem[D[n],index,esize], 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.