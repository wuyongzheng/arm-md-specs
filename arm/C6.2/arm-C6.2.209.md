## C6.2.209 LDLAR

## Load LOAcquire register

This instruction loads a 32-bit word or 64-bit doubleword from memory, and writes it to a register.

If the destination register is not one of WZR or XZR , LDLAR loads from memory with Acquire semantics.

For more information about memory ordering semantics, see Load LOAcquire, Store LORelease and Load-Acquire, Load-AcquirePC, and Store-Release.

For information about addressing modes, see Load/Store addressing modes.

## No offset

(FEAT\_LOR)

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (size == 10) LDLAR <Wt>, [<Xn|SP>{, #0}]
```

## Encoding for the 64-bit variant

```
Applies when (size == 11) LDLAR <Xt>, [<Xn|SP>{, #0}]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_LOR) then EndOfDecode(Decode_UNDEF);
```

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant integer elsize = 8 << UInt(size); constant integer regsize = if elsize == 64 then 64 else 32; constant boolean acquire = t != 31; constant boolean tagchecked = n != 31;
```

## Assembler Symbols

## &lt;Wt&gt;

Is the 32-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## &lt;Xt&gt;

Is the 64-bit name of the general-purpose register to be transferred, encoded in the 'Rt' field.

## Operation

```
bits(64) address; constant integer dbytes = elsize DIV 8; constant AccessDescriptor accdesc = CreateAccDescLOR(MemOp_LOAD, tagchecked, acquire, t); if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(elsize) data = Mem[address, dbytes, accdesc]; X[t, regsize] = ZeroExtend(data, regsize);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
