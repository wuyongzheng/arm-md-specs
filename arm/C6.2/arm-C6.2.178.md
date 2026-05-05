## C6.2.178 LD64B

Single-copy atomic 64-byte Load

This instruction derives an address from a base register value, loads eight 64-bit doublewords from a memory location, and writes them to consecutive registers. The load starts at register Xt , with the data being read as

X(t+7)::X(t+6)::X(t+5)::X(t+4)::X(t+3)::X(t+2)::X(t+1)::Xt = Data[511:0] . The data is loaded atomically and is required to be 64-byte aligned.

It is IMPLEMENTATION DEFINED which memory locations support this instruction. A memory location that supports LD64B also supports ST64B .

For more information, including about the memory types accessible and how the accesses are performed, see Single-copy atomic 64-byte load/store.

## Integer

(FEAT\_LS64)

<!-- image -->

## Encoding

```
LD64B <Xt>, [<Xn|SP>
```

```
{, #0}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_LS64) then EndOfDecode(Decode_UNDEF); if Rt<4:3> == '11' || Rt<0> == '1' then EndOfDecode(Decode_UNDEF); constant boolean withstatus = FALSE; constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant boolean tagchecked = n != 31;
```

For information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly LD64B.

## Assembler Symbols

&lt;Xt&gt;

Is the 64-bit name of the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose base register or stack pointer, encoded in the 'Rn' field.

## Operation

```
CheckLDST64BEnabled(); bits(512) data; bits(64) address; bits(64) value; constant AccessDescriptor accdesc = CreateAccDescLS64(MemOp_LOAD, withstatus, tagchecked); if n == 31 then CheckSPAlignment();
```

```
address = SP[64]; else address = X[n, 64]; data = MemLoad64B(address, accdesc); for i = 0 to 7 value = data<63+64*i : 64*i>; if BigEndian(accdesc.acctype) then value = BigEndianReverse(value); X[t+i, 64] = value;
```
