## C7.2.217 LDAPUR (SIMD&amp;FP)

Load-acquire RCpc SIMD&amp;FP register (unscaled offset)

This instruction loads a SIMD&amp;FP register from memory. The address that is used for the load is calculated from a base register value and an optional immediate offset.

The instruction has memory ordering semantics as described in Load-Acquire, Load-AcquirePC, and Store-Release, except that:

- There is no ordering requirement, separate from the requirements of a Load-AcquirePC or a Store-Release, created by having a Store-Release followed by a Load-AcquirePC instruction.
- The reading of a value written by a Store-Release by a Load-AcquirePC instruction by the same observer does not make the write of the Store-Release globally observed.

This difference in memory ordering is not described in the pseudocode.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Unscaled offset

(FEAT\_FP &amp;&amp; FEAT\_LRCPC3)

<!-- image -->

## Encoding for the 8-bit variant

```
Applies when (size == 00 && opc == 01) LDAPUR <Bt>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 16-bit variant

```
Applies when (size == 01 && opc == 01) LDAPUR <Ht>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 32-bit variant

```
Applies when (size == 10 && opc == 01) LDAPUR <St>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 64-bit variant

```
Applies when (size == 11 && opc == 01) LDAPUR <Dt>, [<Xn|SP>{, #<simm>}]
```

## Encoding for the 128-bit variant

```
Applies when (size == 00 && opc == 11) LDAPUR <Qt>, [<Xn|SP>{, #<simm>}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) || !IsFeatureImplemented(FEAT_LRCPC3) then EndOfDecode(Decode_UNDEF); if opc<1> == '1' && size != '00' then EndOfDecode(Decode_UNDEF); constant integer scale = if opc<1> == '1' then 4 else UInt(size); constant bits(64) offset = SignExtend(imm9, 64);
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
AArch64.CheckFPAdvSIMDEnabled(); bits(64) address; constant AccessDescriptor accdesc = if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; address = AddressAdd(address, offset, accdesc); V[t, datasize] = Mem[address, datasize DIV 8, accdesc];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

Is the 16-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is the 32-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

Is the 64-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Rt' field.

```
scale;
```

```
CreateAccDescASIMDAcqRel(MemOp_LOAD, tagchecked);
```
