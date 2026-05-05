## C7.2.391 STUR (SIMD&amp;FP)

Store SIMD&amp;FP register (unscaled offset)

This instruction stores a single SIMD&amp;FP register to memory. The address that is used for the store is calculated from a base register value and an optional immediate offset.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Unscaled offset

(FEAT\_FP)

<!-- image -->

## Encoding for the 8-bit variant

Applies when (size == 00 &amp;&amp; opc == 00)

```
STUR
```

```
<Bt>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 16-bit variant

```
Applies when (size == 01 && opc == 00) STUR <Ht>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 32-bit variant

```
Applies when (size == 10 && opc == 00) STUR <St>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 64-bit variant

```
Applies when (size == 11 && opc == 00) STUR <Dt>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 128-bit variant

```
Applies when (size == 00 && opc == 10) STUR <Qt>, [<Xn|SP>{, #<simm>}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); UInt(size);
```

```
if opc<1> == '1' && size != '00' then EndOfDecode(Decode_UNDEF); constant integer scale = if opc<1> == '1' then 4 else constant bits(64) offset = SignExtend(imm9, 64);
```

## Assembler Symbols

## &lt;Bt&gt;

Is the 8-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;simm&gt;

Is the optional signed immediate byte offset, in the range -256 to 255, defaulting to 0 and encoded in the 'imm9' field.

## &lt;Ht&gt;

## &lt;St&gt;

## &lt;Dt&gt;

## &lt;Qt&gt;

Is the 128-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

## Shared Decode

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer{} datasize = 8 << constant boolean nontemporal = FALSE; constant boolean tagchecked = n != 31;
```

## Operation

```
AArch64.CheckFPEnabled(); bits(64) address; constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_STORE, nontemporal, tagchecked, privileged); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); Mem[address, datasize DIV 8, accdesc] = V[t, datasize];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

Is the 16-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is the 32-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is the 64-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

```
scale;
```
