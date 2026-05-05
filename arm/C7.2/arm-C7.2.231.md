## C7.2.231 LDR (literal, SIMD&amp;FP)

Load SIMD&amp;FP register (PC-relative literal)

This instruction loads a SIMD&amp;FP register from memory. The address that is used for the load is calculated from the PC value and an immediate offset.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Literal

(FEAT\_FP)

<!-- image -->

VR

## Encoding for the 32-bit variant

Applies when (opc ==

```
00) LDR <St>, <label>
```

## Encoding for the 64-bit variant

```
Applies when (opc == 01) LDR <Dt>, <label>
```

## Encoding for the 128-bit variant

```
(opc ==
```

```
Applies when LDR <Qt>, <label>
```

```
10)
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF);
```

```
constant integer t = UInt(Rt); if opc == '11' then EndOfDecode(Decode_UNDEF); constant integer size = 4 << (UInt(opc)); constant boolean nontemporal = FALSE; constant boolean tagchecked = FALSE; constant bits(64) offset = SignExtend(imm19:'00', 64);
```

## Assembler Symbols

&lt;St&gt;

Is the 32-bit name of the SIMD&amp;FP register to be loaded, encoded in the 'Rt' field.

## &lt;label&gt;

Is the program label from which the data is to be loaded. Its offset from the address of this instruction, in the range +/-1MB, is encoded as 'imm19' times 4.

## &lt;Dt&gt;

Is the 64-bit name of the SIMD&amp;FP register to be loaded, encoded in the 'Rt' field.

<!-- image -->

Is the 128-bit name of the SIMD&amp;FP register to be loaded, encoded in the 'Rt' field.

## Operation

```
constant bits(64) address = PC64 + offset; AArch64.CheckFPEnabled(); constant boolean privileged = PSTATE.EL != EL0; constant AccessDescriptor accdesc = CreateAccDescASIMD(MemOp_LOAD, nontemporal, tagchecked, privileged); constant bits(size*8) data = Mem[address, size, accdesc]; V[t, size*8] = data;
```
