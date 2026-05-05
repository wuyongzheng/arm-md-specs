## C6.2.382 ST64B

Single-copy atomic 64-byte store without status result

This instruction stores eight 64-bit doublewords from consecutive registers to a memory location. The store starts at register Xt , with the data being formed as Data[511:0] =

X(t+7)::X(t+6)::X(t+5)::X(t+4)::X(t+3)::X(t+2)::X(t+1)::Xt . The data is stored atomically and is required to be 64-byte aligned.

It is IMPLEMENTATION DEFINED which memory locations support this instruction. A memory location that supports ST64B also supports LD64B .

For more information, including about the memory types accessible and how the accesses are performed, see Single-copy atomic 64-byte load/store.

## Integer

(FEAT\_LS64)

<!-- image -->

## Encoding

```
ST64B <Xt>, [<Xn|SP>
```

```
{, #0}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LS64) then EndOfDecode(Decode_UNDEF); if Rt<4:3> == '11' || Rt<0> == '1' then EndOfDecode(Decode_UNDEF); constant boolean withstatus = FALSE; constant integer s = UInt(Rs); constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean tagchecked = n != 31;
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly ST64B.

## Assembler Symbols

&lt;Xt&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
CheckLDST64BEnabled(); bits(512) data; bits(64) address; bits(64) value; constant AccessDescriptor accdesc = CreateAccDescLS64(MemOp_STORE, withstatus, tagchecked); for i = 0 to 7
```

```
value = X[t+i, 64]; if BigEndian(accdesc.acctype) then value = BigEndianReverse(value); data<63+64*i : 64*i> = value; if n == 31 then CheckSPAlignment(); address = SP[64]; else address = X[n, 64]; MemStore64B(address, data, accdesc);
```
