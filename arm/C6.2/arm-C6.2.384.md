## C6.2.384 ST64BV0

Single-copy atomic 64-byte EL0 store with status result

This instruction stores eight 64-bit doublewords from consecutive registers to a memory location, with the bottom 32 bits taken from ACCDATA\_EL1, and writes the status result of the store to a register. The store starts at register Xt , with the data being formed as Data[511:0] =

X(t+7)::X(t+6)::X(t+5)::X(t+4)::X(t+3)::X(t+2)::X(t+1)::Xt[63:32]::ACCDATA\_EL1()[31:0] . The data is stored atomically and is required to be 64-byte aligned.

It is IMPLEMENTATION DEFINED which memory locations support this instruction. A memory location that supports ST64BV0 also supports ST64BV .

For more information, including about the memory types accessible and how the accesses are performed, see Single-copy atomic 64-byte load/store.

## Integer

(FEAT\_LS64\_ACCDATA)

<!-- image -->

## Encoding

```
ST64BV0 <Xs>, <Xt>, [<Xn|SP>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LS64_ACCDATA) then EndOfDecode(Decode_UNDEF); if Rt<4:3> == '11' || Rt<0> == '1' then EndOfDecode(Decode_UNDEF); constant boolean withstatus = TRUE; constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean tagchecked = n != 31;
```

## Assembler Symbols

<!-- image -->

Is the 64-bit name of the general-purpose register into which the status result of this instruction is written, encoded in the 'Rs' field.

The value returned is:

0xFFFFFFFF \_FFFFFFFF If the memory location accessed does not support this instruction. In this case, the value at the memory location is UNKNOWN.

!= 0xFFFFFFFF \_FFFFFFFF If the memory location accessed does support this instruction. In this case, the peripheral that provides the response defines the returned value and provides information on the state of the memory update at the memory location.

If XZR is used, then the return value is ignored.

## &lt;Xt&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
CheckST64BV0Enabled(); bits(512) data; bits(64) address; bits(64) value; constant AccessDescriptor accdesc = CreateAccDescLS64(MemOp_STORE, withstatus, tagchecked); constant bits(64) Xt = X[t, 64]; value<31:0> = ACCDATA_EL1<31:0>; value<63:32> = Xt<63:32>; if BigEndian(accdesc.acctype) then value = BigEndianReverse(value); data<63:0> = value; for i = 1 to 7 value = X[t+i, 64]; if BigEndian(accdesc.acctype) then value = BigEndianReverse(value); data<63+64*i : 64*i> = value; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; constant bits(64) status = MemStore64BWithRet(address, data, accdesc); if s != 31 then X[s, 64] = status;
```
