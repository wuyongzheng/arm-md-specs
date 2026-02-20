## F6.1.136 VMOV (general-purpose register to scalar)

Copy a general-purpose register to a vector element copies a byte, halfword, or word from a general-purpose register into an Advanced SIMD scalar.

On a Floating-point-only system, this instruction transfers one word to the upper or lower half of a double-precision floating-point register from a general-purpose register. This is an identical operation to the Advanced SIMD single word transfer.

For more information about scalars see Advanced SIMD scalars.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VMOV{<c>}{<q>}{.<size>} <Dd[x]>, <Rt>
```

## Decode for this encoding

```
constant bits(4) opc = opc1:opc2; if opc == '\texttt{0x10}' then UNdefined; constant integer lsb = LowestSetBit(opc<0,3>); constant integer esize = 8 << lsb; constant integer index = UInt(opc<2:lsb>); constant boolean advsimd = (esize < 32); constant integer d = UInt(D:Vd); constant integer t = UInt(Rt); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
VMOV{<c>}{<q>}{.<size>} <Dd[x]>, <Rt>
```

## Decode for this encoding

```
constant bits(4) opc = opc1:opc2; if opc == '\texttt{0x10}' then UNdefined; constant integer lsb = LowestSetBit(opc<0,3>); constant integer esize = 8 << lsb; constant integer index = UInt(opc<2:lsb>); constant boolean advsimd = (esize < 32); constant integer d = UInt(D:Vd); constant integer t = UInt(Rt); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields. <size> The data size. It must be one of: .
```

```
8 Encoded as opc1<1> = 1. [x] is encoded in opc1<0> , opc2 . 16 Encoded as opc1<1> = 0, opc2<0> = 1. [x] is encoded in opc1<0> , opc2<1> 32 Encoded as opc1<1> = 0, opc2 = 0b00 . [x] is encoded in opc1<0> . omitted Equivalent to 32 .
```

## &lt;Dd[x]&gt;

The scalar. The register &lt;Dd&gt; is encoded in D:Vd. For details of how [x] is encoded, see the description of &lt;size&gt; .

## &lt;Rt&gt;

The source general-purpose register.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDOrVFPEnabled(TRUE, advsimd); Elem[D[d],index,esize] = R[t]<esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.