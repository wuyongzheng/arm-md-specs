## C6.2.343 REV32

Reverse bytes in 32-bit words

This instruction reverses the byte order in each 32-bit word of a register.

<!-- image -->

## Encoding

```
REV32 <Xd>, <Xn>
```

## Decode for this encoding

```
'0' then EndOfDecode(Decode_UNDEF);
```

```
if opc == '11' && sf == constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sf); constant integer container_size = 8 << UInt(opc);
```

## Assembler Symbols

&lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

&lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
constant bits(datasize) operand = X[n, datasize]; bits(datasize) result; constant integer containers = datasize DIV container_size; for c = 0 to containers-1 constant bits(container_size) container = Elem[operand, c, container_size]; Elem[result, c, container_size] = Reverse(container, 8); X[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
